# function that finds the distance between two points
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# function that finds the closest pair of points from a multidimensional
# list of points
def nearestPoints(points):
    # initialize indicies of nearest points
    p1, p2 = 0, 1
    #initialize shortest distance
    shortestDistance = distance(points[p1][0], points[p1][1],
                            points[p2][0], points[p2][1])
    # nested for loop to check all possible pairings
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            d = distance(points[i][0], points[i][1], points[i+1][0], points[i+1][1])
            if d < shortestDistance:
                shortestDistance = d # update shortest distance
                p1, p2 = i, j # update indicies of closest points

    return p1, p2
