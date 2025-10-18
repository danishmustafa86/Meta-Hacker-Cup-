def calculate_cost_new(arr):
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
    
    # Check if array contains any zeros
    has_zeros = 0 in arr
    
    if has_zeros:
        # If there are zeros mixed in, use n-1
        return n - 1
    else:
        # If no zeros, count transitions between consecutive different values
        transitions = 0
        for i in range(n - 1):
            if arr[i] != arr[i + 1]:
                transitions += 1
        return max(1, transitions)

# Test all cases
test_cases = [
    ([0, 0], 0, "all zeros"),
    ([1, 1, 1], 8, "sample 2"),
    ([1, 2, 3], 9, "sample 3"),
    ([0, 1, 0, 2, 0, 3, 0], 72, "sample 4"),
    ([1, 0, 1], None, "edge case"),
    ([1073741823, 1073741823], None, "case 5"),
]

for arr, expected, desc in test_cases:
    total = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sub = arr[i:j+1]
            cost = calculate_cost_new(sub)
            total += cost
    
    if expected:
        print(f"{desc}: {total} (expected {expected}) {'PASS' if total == expected else 'FAIL'}")
    else:
        print(f"{desc}: {total}")

