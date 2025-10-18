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
    
    return n - 1

# Case 4: [0, 1, 0, 2, 0, 3, 0]
arr = [0, 1, 0, 2, 0, 3, 0]
print("Case 4: [0, 1, 0, 2, 0, 3, 0]")
total = 0
for i in range(7):
    for j in range(i, 7):
        sub = arr[i:j+1]
        cost = calculate_cost(sub)
        xor = 0
        for x in sub:
            xor ^= x
        if cost > 0:
            print(f"  [{i}:{j+1}] {sub}: XOR={xor}, cost={cost}")
        total += cost

print(f"\nTotal: {total}")
print(f"Expected: 72")

