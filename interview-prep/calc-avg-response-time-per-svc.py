from typing import List, Dict

def calculate_avg_response_times(requests: List[Dict]) -> Dict[str, float]:
    """
    Calculate average response time for each service.
    
    Each request dict has:
    - 'service': string
    - 'response_time_ms': int
    
    Return dict where:
    - Keys are service names
    - Values are average response times (rounded to 2 decimals)
    
    Should return: {
        'api': 150.0,     # (100 + 150 + 200) / 3
        'db': 60.0,       # (50 + 70) / 2
        'cache': 10.0     # 10 / 1
    }
    """
    requests = [
        {'service': 'api', 'response_time_ms': 100},
        {'service': 'api', 'response_time_ms': 150},
        {'service': 'api', 'response_time_ms': 200},
        {'service': 'db', 'response_time_ms': 50},
        {'service': 'db', 'response_time_ms': 70},
        {'service': 'cache', 'response_time_ms': 10}
    ]

    average_rt = {}
    for r in requests:
        svc = r['service']
        rt = r['response_time_ms'] 

        if r['service'] not in average_rt:
            average_rt[svc] = []
        
        average_rt[svc].append(rt)

    for value in average_rt.values():
        value = round(sum(value) / len(value), 2)

if __name__ == "__main__":
    calculate_avg_response_times([])
        

            

