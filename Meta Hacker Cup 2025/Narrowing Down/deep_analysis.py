def calculate_cost_simple(arr):
    """Simple rule: XOR=0 means cost = n-1"""
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
    return n - 1

def calculate_cost_complex(arr):
    """Complex rule with segments"""
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

# Test cases
test_cases = [
    ([0, 0], 0),
    ([1, 1, 1], 8),
    ([1, 2, 3], 9),
    ([0, 1, 0, 2, 0, 3, 0], 72),
]

print("Testing both algorithms:\n")
for arr, expected in test_cases:
    total_simple = 0
    total_complex = 0
    
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sub = arr[i:j+1]
            total_simple += calculate_cost_simple(sub)
            total_complex += calculate_cost_complex(sub)
    
    print(f"Array: {arr}")
    print(f"  Expected: {expected}")
    print(f"  Simple (n-1 for XOR=0): {total_simple} {'PASS' if total_simple == expected else 'FAIL'}")
    print(f"  Complex (segments): {total_complex} {'PASS' if total_complex == expected else 'FAIL'}")
    print()

# Now test specifically problematic subarrays from case 4
print("\nDetailed analysis of case 4 XOR=0 subarrays:")
arr = [0, 1, 0, 2, 0, 3, 0]
for i in range(len(arr)):
    for j in range(i, len(arr)):
        sub = arr[i:j+1]
        xor = 0
        for x in sub:
            xor ^= x
        if xor == 0 and not all(x == 0 for x in sub):
            simple = calculate_cost_simple(sub)
            complex = calculate_cost_complex(sub)
            non_zero = sum(1 for x in sub if x != 0)
            print(f"  {sub}: non_zero={non_zero}, simple={simple}, complex={complex}, diff={simple-complex}")

