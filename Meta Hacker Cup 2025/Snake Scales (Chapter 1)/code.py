def solve():
    """
    Solution for Snake Scales (Chapter 1)

    """
    n = int(input())
    
    # Special case: only one platform, no ladder needed
    if n == 1:
        input()  # Read the platform height (not needed)
        return 0
    
    # Read platform heights
    heights = list(map(int, input().split()))
    
    # Find maximum difference between consecutive platforms
    max_diff = 0
    for i in range(n - 1):
        diff = abs(heights[i] - heights[i + 1])
        max_diff = max(max_diff, diff)
    
    return max_diff


def main():
    t = int(input())  # Number of test cases
    
    for case_num in range(1, t + 1):
        result = solve()
        print(f"Case #{case_num}: {result}")


if __name__ == "__main__":
    main()

