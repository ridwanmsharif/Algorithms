# Implementation of Pigeonhole/Counting sort
def pigeonhole_sort(a):
    
    my_min = min(a)
    my_max = max(a)
    size = my_max - my_min + 1

    # List of Pigeonholes
    holes = [0] * size

    # Populate the pigeonholes.
    for x in a:
        assert type(x) is int, "integers only please"
        holes[x - my_min] += 1

    # Put the elements back into the array in order.
    i = 0
    for count in xrange(size):
        while holes[count] > 0:
            holes[count] -= 1
            a[i] = count + my_min
            i += 1
