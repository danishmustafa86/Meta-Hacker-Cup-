def count_decodings(s):
    n = len(s)
    if n == 0 or (n == 1 and s[0] == '0'):
        return 0

    dp = [0] * (n + 1)
    dp[0] = 1  # There's one way to decode an empty string

    for i in range(1, n + 1):
        # Check the last single digit
        if s[i - 1] != '0':  # Not allowed to decode leading zero
            dp[i] += dp[i - 1]
        
        # Check the last two digits
        if i > 1:
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

    return dp[n]

def generate_uncorrupted_strings(encoded):
    if '?' not in encoded:
        return [encoded]  # No uncorrupted version needed

    results = []
    queue = [encoded]

    while queue:
        current = queue.pop(0)
        if '?' in current:
            index = current.index('?')
            for digit in '0123456789':
                # Avoid leading zero
                if index == 0 and digit == '0':
                    continue
                next_string = current[:index] + digit + current[index + 1:]
                queue.append(next_string)
        else:
            results.append(current)

    return results

def find_kth_largest_string(encoded, k):
    # Generate all uncorrupted strings
    uncorrupted_strings = generate_uncorrupted_strings(encoded)
    
    # Count decodings for each uncorrupted string
    max_count = 0
    valid_strings = []

    for us in uncorrupted_strings:
        count = count_decodings(us)
        if count > max_count:
            max_count = count
            valid_strings = [us]
        elif count == max_count:
            valid_strings.append(us)

    # Sort valid strings lexicographically
    valid_strings.sort()
    
    # Return the Kth largest string and the maximum count
    return valid_strings[k - 1], max_count % 998244353

def process_cases(test_cases):
    results = []
    for i, (encoded, k) in enumerate(test_cases, 1):
        kth_string, max_count = find_kth_largest_string(encoded, k)
        results.append(f"Case #{i}: {kth_string} {max_count}")
    return results

def main():
    output = []  # Initialize output here to avoid NameError in finally block
    # Read from input.txt and write to output.txt
    try:
        with open('input.txt', 'r') as fin:
            T = int(fin.readline().strip())
            test_cases = []
            
            for _ in range(T):
                line = fin.readline().strip().split()
                encoded = line[0]
                k = int(line[1])
                test_cases.append((encoded, k))
        
        # Process the test cases
        output = process_cases(test_cases)
        
        # Write output to file
        with open('output.txt', 'w') as fout:
            for line in output:
                fout.write(line + '\n')
        
        print("Output written to output.txt successfully.")
    
    except FileNotFoundError:
        print("Error: input.txt file not found.")
    except ValueError as ve:
        print(f"Error: Invalid input format. {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
