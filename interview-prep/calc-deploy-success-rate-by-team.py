from typing import List, Dict

def calculate_deployment_success_rates(deployments: List[Dict]) -> Dict[str, float]:
    """
    Given deployment history, calculate success rate for each team.
    
    Success rate = (successful_deploys / total_deploys) * 100
    
    Each deployment dict has:
    - 'team': string
    - 'status': string ('success' or 'failed')
    
    Return dict where:
    - Keys are team names
    - Values are success rates (rounded to 2 decimal places)
    
    """
    deployments = [
        {'team': 'backend', 'status': 'success'},
        {'team': 'backend', 'status': 'success'},
        {'team': 'backend', 'status': 'failed'},
        {'team': 'frontend', 'status': 'success'},
        {'team': 'frontend', 'status': 'success'},
        {'team': 'frontend', 'status': 'success'},
        {'team': 'data', 'status': 'failed'},
        {'team': 'data', 'status': 'success'}
    ]

    team_stats = {}

    for deploy in deployments:
        team = deploy['team']

        if team not in team_stats:
            team_stats[team] = {'success': 0, 'total': 0}

        # Increment total every time
        team_stats[team]['total'] += 1
        
        # Increment successes if status is 'success'
        if deploy['status'] == 'success':
            team_stats[team]['success'] += 1

    success_rates = {}

    # When you loop through a dictionary with .items(), you get BOTH the key AND the value:
    for team, stats in team_stats.items():
        rate = (stats['success'] / stats['total']) * 100
        success_rates[team] = round(rate, 2)

    return success_rates
    
        
    
       
    #Should return: {
    #    'backend': 66.67,    # 2 success out of 3 total
    #    'frontend': 100.0,   # 3 success out of 3 total
    #    'data': 50.0         # 1 success out of 2 total
    #}

# Test
if __name__ == "__main__":
    deployments = [
        {'team': 'backend', 'status': 'success'},
        {'team': 'backend', 'status': 'success'},
        {'team': 'backend', 'status': 'failed'},
        {'team': 'frontend', 'status': 'success'},
        {'team': 'frontend', 'status': 'success'},
        {'team': 'frontend', 'status': 'success'},
        {'team': 'data', 'status': 'failed'},
        {'team': 'data', 'status': 'success'}
    ]
    
    result = calculate_deployment_success_rates(deployments)
    expected = {
        'backend': 66.67,
        'frontend': 100.0,
        'data': 50.0
    }
    
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")