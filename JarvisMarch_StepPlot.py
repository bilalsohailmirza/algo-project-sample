
import sys
import numpy as np
import matplotlib.pyplot as plt

# Function to know if we have a CCW turn
def CCW(p1, p2, p3):
	if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
		return True
	return False


def JarvisMarch(S):
	plt.figure()  # Define figure
	index = 0
	S = list(S)
	S.sort(key = lambda x: x[1])	# Sort the set of points

	S = np.array(S)

	print("\nSorted List of Points: ")
	print(S, end='\n\n')
	n = len(S)
	P = [None] * n
	l = np.where(S[:,1] == np.min(S[:,1]))
	pointOnHull = S[l[0][0]]
	i = 0
	while True:
		P[i] = pointOnHull
		endpoint = S[0]
		for j in range(1,n):
			if (endpoint[0] == pointOnHull[0] and endpoint[1] == pointOnHull[1]) or not CCW(S[j],P[i],endpoint):
				endpoint = S[j]
		i = i + 1
		pointOnHull = endpoint
		J = np.array([P[k] for k in range(n) if P[k] is not None])
		plt.clf()               # Clear plot
		plt.plot(J[:,0],J[:,1], 'b-', picker=5)   # Plot lines
		plt.plot(S[:,0],S[:,1],".r")              # Plot points
		plt.axis('off')         # No axis
		plt.show(block=False)   # Close plot
		plt.pause(0.1)    # Mini-pause before closing plot
		index += 1
		if endpoint[0] == P[0][0] and endpoint[1] == P[0][1]:
			break
	for i in range(n):
		if P[-1] is None:
			del P[-1]
	P = np.array(P)
	
	# Plot final hull
	plt.clf()
	plt.plot(P[:,0],P[:,1], 'b-', picker=5)
	plt.plot([P[-1,0],P[0,0]],[P[-1,1],P[0,1]], 'b-', picker=5)
	plt.plot(S[:,0],S[:,1],".r")
	plt.axis('off')
	plt.show(block=False)
	plt.pause(0.1)
	return P

def main():
	try:
		N = int(sys.argv[1])
	except:
		N = int(input("Introduce N: "))
  
	# By default we build a random set of N points with coordinates in [0,300)x[0,300):
	Points = np.array([(np.random.randint(-300,300),np.random.randint(-300,300)) for i in range(N)])
	for p in Points:
		print(p)

	Final_Hull = JarvisMarch(Points)

	print(Final_Hull)
	print(Final_Hull[:,1])
	
	# We use the predefined figure
	plt.plot(Final_Hull[:,0],Final_Hull[:,1], 'b-', picker=5)
	plt.plot([Final_Hull[-1,0],Final_Hull[0,0]],[Final_Hull[-1,1],Final_Hull[0,1]], 'b-', picker=5)
	plt.plot(Points[:,0],Points[:,1],".r")
	plt.axis('off')
	plt.show()

if __name__ == '__main__':
	main()
