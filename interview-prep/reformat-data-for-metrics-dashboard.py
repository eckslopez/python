from typing import List, Dict

def transform_metrics_for_dashboard(raw_metrics: List[Dict]) -> Dict[str, List[int]]:
    """
    Given raw time-series metrics, transform them into a format for charting.
    
    Input: List of metric snapshots with timestamp
    Output: Dict where keys are metric names, values are lists of values over time
    
    Each raw metric dict has:
    - 'timestamp': string (not needed in output)
    - 'cpu_percent': int
    - 'memory_percent': int
    - 'disk_percent': int
    """
    raw_metrics = [
        {'timestamp': '10:00', 'cpu_percent': 45, 'memory_percent': 60, 'disk_percent': 30},
        {'timestamp': '10:01', 'cpu_percent': 50, 'memory_percent': 62, 'disk_percent': 30},
        {'timestamp': '10:02', 'cpu_percent': 48, 'memory_percent': 65, 'disk_percent': 31}
    ]

    transformation = {}
    transformation['cpu_percent'] = []
    transformation['memory_percent'] = []
    transformation['disk_percent'] = []

    for log in raw_metrics:
        cpu_percent = log['cpu_percent']
        memory_percent = log['memory_percent']
        disk_percent = log['disk_percent']

        transformation['cpu_percent'].append(cpu_percent)
        transformation['memory_percent'].append(memory_percent)
        transformation['disk_percent'].append(disk_percent)
    
    return transformation

    #Should return: {
    #    'cpu_percent': [45, 50, 48],
    #    'memory_percent': [60, 62, 65],
    #    'disk_percent': [30, 30, 31]
    #}

# Test
if __name__ == "__main__":
    raw_metrics = [
        {'timestamp': '10:00', 'cpu_percent': 45, 'memory_percent': 60, 'disk_percent': 30},
        {'timestamp': '10:01', 'cpu_percent': 50, 'memory_percent': 62, 'disk_percent': 30},
        {'timestamp': '10:02', 'cpu_percent': 48, 'memory_percent': 65, 'disk_percent': 31}
    ]
    
    result = transform_metrics_for_dashboard(raw_metrics)
    expected = {
        'cpu_percent': [45, 50, 48],
        'memory_percent': [60, 62, 65],
        'disk_percent': [30, 30, 31]
    }
    
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")