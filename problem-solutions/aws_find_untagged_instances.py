from typing import List, Dict

def find_untagged_instances(instances: List[Dict]) -> List[str]:
    """
    Given a list of EC2 instance dictionaries, return a list of instance IDs
    that are missing the 'Environment' tag.
    
    Each instance dict has:
    - 'instance_id': string
    - 'tags': dict of tag key-value pairs (may be empty)
    
    Example:
    instances = [
        {'instance_id': 'i-1234', 'tags': {'Environment': 'prod', 'Team': 'platform'}},
        {'instance_id': 'i-5678', 'tags': {'Team': 'data'}},  # Missing Environment
        {'instance_id': 'i-9012', 'tags': {}},  # No tags at all
        {'instance_id': 'i-3456', 'tags': {'Environment': 'dev'}}
    ]
    
    Should return: ['i-5678', 'i-9012']
    """
    untagged = [] # Empty list to collect results

    for instance in instances:
        # Check if 'Environment' key exists in the tags dictionary
        if 'Environment' not in instance['tags']:
            untagged.append(instance['instance_id'])
    return untagged

# Test
if __name__ == "__main__":
    instances = [
        {'instance_id': 'i-1234', 'tags': {'Environment': 'prod', 'Team': 'platform'}},
        {'instance_id': 'i-5678', 'tags': {'Team': 'data'}},
        {'instance_id': 'i-9012', 'tags': {}},
        {'instance_id': 'i-3456', 'tags': {'Environment': 'dev'}}
    ]
    
    result = find_untagged_instances(instances)
    expected = ['i-5678', 'i-9012']
    print(f"Untagged instances: {result}")
    print(f"Expected: {expected}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")