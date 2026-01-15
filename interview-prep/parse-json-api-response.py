from typing import List, Dict

def get_unhealthy_services(services: List[Dict]) -> List[str]:
    """
    Given a list of service health check responses, return the names of 
    services that are NOT healthy.
    
    A service is unhealthy if:
    - status is not "healthy"
    - OR response_time_ms is greater than 1000
    
    Each service dict has:
    - 'name': string
    - 'status': string ('healthy', 'degraded', 'down')
    - 'response_time_ms': int (milliseconds)
    
    Example:
    services = [
        {'name': 'api-gateway', 'status': 'healthy', 'response_time_ms': 245},
        {'name': 'auth-service', 'status': 'degraded', 'response_time_ms': 450},
        {'name': 'db-primary', 'status': 'healthy', 'response_time_ms': 1200},
        {'name': 'cache-redis', 'status': 'down', 'response_time_ms': 0},
        {'name': 'worker-queue', 'status': 'healthy', 'response_time_ms': 180}
    ]
    
    Should return: ['auth-service', 'db-primary', 'cache-redis']
    
    Explanation:
    - api-gateway: healthy and fast (not returned)
    - auth-service: degraded status (returned)
    - db-primary: healthy but slow >1000ms (returned)
    - cache-redis: down status (returned)
    - worker-queue: healthy and fast (not returned)
    """
    # YOUR CODE HERE
    services = [
        {'name': 'api-gateway', 'status': 'healthy', 'response_time_ms': 245},
        {'name': 'auth-service', 'status': 'degraded', 'response_time_ms': 450},
        {'name': 'db-primary', 'status': 'healthy', 'response_time_ms': 1200},
        {'name': 'cache-redis', 'status': 'down', 'response_time_ms': 0},
        {'name': 'worker-queue', 'status': 'healthy', 'response_time_ms': 180}
    ]

    # A place for unhealthy services
    unhealthy_services = []

    for svc in services:
        if svc['status'] != 'healthy' or  svc['response_time_ms'] > 1000:
            unhealthy_services.append(svc['name'])

    return unhealthy_services 
    

# Test
if __name__ == "__main__":
    services = [
        {'name': 'api-gateway', 'status': 'healthy', 'response_time_ms': 245},
        {'name': 'auth-service', 'status': 'degraded', 'response_time_ms': 450},
        {'name': 'db-primary', 'status': 'healthy', 'response_time_ms': 1200},
        {'name': 'cache-redis', 'status': 'down', 'response_time_ms': 0},
        {'name': 'worker-queue', 'status': 'healthy', 'response_time_ms': 180}
    ]
    
    result = get_unhealthy_services(services)
    expected = ['auth-service', 'db-primary', 'cache-redis']
    print(f"Unhealthy services: {result}")
    print(f"Expected: {expected}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")