from typing import List, Dict

def get_running_instances(instances: List[Dict]) -> List[str]:
    """
    Given a list of EC2 instances, return instance IDs of only those 
    that are in 'running' state.
    
    Each instance dict has:
    - 'instance_id': string
    - 'state': string ('running', 'stopped', 'terminated', etc.)
    - 'instance_type': string (e.g., 't3.micro')
    
    Example:
    instances = [
        {'instance_id': 'i-1111', 'state': 'running', 'instance_type': 't3.micro'},
        {'instance_id': 'i-2222', 'state': 'stopped', 'instance_type': 't3.small'},
        {'instance_id': 'i-3333', 'state': 'running', 'instance_type': 't3.medium'},
        {'instance_id': 'i-4444', 'state': 'terminated', 'instance_type': 't3.micro'}
    ]
    
    Should return: ['i-1111', 'i-3333']
    """
    # Create empty array to collect the ids of running instances
    running = []

    for instance in instances:
        # Check if value of key 'state' is 'running'
        if instance['state'] == 'running':
            running.append(instance['instance_id'])
    return running 


# Test
if __name__ == "__main__":
    instances = [
        {'instance_id': 'i-1111', 'state': 'running', 'instance_type': 't3.micro'},
        {'instance_id': 'i-2222', 'state': 'stopped', 'instance_type': 't3.small'},
        {'instance_id': 'i-3333', 'state': 'running', 'instance_type': 't3.medium'},
        {'instance_id': 'i-4444', 'state': 'terminated', 'instance_type': 't3.micro'}
    ]
    
    result = get_running_instances(instances)
    expected = ['i-1111', 'i-3333']
    print(f"Running instances: {result}")
    print(f"Expected: {expected}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")