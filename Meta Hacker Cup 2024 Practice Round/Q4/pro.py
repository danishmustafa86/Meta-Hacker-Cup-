def solve(input_file: str, output_file: str):
    # Open the input file for reading
    with open(input_file, 'r') as f:
        data = f.read().splitlines()  # Read the entire file and split it into lines
    
    idx = 0
    T = int(data[idx])  # Number of test cases
    idx += 1
    results = []
    
    for t in range(1, T + 1):
        # Read N (number of stones) and G (goal position)
        N, G = map(int, data[idx].split())
        idx += 1
        
        energies = []
        for _ in range(N):
            energies.append(int(data[idx]))  # Energies of stones
            idx += 1
        
        # To store the final positions of stones after resolving collisions
        final_positions = [-1] * N
        
        for i in range(N):
            pos = energies[i]
            # Check for collisions: if the position is already taken, reduce position
            while pos in final_positions:
                pos -= 1  # Collision detected, reduce position
            final_positions[i] = pos
        
        # Find the stone closest to G
        closest_index = -1
        closest_distance = float('inf')
        
        for i in range(N):
            distance = abs(final_positions[i] - G)
            if distance < closest_distance or (distance == closest_distance and i < closest_index):
                closest_index = i
                closest_distance = distance
        
        # Append the result for this test case
        results.append(f"Case #{t}: {closest_index + 1} {closest_distance}")
    
    # Write the results to the output file
    with open(output_file, 'w') as f:
        f.write("\n".join(results) + "\n")


solve("input.txt", "output.txt")