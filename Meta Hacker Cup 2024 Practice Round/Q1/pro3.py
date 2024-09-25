def solve(input_file, output_file):
    # Open input file to read and output file to write
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Read the number of test cases
        T = int(infile.readline().strip())
        
        # Process each test case
        for t in range(1, T + 1):
            # Read the values of N and K
            N, K = map(int, infile.readline().split())
            S = [int(infile.readline().strip()) for _ in range(N)]
            
            # Sort the times for optimal crossings
            S.sort()

            # Simulate the crossing strategy and calculate the total time
            total_time = 0
            if len(S) >= 2:
                total_time = 2 * (S[0] * (len(S) - 2)) + S[0]
            else:
                total_time = S[0]

            # Write the result for this test case to the output file
            if total_time <= K:
                outfile.write(f"Case #{t}: YES\n")
            else:
                outfile.write(f"Case #{t}: NO\n")

# Example usage: solve input from 'input.txt' and store result in 'output.txt'
solve('input.txt', 'output.txt')
