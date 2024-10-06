def find_min_speed(T, test_cases):
    results = []
    
    for case_num in range(T):
        N = test_cases[case_num][0]  # Number of stations
        stations = test_cases[case_num][1]  # A list of tuples (Ai, Bi) for each station
        
        # Initialize bounds for valid speed range
        lower_bound = 0  # Slowest speed allowed
        upper_bound = float('inf')  # Fastest speed allowed
        
        for i in range(1, N + 1):
            Ai, Bi = stations[i - 1]
            
            if Bi == 0:
                continue  # Skip station if time window is invalid (Bi == 0)
            
            # Update lower and upper bounds for this station
            lower_bound = max(lower_bound, i / Bi)  # Sonic must be at least this fast to reach in time
            
            if Ai > 0:  # Avoid division by zero for arrival time check
                upper_bound = min(upper_bound, i / Ai)  # Sonic must be no faster than this to avoid arriving early
            
            # If the bounds cross, it's impossible to satisfy the conditions
            if lower_bound > upper_bound:
                results.append(f"Case #{case_num + 1}: -1")
                break
        else:
            # If we didn't break, we found a valid speed range
            results.append(f"Case #{case_num + 1}: {lower_bound:.6f}")
    
    return results


def read_input(file_name):
    with open(file_name, 'r') as file:
        T = int(file.readline().strip())  # Read number of test cases
        test_cases = []
        for _ in range(T):
            N = int(file.readline().strip())  # Number of stations
            stations = [tuple(map(int, file.readline().strip().split())) for _ in range(N)]
            test_cases.append((N, stations))
    return T, test_cases


def write_output(file_name, results):
    with open(file_name, 'w') as file:
        for result in results:
            file.write(result + '\n')


if __name__ == "__main__":
    # Read from input.txt
    T, test_cases = read_input('input.txt')
    
    # Run the function
    results = find_min_speed(T, test_cases)

    # Write results to output.txt
    write_output('output.txt', results)
