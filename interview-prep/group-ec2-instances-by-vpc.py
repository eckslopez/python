from typing import List, Dict

def group_instances_by_vpc(instances: List[Dict]) -> Dict[str, List[str]]:
    """
    Given a list of EC2 instances, group them by VPC ID.
    
    Each instance dict has:
    - 'instance_id': string
    - 'vpc_id': string
    - 'instance_type': string
    
    Return a dictionary where:
    - Keys are VPC IDs
    - Values are lists of instance IDs in that VPC
    
    Example:
    
    Should return: {
        'vpc-aaa': ['i-1111', 'i-3333', 'i-4444'],
        'vpc-bbb': ['i-2222', 'i-6666'],
        'vpc-ccc': ['i-5555']
    }
    """
    instances = [
        {'instance_id': 'i-1111', 'vpc_id': 'vpc-aaa', 'instance_type': 't3.micro'},
        {'instance_id': 'i-2222', 'vpc_id': 'vpc-bbb', 'instance_type': 't3.small'},
        {'instance_id': 'i-3333', 'vpc_id': 'vpc-aaa', 'instance_type': 't3.medium'},
        {'instance_id': 'i-4444', 'vpc_id': 'vpc-aaa', 'instance_type': 't3.micro'},
        {'instance_id': 'i-5555', 'vpc_id': 'vpc-ccc', 'instance_type': 't3.large'},
        {'instance_id': 'i-6666', 'vpc_id': 'vpc-bbb', 'instance_type': 't3.small'}
    ]
    
    groups = {}

    for instance in instances:
        vpc_id = instance['vpc_id']
        instance_id = instance['instance_id']

        if vpc_id not in groups:
            groups[vpc_id] = [] # Create empty list for this VPC

        groups[vpc_id].append(instance_id) # Add instance to the list
    
    return groups


# Test
if __name__ == "__main__":
    instances = [
        {'instance_id': 'i-1111', 'vpc_id': 'vpc-aaa', 'instance_type': 't3.micro'},
        {'instance_id': 'i-2222', 'vpc_id': 'vpc-bbb', 'instance_type': 't3.small'},
        {'instance_id': 'i-3333', 'vpc_id': 'vpc-aaa', 'instance_type': 't3.medium'},
        {'instance_id': 'i-4444', 'vpc_id': 'vpc-aaa', 'instance_type': 't3.micro'},
        {'instance_id': 'i-5555', 'vpc_id': 'vpc-ccc', 'instance_type': 't3.large'},
        {'instance_id': 'i-6666', 'vpc_id': 'vpc-bbb', 'instance_type': 't3.small'}
    ]
    
    result = group_instances_by_vpc(instances)
    expected = {
        'vpc-aaa': ['i-1111', 'i-3333', 'i-4444'],
        'vpc-bbb': ['i-2222', 'i-6666'],
        'vpc-ccc': ['i-5555']
    }
    
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")