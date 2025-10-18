MOD = 10**9 + 7

def get_prime_factors(n):
    """Get prime factorization as list of (prime, exponent)"""
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def get_divisors(n):
    """Get all divisors of n"""
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    return sorted(divisors)

def mod_inverse(a, mod):
    """Compute modular inverse using Fermat's little theorem"""
    return pow(a, mod - 2, mod)

def comb_mod(n, k, mod):
    """Compute C(n,k) mod using factorial and modular inverse"""
    if k > n or k < 0:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator = (numerator * (n - i)) % mod
        denominator = (denominator * (i + 1)) % mod
    
    return (numerator * mod_inverse(denominator, mod)) % mod

def stars_and_bars(exponent, positions, mod):
    """
    Distribute 'exponent' items into 'positions' bins
    Answer: C(exponent + positions - 1, exponent)
    """
    return comb_mod(exponent + positions - 1, exponent, mod)

def solve_part2(N, A, B):
    """Count valid sequences of 2N multipliers"""
    
    # Get all divisors of B that are <= A
    # These are possible products for first N days
    divisors = get_divisors(B)
    valid_divisors = [d for d in divisors if d <= A]
    
    total_count = 0
    
    # For each valid divisor d (product of first N days)
    for d in valid_divisors:
        remainder = B // d  # Product needed in second N days
        
        # Get prime factorizations
        d_factors = get_prime_factors(d)
        remainder_factors = get_prime_factors(remainder)
        
        # Count ways to distribute d across first N days
        ways_first = 1
        for exponent in d_factors.values():
            ways_first = (ways_first * stars_and_bars(exponent, N, MOD)) % MOD
        
        # Count ways to distribute remainder across second N days
        ways_second = 1
        for exponent in remainder_factors.values():
            ways_second = (ways_second * stars_and_bars(exponent, N, MOD)) % MOD
        
        # Add to total
        total_count = (total_count + ways_first * ways_second) % MOD
    
    return total_count

# Read from input.txt
with open('input.txt', 'r') as infile:
    lines = infile.readlines()

results = []
T = int(lines[0].strip())
line_idx = 1

for case_num in range(1, T + 1):
    N, A, B = map(int, lines[line_idx].strip().split())
    line_idx += 1
    
    count = solve_part2(N, A, B)
    result = f"Case #{case_num}: {count}"
    results.append(result)

# Write to output.txt
with open('output.txt', 'w') as outfile:
    for result in results:
        outfile.write(result + '\n')