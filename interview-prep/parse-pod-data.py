from typing import List, Dict

def find_pods_with_failing_containers(pods: List[Dict]) -> List[str]:
    """
    Given a list of Kubernetes pod objects, return the names of pods that 
    have at least one container in a non-running state.
    
    Each pod dict has:
    - 'name': string (pod name)
    - 'containers': list of dicts, each with:
        - 'name': string (container name)
        - 'state': string ('running', 'waiting', 'terminated')
    
    A pod is failing if ANY of its containers have state != 'running'
    
    Example:
    pods = [
        {
            'name': 'web-app-abc123',
            'containers': [
                {'name': 'nginx', 'state': 'running'},
                {'name': 'app', 'state': 'running'}
            ]
        },
        {
            'name': 'worker-def456',
            'containers': [
                {'name': 'worker', 'state': 'waiting'},
                {'name': 'sidecar', 'state': 'running'}
            ]
        },
        {
            'name': 'cache-ghi789',
            'containers': [
                {'name': 'redis', 'state': 'running'}
            ]
        },
        {
            'name': 'api-jkl012',
            'containers': [
                {'name': 'api', 'state': 'terminated'},
                {'name': 'proxy', 'state': 'terminated'}
            ]
        }
    ]
    
    Should return: ['worker-def456', 'api-jkl012']
    
    Explanation:
    - web-app-abc123: All containers running (not returned)
    - worker-def456: 'worker' container is waiting (returned)
    - cache-ghi789: All containers running (not returned)
    - api-jkl012: Both containers terminated (returned)
    """
    pods = [
        {
            'name': 'web-app-abc123',
            'containers': [
                {'name': 'nginx', 'state': 'running'},
                {'name': 'app', 'state': 'running'}
            ]
        },
        {
            'name': 'worker-def456',
            'containers': [
                {'name': 'worker', 'state': 'waiting'},
                {'name': 'sidecar', 'state': 'running'}
            ]
        },
        {
            'name': 'cache-ghi789',
            'containers': [
                {'name': 'redis', 'state': 'running'}
            ]
        },
        {
            'name': 'api-jkl012',
            'containers': [
                {'name': 'api', 'state': 'terminated'},
                {'name': 'proxy', 'state': 'terminated'}
            ]
        }
    ]
    
    not_running = []

    for p in pods:
        for c in p['containers']:
            if c['state'] != 'running':
                not_running.append(p['name'])
                break

    return not_running

# Test
if __name__ == "__main__":
    pods = [
        {
            'name': 'web-app-abc123',
            'containers': [
                {'name': 'nginx', 'state': 'running'},
                {'name': 'app', 'state': 'running'}
            ]
        },
        {
            'name': 'worker-def456',
            'containers': [
                {'name': 'worker', 'state': 'waiting'},
                {'name': 'sidecar', 'state': 'running'}
            ]
        },
        {
            'name': 'cache-ghi789',
            'containers': [
                {'name': 'redis', 'state': 'running'}
            ]
        },
        {
            'name': 'api-jkl012',
            'containers': [
                {'name': 'api', 'state': 'terminated'},
                {'name': 'proxy', 'state': 'terminated'}
            ]
        }
    ]
    
    result = find_pods_with_failing_containers(pods)
    expected = ['worker-def456', 'api-jkl012']
    print(f"Failing pods: {result}")
    print(f"Expected: {expected}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")