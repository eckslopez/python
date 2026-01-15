from typing import List, Dict

def parse_error_logs(log_lines: List[str]) -> List[Dict[str, str]]:
    """
    Parse error log lines and extract structured information.
    
    Each log line has format:
    "[TIMESTAMP] LEVEL: message"
    
    Example: "[2024-01-15 10:23:45] ERROR: Database connection failed"
    
    Extract only ERROR level logs and return a list of dicts with:
    - 'timestamp': the timestamp string (without brackets)
    - 'message': the error message (after "ERROR: ")
    
    Should return: [
        {'timestamp': '2024-01-15 10:23:45', 'message': 'Database connection failed'},
        {'timestamp': '2024-01-15 10:24:20', 'message': 'Connection timeout after 30s'}
    ]
    
    """
    logs = [
        "[2024-01-15 10:23:45] INFO: Server started",
        "[2024-01-15 10:24:12] ERROR: Database connection failed",
        "[2024-01-15 10:24:15] WARN: Retrying connection",
        "[2024-01-15 10:24:20] ERROR: Connection timeout after 30s"
    ]

    # Create an empty list, to be filled with dictionaries, later
    errors = []

    # Add values to dict 
    for log in logs:
        if "ERROR: " in log:
            # Create a new dict for each error, to be appended to the list
            error = {
                'timestamp': log[1:20], # Extract timestample
                'message': log[29:]     # Extract message
            }
            errors.append(error)
    
    return errors

# Test
if __name__ == "__main__":
    logs = [
        "[2024-01-15 10:23:45] INFO: Server started",
        "[2024-01-15 10:24:12] ERROR: Database connection failed",
        "[2024-01-15 10:24:15] WARN: Retrying connection",
        "[2024-01-15 10:24:20] ERROR: Connection timeout after 30s",
        "[2024-01-15 10:24:25] INFO: Request processed"
    ]
    
    result = parse_error_logs(logs)
    expected = [
        {'timestamp': '2024-01-15 10:24:12', 'message': 'Database connection failed'},
        {'timestamp': '2024-01-15 10:24:20', 'message': 'Connection timeout after 30s'}
    ]
    
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")