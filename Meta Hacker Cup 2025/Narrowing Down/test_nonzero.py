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
    
    # XOR = 0, count non-zero elements
    non_zero_count = sum(1 for x in arr if x != 0)
    return non_zero_count - 1 if non_zero_count > 0 else 0

# Test on all cases
print("Case 1: [0, 0]")
arr1 = [0, 0]
total = 0
for i in range(len(arr1)):
    for j in range(i, len(arr1)):
        sub = arr1[i:j+1]
        cost = calculate_cost(sub)
        total += cost
print(f"Total: {total}\n")

print("Case 2: [1, 1, 1]")
arr2 = [1, 1, 1]
total = 0
for i in range(len(arr2)):
    for j in range(i, len(arr2)):
        sub = arr2[i:j+1]
        cost = calculate_cost(sub)
        total += cost
print(f"Total: {total}\n")

print("Case 3: [1, 2, 3]")
arr3 = [1, 2, 3]
total = 0
for i in range(len(arr3)):
    for j in range(i, len(arr3)):
        sub = arr3[i:j+1]
        cost = calculate_cost(sub)
        total += cost
print(f"Total: {total}\n")

print("Case 4: [0, 1, 0, 2, 0, 3, 0]")
arr4 = [0, 1, 0, 2, 0, 3, 0]
total = 0
for i in range(len(arr4)):
    for j in range(i, len(arr4)):
        sub = arr4[i:j+1]
        cost = calculate_cost(sub)
        xor = 0
        for x in sub:
            xor ^= x
        if cost > 0 and xor == 0:
            non_zero = sum(1 for x in sub if x != 0)
            print(f"  {sub}: XOR=0, non_zero={non_zero}, cost={cost}")
        total += cost
print(f"Total: {total}")
print(f"Expected: 72\n")

