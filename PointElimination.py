import sys
import random
import numpy as np
from matplotlib import pyplot as plt

def initPoints(n):
    Points = []
    for i in range(0, n):  # Plots points on table
        Points.append([random.randint(1, 100), random.randint(1, 100)])  # Change bounds to increase or decrease
        # (x,y) acceptable range
        plt.plot(Points[i][0], Points[i][1], '.r')
        
        

    return Points

def PointElimination(Points):
    """
    FIRST STEP:
    1. Vertically lowest (bottom-most) point
    2. Vertically highest (top-most) point
    3. Leftmost point
    4. Rightmost point
    
    SECOND STEP:
    Using these 4 points creat a quadrilateral

    THIRD STEP:
    # Now remove those points from the that are inside the quadrilateral


    """ 
    # IMPLMENTING FIRST STEP
    
    x_sortedPoints = sorted(Points, key = lambda x: x[0])
    y_sortedPoints = sorted(Points, key = lambda x: x[1])

    print(x_sortedPoints)
    print(y_sortedPoints)

    left_most = np.array(x_sortedPoints[0])
    right_most = np.array(x_sortedPoints[-1])
    lowest = np.array(y_sortedPoints[0]) #bottom most element
    highest = np.array(y_sortedPoints[-1]) #top most element


    print(left_most)
    print(right_most)
    print(lowest)
    print(highest)


def main():

    try:
        N = int(sys.argv[1])
    except:
        N = int(input("Introduce N: "))
  
    Points = initPoints(N)

    PointElimination(Points)
    plt.show()
    # start = time.time()


if __name__ == '__main__':
    main()
