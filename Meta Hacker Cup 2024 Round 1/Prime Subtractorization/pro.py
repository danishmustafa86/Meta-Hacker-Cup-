def sieve_of_eratosthenes(n):
    """Generate a list of prime numbers up to n."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False
    return [i for i in range(2, n + 1) if primes[i]]

def count_subtractorizations(n):
    """Count the number of subtractorizations for a given n."""
    primes = sieve_of_eratosthenes(n * n)
    prime_set = set(primes)
    subtractorizations = set()

    for i, p1 in enumerate(primes):
        if p1 > n:
            break
        for j in range(i, len(primes)):
            p2 = primes[j]
            if p2 > n:
                break
            diff = abs(p2 - p1)
            if diff in prime_set:
                subtractorizations.add(diff)

    return len(subtractorizations)

def main():
    try:
        # Read input from input.txt
        with open('input.txt', 'r') as f:
            t = int(f.readline().strip())

        # Process each test case
        with open('output.txt', 'a') as f_out:  # Open output file in append mode
            for case in range(1, t + 1):
                n = int(f.readline().strip())
                result = count_subtractorizations(n)
                f_out.write(f"Case #{case}: {result}\n")

        print("Output written to output.txt")
    except FileNotFoundError:
        print("Error: The input file 'input.txt' was not found.")
    except ValueError as e:
        print(f"Error: Invalid input format. {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()