import sys
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

def CCW(p1, p2, p3):
    # return true if p3 is in the leftside of line p1p2
    # else return false
    if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
        return False
    
    return True

def find_distance(p1, p2, p3):
    #return the distance from point p3 to line p1p2
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    numerator = abs((y2-y1)*x3 - (x2-x1)*y3 + x2*y1 - y2*x1)
    denominator = ((y2-y1)*(y2-y1) + (x2-x1)*(x2-x1))

    ans = numerator / sqrt(denominator)
    return ans

def find_max_distance(p1, p2, Points):
    # return a point from listPts who has most distance from line p1p2
    max_dist = float(0)
    ans = []
    for point in Points:
        dist = find_distance(p1, p2, point)
        if dist > max_dist and point != p1 and point != p2:
            max_dist = dist
            ans = point
    return ans

def QuickHull (min, max, Points, direction):
    # return the points that make the convex hull for listPts
    LeftHull = []
    RightHull = []
    HullPoints = []

    for point in Points:
        if CCW(min, max, point) and direction != 1:
            LeftHull.append(point)
        elif CCW(max, min, point) and direction != 0:
            RightHull.append(point)

    
    checked = False
    if direction != 1:
        leftMostPts = find_max_distance(min, max, LeftHull)
        #print(direction,leftMostPts)
        if len(leftMostPts) > 0:
            HullPoints = HullPoints + QuickHull(min, leftMostPts, LeftHull, 0)
            HullPoints = HullPoints + QuickHull(leftMostPts, max, LeftHull, 0)
        else:
            checked = True
            HullPoints.append(max)
    if direction != 0:
        rigthMostPts = find_max_distance(min, max, RightHull)
        #print(direction,rigthMostPts)
        if len(rigthMostPts) > 0:
            HullPoints = HullPoints + QuickHull(rigthMostPts, max, RightHull, 1)
            HullPoints = HullPoints + QuickHull(min, rigthMostPts, RightHull, 1)
        elif not checked:
            HullPoints.append(max)

    return HullPoints




def main():
    try:
        N = int(sys.argv[1])
    except:
        N = int(input("Introduce N: "))
        
    Points = [(np.random.randint(-1000,1000),np.random.randint(-1000,1000)) for i in range(N)]

    FinalHull = QuickHull(Points[0], Points[N-1], Points, 10)

    if not(Points[0] in FinalHull):
        FinalHull = [Points[0]] + FinalHull
    if not(Points[N-1] in FinalHull):
        FinalHull.append(Points[N-1])

    # x and y will be used for visual plotting
    x = [i[0] for i in FinalHull]
    y = [i[1] for i in FinalHull]

    x.append(x[0])
    y.append(y[0])

    print('Generated Points :')
    print(Points)
    print('Points On Convex Hull :')
    print(FinalHull)

    # Plotting
    plt.figure(facecolor='#4e4e4e')
    axes = plt.axes()
    axes.set_facecolor('#6f6f6f')
    plt.title("Quick Hull")
    for i in Points:
        plt.plot(i[0],i[1],'.w')

    plt.plot(x,y, '-r')
    plt.show()

if __name__ == '__main__':
    main()