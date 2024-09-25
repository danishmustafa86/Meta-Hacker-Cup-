T = int(input())
for t in range(1, T + 1):
    N, P = map(int, input().split())
    
    # Calculate the new required probability
    P_new = (P / 100) ** ((N - 1) / N)
    
    # Convert back to percentage
    P_new_percentage = P_new * 100
    
    # Calculate the increase
    increase = P_new_percentage - P
    
    # Print the result for the test case
    print(f"Case #{t}: {increase:.15f}")
