import time
import sys
import numpy as np
import matplotlib.pyplot as plt


def CCW(p1, p2, p3):
    if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
        return False
    
    return True



def BruteForce(Points):  # Main method which forms convex hull

    x_values = []
    y_values = []

    for i in range(0, len(Points)):
        for j in range(1, len(Points)):
            if j != i:
                above = 0
                below = 0
                for k in range(0, len(Points)):
                    if k != i and k != j:
                        
                        if CCW(np.array(Points[k]), np.array(Points[i]), np.array(Points[j])):
                            above = above + 1

                        else:
                            below = below + 1

                    if k == len(Points) - 1 and ((below == 0) or (above == 0)):
                        
                        x_values = [Points[i][0], Points[j][0]]
                        y_values = [Points[i][1], Points[j][1]]
                        plt.title("Brute Force")
                        plt.plot(x_values, y_values, '-r')
                        plt.show(block=False)
                        plt.pause(0.01)


def main():
    
    try:
        N = int(sys.argv[1])
    except:
        N = int(input("Introduce N: "))
        
    Points = [(np.random.randint(-1000,1000),np.random.randint(-1000,1000)) for i in range(N)]


    print("Generated Points: ")
    for p in Points:
        print(p)
        plt.plot(p[0], p[1], '.b')
    
    BruteForce(Points)
    

    plt.show()

if __name__ == '__main__':

    start = time.time()
    main()