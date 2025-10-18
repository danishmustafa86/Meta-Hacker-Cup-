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

# Case 5
print("Case 5: [1073741823, 1073741823]")
arr5 = [1073741823, 1073741823]
total = 0
for i in range(len(arr5)):
    for j in range(i, len(arr5)):
        sub = arr5[i:j+1]
        cost = calculate_cost(sub)
        print(f"  {sub}: cost={cost}")
        total += cost
print(f"Total: {total}\n")

# Check if there's something special about 1073741823
print(f"1073741823 in binary: {bin(1073741823)}")
print(f"1073741823 = 2^30 - 1 = {2**30 - 1}")
print(f"XOR of two identical numbers: {1073741823 ^ 1073741823}\n")

# Case 6 - partial analysis
print("Case 6: First 10 elements [1, 6, 12, 4, 0, 2, 4, 2, 1, 10]")
arr6_partial = [1, 6, 12, 4, 0, 2, 4, 2, 1, 10]
print(f"XOR of all: {sum(arr6_partial) % 2}")  # wrong, let me fix
xor_all = 0
for x in arr6_partial:
    xor_all ^= x
print(f"XOR of all elements: {xor_all}")

# Count some stats
print(f"Number of zeros: {arr6_partial.count(0)}")
print(f"Unique values: {len(set(arr6_partial))}")

