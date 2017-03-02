# Starting from the vertex with the lexicographically smallest coordinates.
# Produces Convex-hull in Clockwise order
# Implements Andrew's monotone chain algorithm. O(n log n) complexity.
# Contract: [[int, int]] -> [[int, int]]
def convex_hull(points):

    # Uses quicksort built-in to sort the co-ordinates bottom upwards
    # REmoves duplicates automatically if any
    points = sorted(set(points))

    # Single Point Convex Hull
    if len(points) <= 1:
        return points

    # Now determine whether three points input form a clockwise turn (< 0)
    # Or a counter-clockwise turn (>  0)
    # Does so by invoking cross_product properties of vectors in Lexicographical space
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build lower hull 
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) >= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) >= 0:
            upper.pop()
        upper.append(p)

    # Concatenation of the lower and upper hulls gives the convex hull.
    # Last point of each list is omitted because it is repeated at the beginning of the other list. 
    return lower[:-1] + upper[:-1]


assert convex_hull([(i//10, i%10) for i in range(100)]) == [(0, 0), (0, 9), (9, 9), (9, 0)]