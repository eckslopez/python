from typing import List, Dict

def calculate_cluster_stats(nodes: List[Dict]) -> Dict[str, float]:
    """
    Given a list of Kubernetes nodes with resource usage, return statistics
    about the cluster.
    
    Each node dict has:
    - 'name': string
    - 'cpu_used': int (CPU cores used)
    - 'cpu_total': int (total CPU cores)
    - 'memory_used_gb': int (GB used)
    - 'memory_total_gb': int (total GB)
    
    Return a dict with:
    - 'total_cpu_used': sum of all cpu_used
    - 'total_cpu_available': sum of all cpu_total
    - 'total_memory_used_gb': sum of all memory_used_gb
    - 'total_memory_available_gb': sum of all memory_total_gb
    - 'avg_cpu_utilization_percent': average CPU utilization across all nodes
    - 'avg_memory_utilization_percent': average memory utilization across all nodes
    
    Utilization percent = (used / total) * 100
    
    Example:
    nodes = [
        {'name': 'node-1', 'cpu_used': 6, 'cpu_total': 8, 'memory_used_gb': 12, 'memory_total_gb': 16},
        {'name': 'node-2', 'cpu_used': 4, 'cpu_total': 8, 'memory_used_gb': 10, 'memory_total_gb': 16},
        {'name': 'node-3', 'cpu_used': 7, 'cpu_total': 8, 'memory_used_gb': 14, 'memory_total_gb': 16}
    ]
    
    Should return: {
        'total_cpu_used': 17,
        'total_cpu_available': 24,
        'total_memory_used_gb': 36,
        'total_memory_available_gb': 48,
        'avg_cpu_utilization_percent': 70.83,  # (6/8 + 4/8 + 7/8) / 3 * 100
        'avg_memory_utilization_percent': 75.0  # (12/16 + 10/16 + 14/16) / 3 * 100
    }
    
    Note: Round averages to 2 decimal places using round(value, 2)
    """
    nodes = [
        {'name': 'node-1', 'cpu_used': 6, 'cpu_total': 8, 'memory_used_gb': 12, 'memory_total_gb': 16},
        {'name': 'node-2', 'cpu_used': 4, 'cpu_total': 8, 'memory_used_gb': 10, 'memory_total_gb': 16},
        {'name': 'node-3', 'cpu_used': 7, 'cpu_total': 8, 'memory_used_gb': 14, 'memory_total_gb': 16}
    ]

    total_cpu_used = 0
    total_cpu_available = 0
    total_memory_used_gb = 0
    total_memory_available_gb = 0
    avg_cpu_utilization_percent = 0
    avg_memory_utilization_percent = 0

    for n in nodes:
        total_cpu_used += n['cpu_used']
        total_cpu_available += n['cpu_total']
        total_memory_used_gb += n['memory_used_gb']
        total_memory_available_gb += n['memory_total_gb']
        avg_cpu_utilization_percent += (n['cpu_used'] / n['cpu_total']) * 100
        avg_memory_utilization_percent += (n['memory_used_gb'] / n['memory_total_gb']) * 100

    return {
        'total_cpu_used': total_cpu_used,
        'total_cpu_available': total_cpu_available,
        'total_memory_used_gb': total_memory_used_gb,
        'total_memory_available_gb': total_memory_available_gb,
        'avg_cpu_utilization_percent': round((avg_cpu_utilization_percent / 3), 2),
        'avg_memory_utilization_percent': round((avg_memory_utilization_percent / 3), 2)
    }

# Test
if __name__ == "__main__":
    nodes = [
        {'name': 'node-1', 'cpu_used': 6, 'cpu_total': 8, 'memory_used_gb': 12, 'memory_total_gb': 16},
        {'name': 'node-2', 'cpu_used': 4, 'cpu_total': 8, 'memory_used_gb': 10, 'memory_total_gb': 16},
        {'name': 'node-3', 'cpu_used': 7, 'cpu_total': 8, 'memory_used_gb': 14, 'memory_total_gb': 16}
    ]
    
    result = calculate_cluster_stats(nodes)
    expected = {
        'total_cpu_used': 17,
        'total_cpu_available': 24,
        'total_memory_used_gb': 36,
        'total_memory_available_gb': 48,
        'avg_cpu_utilization_percent': 70.83,
        'avg_memory_utilization_percent': 75.0
    }
    
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")