from typing import List, Dict

def count_pods_per_namespace(pods: List[Dict]) -> Dict[str, int]:
    """
    Count how many pods are in each namespace.
    
    Return dict where keys are namespaces, values are counts.
    
    
    Should return: {'production': 3, 'staging': 2}
    """
    pods = [
        {'name': 'web-1', 'namespace': 'production'},
        {'name': 'web-2', 'namespace': 'production'},
        {'name': 'api-1', 'namespace': 'staging'},
        {'name': 'worker-1', 'namespace': 'production'},
        {'name': 'cache-1', 'namespace': 'staging'}
    ]

    # Create empty dict
    pods_per_ns = {}

    # Count groups
    for p in pods:
        ns = p['namespace']

        if ns not in pods_per_ns:
            pods_per_ns[ns] = 1
        else:
            pods_per_ns[ns] += 1

    return pods_per_ns

# At the bottom, outside the function:
if __name__ == "__main__":
    pods = [...]  # your test data
    
    result = count_pods_per_namespace(pods)
    print(f"Result: {result}")