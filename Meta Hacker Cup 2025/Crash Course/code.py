def solve(N, A, B):
    """
    Count sequences of 2N multipliers that:
    - Start from coolness 1
    - After N days: coolness <= A
    - After 2N days: coolness = B
    Result modulo 10^9 + 7
    """
    MOD = 10**9 + 7
    
    # Find all divisors of B that are <= A
    # These are valid intermediate values after N days
    divisors = []
    i = 1
    while i * i <= B:
        if B % i == 0:
            if i <= A:
                divisors.append(i)
            if i != B // i and B // i <= A:
                divisors.append(B // i)
        i += 1
    
    if not divisors:
        return 0
    
    # For each valid intermediate value, count ways to reach it in N steps
    # and ways to reach B from it in N steps
    
    def count_ways(start, end, steps):
        """Count ways to multiply from start to end in exactly steps operations"""
        if steps == 0:
            return 1 if start == end else 0
        
        if start > end:
            return 0
        
        if start == end:
            # Can only use multiplier 1
            return 1
        
        if end % start != 0:
            return 0
        
        target = end // start
        
        # Use DP: dp[s][val] = number of ways to reach val from 1 in s steps
        # We need to count factorizations of target into steps factors
        return count_factorizations(target, steps)
    
    def count_factorizations(n, k):
        """Count ordered factorizations of n into exactly k factors"""
        if k == 0:
            return 1 if n == 1 else 0
        if k == 1:
            return 1 if n >= 1 else 0
        if n == 1:
            return 1  # All factors must be 1
        
        # DP approach
        memo = {}
        
        def dp(num, remaining_steps):
            if remaining_steps == 0:
                return 1 if num == 1 else 0
            if num == 1:
                return 1
            
            if (num, remaining_steps) in memo:
                return memo[(num, remaining_steps)]
            
            result = 0
            # Try each divisor as the next factor
            i = 1
            while i * i <= num:
                if num % i == 0:
                    # Use divisor i
                    result = (result + dp(num // i, remaining_steps - 1)) % MOD
                    # Use divisor num//i (if different)
                    if i != num // i:
                        result = (result + dp(i, remaining_steps - 1)) % MOD
                i += 1
            
            memo[(num, remaining_steps)] = result
            return result
        
        return dp(n, k)
    
    total = 0
    for intermediate in divisors:
        # Count ways to go from 1 to intermediate in N steps
        ways1 = count_factorizations(intermediate, N)
        
        # Count ways to go from intermediate to B in N steps
        if B % intermediate == 0:
            ways2 = count_factorizations(B // intermediate, N)
            total = (total + ways1 * ways2) % MOD
    
    return total


def main():
    t = int(input())
    
    for case_num in range(1, t + 1):
        N, A, B = map(int, input().split())
        result = solve(N, A, B)
        print(f"Case #{case_num}: {result}")


if __name__ == "__main__":
    main()
