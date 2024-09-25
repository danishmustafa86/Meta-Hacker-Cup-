from math import gcd

T = int(input("Enter number of test cases: "))

for t in range(1, T + 1):
    N = int(input())
    points = []

    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    max_collinear = 1

    for i in range(N):
        slope_count = {}

        for j in range(N):
            if i != j:
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx == 0 and dy == 0:  # Skip the same point
                    continue

                # Handle vertical and horizontal lines
                if dx == 0:  # vertical line
                    slope = (1, 0)
                elif dy == 0:  # horizontal line
                    slope = (0, 1)
                else:
                    g = gcd(dy, dx)  # Calculate gcd of dy and dx
                    slope = (dy // g, dx // g)  # Reduce slope by gcd

                if slope in slope_count:
                    slope_count[slope] += 1
                else:
                    slope_count[slope] = 1

        if slope_count:
            max_collinear = max(max_collinear, max(slope_count.values()) + 1)

    moves = N - max_collinear
    print(f"Case #{t}: {moves}")







    
