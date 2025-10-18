def calculate_cost(arr):
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

# Test specific patterns
patterns = [
    [1, 2],  # Simple pair, XOR=3
    [1, 1, 2, 2],  # Two pairs, XOR=0
    [1, 2, 2, 1],  # Symmetric, XOR=0
    [1, 2, 3],  # Three different, XOR=0
    [0, 1, 1],  # Leading zero with pair
    [1, 1, 0],  # Trailing zero with pair
]

for arr in patterns:
    xor = 0
    for x in arr:
        xor ^= x
    cost = calculate_cost(arr)
    print(f"{arr}: XOR={xor}, cost={cost}")

print("\nManual verification for [1,1,2,2]:")
print("  Operations: [1,1,2,2] -> i=1,x=1 -> [0,0,2,2] -> i=3,x=2 -> [0,0,0,0]")
print("  Expected: 2 operations")
print(f"  My algorithm: {calculate_cost([1,1,2,2])}")
print(f"  (transitions=1 for 1->2, segments=1, so max(1,1)=1)")
print()

print("Manual verification for [1,2,2,1]:")
print("  XOR = 0, can we flatten?")
print("  [1,2,2,1] -> i=2,x=3 -> [1,2,1,2] -> ???")
print(f"  My algorithm: {calculate_cost([1,2,2,1])}")

