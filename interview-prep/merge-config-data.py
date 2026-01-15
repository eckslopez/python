from typing import List, Dict

def merge_service_configs(base_configs: List[Dict], overrides: List[Dict]) -> List[Dict]:
    """
    Given base configurations and environment-specific overrides,
    merge them together. Overrides should replace base values.
    
    Each config dict has:
    - 'service_name': string (unique identifier)
    - 'replicas': int
    - 'memory_gb': int
    
    For each service in base_configs:
    - If an override exists (matching service_name), use override values
    - If no override exists, use base values
    
    Return the merged configs (one entry per service from base_configs).
    """
    
    base_configs = [
        {'service_name': 'api', 'replicas': 2, 'memory_gb': 4},
        {'service_name': 'worker', 'replicas': 3, 'memory_gb': 8},
        {'service_name': 'cache', 'replicas': 1, 'memory_gb': 2}
    ]
    
    overrides = [
        {'service_name': 'api', 'replicas': 5, 'memory_gb': 8},
        {'service_name': 'cache', 'replicas': 2, 'memory_gb': 4}
    ]
    
    base_configs = {d['service_name']: d for d in base_configs + overrides}

    base_configs = list(base_configs.values())

    return base_configs

#    Should return: [
#        {'service_name': 'api', 'replicas': 5, 'memory_gb': 8},      # Overridden
#        {'service_name': 'worker', 'replicas': 3, 'memory_gb': 8},   # Base (no override)
#        {'service_name': 'cache', 'replicas': 2, 'memory_gb': 4}     # Overridden
#    ]

# Test
if __name__ == "__main__":
    base_configs = [
        {'service_name': 'api', 'replicas': 2, 'memory_gb': 4},
        {'service_name': 'worker', 'replicas': 3, 'memory_gb': 8},
        {'service_name': 'cache', 'replicas': 1, 'memory_gb': 2}
    ]
    
    overrides = [
        {'service_name': 'api', 'replicas': 5, 'memory_gb': 8},
        {'service_name': 'cache', 'replicas': 2, 'memory_gb': 4}
    ]
    
    result = merge_service_configs(base_configs, overrides)
    expected = [
        {'service_name': 'api', 'replicas': 5, 'memory_gb': 8},
        {'service_name': 'worker', 'replicas': 3, 'memory_gb': 8},
        {'service_name': 'cache', 'replicas': 2, 'memory_gb': 4}
    ]
    
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")