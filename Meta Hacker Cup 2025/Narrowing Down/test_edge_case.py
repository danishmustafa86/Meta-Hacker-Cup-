def calculate_cost_current(arr):
    n = len(arr)
    if all(x == 0 for x in arr):
        return 0
    if n == 1:
        return 1
    xor_sum = 0
    for x in arr:
        xor_sum ^= x
    if xor_sum != 0:
        return n
    if len(set(arr)) == 1:
        return 1
    
    num_segments = 0
    in_segment = False
    for x in arr:
        if x != 0:
            if not in_segment:
                num_segments += 1
                in_segment = True
        else:
            in_segment = False
    
    non_zero_transitions = 0
    for i in range(n - 1):
        if arr[i] != 0 and arr[i + 1] != 0 and arr[i] != arr[i + 1]:
            non_zero_transitions += 1
    
    if num_segments == 1:
        return max(1, non_zero_transitions)
    else:
        return num_segments + 1 + non_zero_transitions

# Test edge case: [1, 0, 1]
print("Testing [1, 0, 1]:")
print(f"  Current algorithm: {calculate_cost_current([1, 0, 1])}")
print(f"  Manual trace: [1,0,1] -> pick i=1,x=1 -> [0,1,1] -> pick i=2,x=1 -> [0,0,0] = 2 operations")
print(f"  Expected: 2")
print(f"  XOR: {1^0^1}")
print()

# Another edge case: [2, 0, 2]
print("Testing [2, 0, 2]:")
print(f"  Current algorithm: {calculate_cost_current([2, 0, 2])}")
print(f"  Expected: 2 (same logic)")
print()

# Edge case with different values: [1, 0, 2, 0, 3]
print("Testing [1, 0, 2, 0, 3] (XOR=0):")
arr = [1, 0, 2, 0, 3]
print(f"  Current algorithm: {calculate_cost_current(arr)}")
print(f"  XOR: {1^0^2^0^3}")
print(f"  Segments: 3, Transitions: 0")
print(f"  Current gives: 3+1+0=4")
print(f"  n-1 gives: 5-1=4")
print()

# The key insight: when segments contain the SAME value, we shouldn't add overhead
print("Key insight: maybe we should count DISTINCT non-zero values in segments?")
print("For [1,0,1]: 2 segments but only 1 distinct value")
print("For [1,0,2,0,3]: 3 segments and 3 distinct values")

