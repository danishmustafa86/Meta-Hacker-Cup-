def find_divisor(B, A):
    """
    Find the largest divisor of B that is <= A
    
    Args:
        B: Target final coolness
        A: Maximum allowed coolness after N days
    
    Returns:
        Largest divisor of B that is <= A
    """
    for d in range(min(A, B), 0, -1):
        if B % d == 0:
            return d
    return 1

def solve_case(N, A, B):
    """
    Solve a single test case
    
    Strategy:
    1. Find intermediate value (divisor of B that is <= A)
    2. First N days: multiply to reach intermediate value
    3. Next N days: multiply to reach B from intermediate value
    
    Args:
        N: Number of days in each phase (total days = 2*N)
        A: Maximum coolness allowed after N days
        B: Target coolness after 2*N days
    
    Returns:
        List of 2*N multipliers
    """
    # Find intermediate value after N days (must be divisor of B and <= A)
    intermediate = find_divisor(B, A)
    
    # Calculate what we need to multiply in second phase
    second_phase = B // intermediate
    
    # Build the sequence
    result = []
    
    # First N days: reach intermediate value
    # Use (N-1) multipliers of 1, then multiply by intermediate on day N
    for _ in range(N - 1):
        result.append(1)
    result.append(intermediate)
    
    # Next N days: reach B from intermediate
    # Use (N-1) multipliers of 1, then multiply by second_phase on day 2*N
    for _ in range(N - 1):
        result.append(1)
    result.append(second_phase)
    
    return result

def main():
    """
    Main function to read input and solve all test cases
    """
    T = int(input())
    
    for case_num in range(1, T + 1):
        N, A, B = map(int, input().split())
        result = solve_case(N, A, B)
        print(f"Case #{case_num}: {' '.join(map(str, result))}")

if __name__ == "__main__":
    main()