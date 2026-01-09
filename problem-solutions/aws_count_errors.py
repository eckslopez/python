from typing import List

def count_errors(log_lines: List[str]) -> int:
    """
    Given a list of log lines, return the count of lines containing 'ERROR'.
    
    Example:
    logs = [
        "2024-01-08 10:23:45 INFO Server started",
        "2024-01-08 10:24:12 ERROR Database connection failed",
        "2024-01-08 10:24:15 WARN Retrying connection",
        "2024-01-08 10:24:20 ERROR Connection timeout"
    ]
    
    count_errors(logs) should return 2
    """
    # YOUR CODE HERE
    substring = 'ERROR'
    count = 0
    for log in log_lines:
        if substring in log:
            count = count + 1 
    return count

# Test your function
if __name__ == "__main__":
    logs = [
        "2024-01-08 10:23:45 INFO Server started",
        "2024-01-08 10:24:12 ERROR Database connection failed",
        "2024-01-08 10:24:15 WARN Retrying connection",
        "2024-01-08 10:24:20 ERROR Connection timeout",
        "2024-01-08 10:24:25 INFO Request processed"
    ]
    
    result = count_errors(logs)
    print(f"Error count: {result}")
    print(f"Expected: 2")
    print(f"Test {'PASSED' if result == 2 else 'FAILED'}")