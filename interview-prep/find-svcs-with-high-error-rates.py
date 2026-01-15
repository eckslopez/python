from typing import List, Dict

def find_services_with_high_error_rate(services: List[Dict]) -> List[str]:
    """
    Given a list of service metrics, return names of services where 
    the error rate is 5% or higher.
    
    Error rate = (errors / total_requests) * 100
    
    Each service dict has:
    - 'name': string
    - 'total_requests': int
    - 'errors': int
    
    Explanation:
    - auth-service: 30/1000 = 3% (below threshold)
    - api-gateway: 150/5000 = 3% (below threshold)
    - worker-queue: 50/2000 = 2.5% (below threshold)
    - cache-redis: 100/10000 = 1% (below threshold)
    
    Wait, let me recalculate...
    - auth-service: (30/1000)*100 = 3%
    - api-gateway: (150/5000)*100 = 3%
    - worker-queue: (50/2000)*100 = 2.5%
    - cache-redis: (100/10000)*100 = 1%
    
    Hmm, none are >= 5%. Let me fix the data...
    """
    services = [
        {'name': 'auth-service', 'total_requests': 1000, 'errors': 30},
        {'name': 'api-gateway', 'total_requests': 5000, 'errors': 150},
        {'name': 'worker-queue', 'total_requests': 2000, 'errors': 50},
        {'name': 'cache-redis', 'total_requests': 10000, 'errors': 100}
    ]
    #Should return: ['worker-queue', 'cache-redis']
    # Create emtpy list for high error rates
    high_error_rates = []
    
    for svc in services:
        # Calculate error rates and check if higher than or equal to 5%
        if (svc['errors'] / svc['total_requests']) * 100 >= 5:
            high_error_rates.append(svc['name'])
    
    return high_error_rates
    


# Test
if __name__ == "__main__":
    services = [
        {'name': 'auth-service', 'total_requests': 1000, 'errors': 30},
        {'name': 'api-gateway', 'total_requests': 5000, 'errors': 250},
        {'name': 'worker-queue', 'total_requests': 2000, 'errors': 120},
        {'name': 'cache-redis', 'total_requests': 10000, 'errors': 100}
    ]
    
    result = find_services_with_high_error_rate(services)
    expected = ['api-gateway', 'worker-queue']
    print(f"High error rate services: {result}")
    print(f"Expected: {expected}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")