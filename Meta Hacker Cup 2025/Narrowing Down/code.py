def calculate_cost(arr):
    """
    Calculate minimum cost to flatten array to all zeros.
    
    Rules:
    - If all elements are 0: cost = 0
    - If single element != 0: cost = 1 (impossible to flatten)
    - If XOR of all elements != 0: cost = length (impossible to flatten)
    - If XOR = 0 and not all zero: count transitions where value changes
    """
    n = len(arr)
    
    # Check if all zeros
    if all(x == 0 for x in arr):
        return 0
    
    # Single element that's not zero
    if n == 1:
        return 1
    
    # Calculate XOR of all elements
    xor_sum = 0
    for x in arr:
        xor_sum ^= x
    
    # If XOR != 0, impossible to flatten
    if xor_sum != 0:
        return n
    
    # If XOR = 0, check if all elements are the same
    if len(set(arr)) == 1:
        return 1
    
    # Count contiguous non-zero segments
    num_segments = 0
    in_segment = False
    for x in arr:
        if x != 0:
            if not in_segment:
                num_segments += 1
                in_segment = True
        else:
            in_segment = False
    
    # Count transitions between non-zero elements
    non_zero_transitions = 0
    for i in range(n - 1):
        if arr[i] != 0 and arr[i + 1] != 0 and arr[i] != arr[i + 1]:
            non_zero_transitions += 1
    
    # If only one segment: cost is based on transitions
    # If multiple segments: add segment count + 1
    if num_segments == 1:
        return max(1, non_zero_transitions)
    else:
        return num_segments + 1 + non_zero_transitions


def solve_case(n, arr):
    """
    Calculate sum of costs for all contiguous subarrays.
    """
    total_cost = 0
    
    # Iterate through all contiguous subarrays
    for left in range(n):
        for right in range(left, n):
            subarray = arr[left:right+1]
            cost = calculate_cost(subarray)
            total_cost += cost
    
    return total_cost


def main():
    T = int(input())
    
    for case_num in range(1, T + 1):
        N = int(input())
        A = list(map(int, input().split()))
        
        result = solve_case(N, A)
        print(f"Case #{case_num}: {result}")


if __name__ == "__main__":
    main()

