from typing import List, Dict

def count_by_instance_type(instances: List[Dict]) -> Dict[str, int]:
    """
    Given a list of EC2 instances, return a dictionary counting how many
    instances of each type exist.
    
    Each instance dict has:
    - 'instance_id': string
    - 'instance_type': string (e.g., 't3.micro', 't3.small')
    
    Example:
    instances = [
        {'instance_id': 'i-1111', 'instance_type': 't3.micro'},
        {'instance_id': 'i-2222', 'instance_type': 't3.small'},
        {'instance_id': 'i-3333', 'instance_type': 't3.micro'},
        {'instance_id': 'i-4444', 'instance_type': 't3.micro'},
        {'instance_id': 'i-5555', 'instance_type': 't3.large'}
    ]
    
    Should return: {'t3.micro': 3, 't3.small': 1, 't3.large': 1}
    """
    counts = {}
    
    for i in instances:
        instance_type = i['instance_type'] # Get the type

        if instance_type in counts:
            counts[instance_type] += 1 # Increment
        else:
            counts[instance_type] = 1

    return counts
        



 
# Test
if __name__ == "__main__":
    instances = [
        {'instance_id': 'i-1111', 'instance_type': 't3.micro'},
        {'instance_id': 'i-2222', 'instance_type': 't3.small'},
        {'instance_id': 'i-3333', 'instance_type': 't3.micro'},
        {'instance_id': 'i-4444', 'instance_type': 't3.micro'},
        {'instance_id': 'i-5555', 'instance_type': 't3.large'}
    ]
    
    result = count_by_instance_type(instances)
    expected = {'t3.micro': 3, 't3.small': 1, 't3.large': 1}
    print(f"Instance counts: {result}")
    print(f"Expected: {expected}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")