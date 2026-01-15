from typing import List, Dict

def group_pods_by_namespace_and_status(pods: List[Dict]) -> Dict[str, Dict[str, List[str]]]:
    """
    Given a list of Kubernetes pods, group them by namespace, then by status.
    
    Each pod dict has:
    - 'name': string
    - 'namespace': string
    - 'status': string ('Running', 'Pending', 'Failed', 'Succeeded')
    
    Return a nested dictionary where:
    - Outer keys are namespace names
    - Inner keys are status values
    - Values are lists of pod names
    
    Should return: {
        'production': {
            'Running': ['web-1', 'web-2'],
            'Failed': ['worker-1'],
            'Pending': ['cache-1']
        },
        'staging': {
            'Running': ['api-1'],
            'Succeeded': ['job-1']
        }
    }
    """
    pods = [
        {'name': 'web-1', 'namespace': 'production', 'status': 'Running'},
        {'name': 'web-2', 'namespace': 'production', 'status': 'Running'},
        {'name': 'worker-1', 'namespace': 'production', 'status': 'Failed'},
        {'name': 'api-1', 'namespace': 'staging', 'status': 'Running'},
        {'name': 'job-1', 'namespace': 'staging', 'status': 'Succeeded'},
        {'name': 'cache-1', 'namespace': 'production', 'status': 'Pending'}
    ]

    groups = {}

    for p in pods:
        name = p['name']
        ns = p['namespace']
        status = p['status']

        if ns not in groups:
            groups[ns] = {} # Create empty list for this namespace

        if status not in groups[ns]:
            groups[ns][status] = [] # Create empty list for this status

        groups[ns][status].append(name)
    return groups

# Test
if __name__ == "__main__":
    pods = [
        {'name': 'web-1', 'namespace': 'production', 'status': 'Running'},
        {'name': 'web-2', 'namespace': 'production', 'status': 'Running'},
        {'name': 'worker-1', 'namespace': 'production', 'status': 'Failed'},
        {'name': 'api-1', 'namespace': 'staging', 'status': 'Running'},
        {'name': 'job-1', 'namespace': 'staging', 'status': 'Succeeded'},
        {'name': 'cache-1', 'namespace': 'production', 'status': 'Pending'}
    ]
    
    result = group_pods_by_namespace_and_status(pods)
    expected = {
        'production': {
            'Running': ['web-1', 'web-2'],
            'Failed': ['worker-1'],
            'Pending': ['cache-1']
        },
        'staging': {
            'Running': ['api-1'],
            'Succeeded': ['job-1']
        }
    }
    
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")