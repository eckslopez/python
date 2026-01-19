from typing import List, Dict

def find_resource_hungry_pods(pods: List[Dict]) -> List[str]:
    """
    Find pods using excessive resources.
    
    A pod is "resource hungry" if:
    - cpu_millicores > 500 OR memory_mb > 1024
    
    Return list of pod names.
    
    Should return: ['api-2', 'worker-3']
    """
    pods = [
        {'name': 'web-1', 'cpu_millicores': 300, 'memory_mb': 512},
        {'name': 'api-2', 'cpu_millicores': 600, 'memory_mb': 800},
        {'name': 'worker-3', 'cpu_millicores': 400, 'memory_mb': 1500},
        {'name': 'cache-4', 'cpu_millicores': 200, 'memory_mb': 256}
    ]
    
    hungry_pods = []
    
    for p in pods:
        if p['cpu_millicores'] > 500 or p['memory_mb'] > 1024:
            hungry_pods.append(p['name'])
    
    return hungry_pods
