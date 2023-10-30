from random import randint
import matplotlib.pyplot as plt

def is_Leftside(p1, p2, p3):
    # return true if p3 is in the leftside of line p1p2
    # else return false
    determinan = p1[0]*p2[1] + p3[0]*p1[1] + p2[0]*p3[1] - p3[0]*p2[1] - p2[0]*p1[1] - p1[0]*p3[1];
    return determinan > 0

def quickHull (mins, maks, listPts, direction):
    # return the points that make the convex hull for listPts
    leftPts = []
    rigthPts = []
    hullPts = []
    for point in listPts:
        if is_Leftside(mins, maks, point) and direction != 1:
            leftPts.append(point)
        elif is_Leftside(maks, mins, point) and direction != 0:
            rigthPts.append(point)
    #print(mins,maks)
    #print('left',leftPts)
    #print('rigth',rigthPts)
    sudah = False
    if direction != 1:
        leftMostPts = most_DistancePts(mins, maks, leftPts)
        #print(direction,leftMostPts)
        if len(leftMostPts) > 0:
            hullPts = hullPts + quickHull(mins, leftMostPts, leftPts, 0)
            hullPts = hullPts + quickHull(leftMostPts, maks, leftPts, 0)
        else:
            sudah = True
            hullPts.append(maks)
    if direction != 0:
        rigthMostPts = most_DistancePts(mins, maks, rigthPts)
        #print(direction,rigthMostPts)
        if len(rigthMostPts) > 0:
            hullPts = hullPts + quickHull(rigthMostPts, maks, rigthPts, 1)
            hullPts = hullPts + quickHull(mins, rigthMostPts, rigthPts, 1)
        elif not(sudah):
            hullPts.append(maks)
    return hullPts

def most_DistancePts(p1, p2, listPts):
    # return a point from listPts who has most distance from line p1p2
    max_dist = float(0)
    ans = []
    for point in listPts:
        dist = distancePts(p1, p2, point)
        if dist > max_dist and point != p1 and point != p2:
            max_dist = dist
            ans = point
    return ans

def distancePts(p1, p2, p3):
    #return the distance from point p3 to line p1p2
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    pembilang = abs((y2-y1)*x3 - (x2-x1)*y3 + x2*y1 - y2*x1)
    penyebut = ((y2-y1)*(y2-y1) + (x2-x1)*(x2-x1)) ** 0.5
    ans = pembilang / penyebut
    return ans


def main():
    n = int(input("Enter N: "))

    listPts = sorted([(randint(0,100), randint(0,100)) for i in range(n)])

    result = quickHull(listPts[0], listPts[n-1], listPts, 10)

    if not(listPts[0] in result):
        result = [listPts[0]] + result
    if not(listPts[n-1] in result):
        result.append(listPts[n-1])

    # x and y will be used for visual plotting
    x = [i[0] for i in result]
    y = [i[1] for i in result]
    x.append(x[0])
    y.append(y[0])
    print('List of point :',listPts)
    print('Points that make convexhull :',result)
    for i in listPts:
        plt.scatter(i[0],i[1], label = 'skitscat', color = 'r')

    plt.plot(x,y)
    plt.show()

if __name__ == '__main__':
    main()