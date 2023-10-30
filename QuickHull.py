import sys
import numpy as np
from math import sqrt
from matplotlib import pyplot as plt

def findDistance(p1, p2, p3):
    """
    Find distance between a line p1-p2 and a plot p3

    :param: p1: the first coordinate on the line 
    :param: p2: the second coordinate on the line[1]
    :param: p3: point to measure the distance from

    :retrun: the distance between the line and the point
    """
    # using distance fomula: ax +by + c = 0
    a = p1[1] - p2[1]
    b = p2[0] - p1[0]
    c = p1[0]*p2[1] - p2[0]*p1[1]

    # using dot product to find the distacne between a line and a point


    return abs(a*p3[0] + b*p3[1] + c) / sqrt(a*a + b*b) 


def createSegment(p1, p2, v):
    """
    Segment a set of coordinates to be below a line p1 - p2

    :param p1:  first coordinate on the line
    :param p2: second coordinate on the line
    :param v: list of coordinates represened by the tuple (x,y)

    return: list of coordinates above and below the line
    """

    above = []
    below = []

    if p2[0] - p1[0] == 0:
        return above, below
    
    # m = (y2 - y1)/ (x2 - x1)
    m = (p2[1] - p1[1])/p2[0] - p1[0]
    # y = mx + c
    c = p1[1] - m*p1[0]
    # print("Length of v in findSegment(): ", len(v[0]), end='\n\n')
    # looping through each coordinate and placing it into correct list
    for coordinate in v:
        # y > mx + c : point is above the line
        # print("Length of coordinate in loop :", len(coordinate), end='\n\n')
        print(coordinate)
        if coordinate[1] > (m * coordinate[0]) + c:
            above.append(coordinate)

        # y < mx + c : point is below the line
        elif coordinate[1] < (m * coordinate[0]) + c:
            below.append(coordinate)
            
        else:
            continue

    return above, below


def CreateSemiHull(p1, p2, segment, flag):

    # exit case for recursion
    if segment == [] or p1 is None or p2 is None:
        return []
    
    convex_hull = []

    # calculate the distance of every point from the line to find the farthest point
    farthest_distance = 0
    farthest_point = 0

    for point in segment:
        distance = findDistance(p1, p2, point)
        
        if distance > farthest_distance:
            farthest_distance = distance
            farthest_point = point


    convex_hull = convex_hull + [farthest_point]

    # removing the point since its in the hull now
    # print('The segment: ', segment, end='\n\n')
    segment = np.delete(segment, np.where(segment == farthest_point))
    print('Type of segment: ', type(segment), end='\n\n')

    point1_above, point1_below = createSegment(p1, farthest_point, segment)
    point2_above, point2_below = createSegment(p2, farthest_point, segment)

    # we only need to use the segments formed in the same direction, opposite direction is contained in the hull

    if flag == "above":
        convex_hull = convex_hull + CreateSemiHull(p1, farthest_point, point1_above, "above")
        print('Convex HUll till now is: ', convex_hull, end='\n')
        convex_hull = convex_hull + CreateSemiHull(farthest_point, p2, point2_above, "above")
        print('Convex HUll till now is: ', convex_hull, end='\n')

    if flag == "below":
        convex_hull = convex_hull + CreateSemiHull(p1, farthest_point, point1_below, "below")
        print('Convex HUll till now is: ', convex_hull, end='\n')
        convex_hull = convex_hull + CreateSemiHull(farthest_point, p2, point2_below, "below")
        print('Convex HUll till now is: ', convex_hull, end='\n')

    return convex_hull

def QuickHull(v):
    """
    Calculate the convex hull of a set of vertives v such that
    :param v: set of coordinates (x,y) where x and y are floats

    :retrun : set of coordinates (x,y) that are the nodes of the convex hull
    """

    if(len(v) <= 2):
        return v
    
    convex_hull = []

    # find the maximum and minimum points on the x-axis
    v.sort(key = lambda x: x[0])
    # v = np.array(v)
    print(v)
    p1 = v[0]
    p2 = v[-1]

    convex_hull = convex_hull + [p1, p2]

    # remove initial two points from the list as they are part of the hull now
    np.delete(v, [0, -1])
    # np.delete(v,-1)
    del v[0]
    del v[-1]

    above, below = createSegment(p1, p2 ,v)
    convex_hull = convex_hull + CreateSemiHull(p1, p2, above, "above")
    convex_hull = convex_hull + CreateSemiHull(p1, p2, below, "below")

    return convex_hull

def main():

    try:
        N = int(sys.argv[1])
    except:
        N = int(input("Introduce N: "))

    
    Points = [(np.random.randint(-300,300),np.random.randint(-300,300)) for i in range(N)]
    # Points = list(Points)

    for p in Points:
        print(p)

    Final_Hull = QuickHull(Points)
    Final_Hull = [list(ele) for ele in Final_Hull]

    print('HULL VALUES: \n')
    for i in range(len(Final_Hull)):
        print(Final_Hull[i])

    plt.figure()
    plt.plot(Final_Hull[:,0],Final_Hull[:,1], 'b-', picker=8)
    plt.plot([Final_Hull[-1,0],Final_Hull[0,0]],[Final_Hull[-1,1],Final_Hull[0,1]], 'b-', picker=8)
    plt.plot(Points[:,0],Points[:,1],".r")
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    main()

