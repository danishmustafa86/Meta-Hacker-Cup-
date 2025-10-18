import sys
sys.setrecursionlimit(1000000)

def solve():
    """
    Solution for Snake Scales (Chapter 2)
    
    This is a graph connectivity problem. We need minimum ladder height h such that
    all platforms are reachable from ground using edges with weight h.
    
    I've Used Union-Find with sorted edges (Kruskal-like algorithm)
    """
    n = int(input())
    
    if n == 1:
        height = int(input())
        return height  # Just need to reach the single platform from ground
    
    heights = list(map(int, input().split()))


    edges = []
    
    # Edges from ground to each platform
    for i in range(n):
        edges.append((heights[i], 0, i + 1))
    
    # Edges between consecutive platforms
    for i in range(n - 1):
        weight = abs(heights[i] - heights[i + 1])
        edges.append((weight, i + 1, i + 2))
    
    # Sort edges by weight
    edges.sort()
    
    # Union-Find data structure with size tracking
    parent = list(range(n + 1))
    size = [1] * (n + 1)  # Track component sizes
    
    def find(x):
        # Iterative find with path compression
        root = x
        while parent[root] != root:
            root = parent[root]
        # Path compression
        while parent[x] != root:
            next_x = parent[x]
            parent[x] = root
            x = next_x
        return root
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            size[py] += size[px]
            return True
        return False
    
    # Add edges until all platforms are connected to ground
    answer = 0
    
    for weight, u, v in edges:
        if union(u, v):
            answer = weight
            
            # Check if all platforms are now connected to ground
            # Ground is node 0, and size includes ground itself
            if size[find(0)] == n + 1:
                return answer
    
    return answer


def main():
    t = int(input())
    
    for case_num in range(1, t + 1):
        result = solve()
        print(f"Case #{case_num}: {result}")


if __name__ == "__main__":
    main()

