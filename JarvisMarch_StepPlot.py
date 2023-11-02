
import sys
import numpy as np
import matplotlib.pyplot as plt

# Function to know if we have a CCW turn
def CCW(p1, p2, p3):
	if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
		return True
	return False


def JarvisMarch(Points):
	plt.figure()  # Define figure
	index = 0
	Points = list(Points)
	Points.sort(key = lambda x: x[1])	# Sort the set of points

	Points = np.array(Points)

	print("\nSorted List of Points: ")
	print(Points, end='\n\n')
	
	n = len(Points)
	FinalHull = [None] * n
	l = np.where(Points[:,1] == np.min(Points[:,1]))
	pointOnHull = Points[l[0][0]]
	i = 0
	while True:
		FinalHull[i] = pointOnHull
		endpoint = Points[0]
		for j in range(1,n):
			if (endpoint[0] == pointOnHull[0] and endpoint[1] == pointOnHull[1]) or not CCW(Points[j],FinalHull[i],endpoint):
				endpoint = Points[j]
		i = i + 1
		pointOnHull = endpoint
		J = np.array([FinalHull[k] for k in range(n) if FinalHull[k] is not None])
		plt.clf()               # Clear plot
		plt.title("Jarvis March")
		plt.plot(J[:,0],J[:,1], 'b-', picker=5)   # Plot lines
		plt.plot(Points[:,0],Points[:,1],".r")              # Plot points
		plt.axis('auto')         # No axis
		plt.show(block=False)   # Close plot
		plt.pause(0.1)    # Mini-pause before closing plot
		index += 1
		if endpoint[0] == FinalHull[0][0] and endpoint[1] == FinalHull[0][1]:
			break
	for i in range(n):
		if FinalHull[-1] is None:
			del FinalHull[-1]
	FinalHull = np.array(FinalHull)
	
	# Plot final hull
	# plt.clf()
	# plt.title("Jarvis March")
	# plt.plot(FinalHull[:,0],FinalHull[:,1], 'b-', picker=5)
	# plt.plot([FinalHull[-1,0],FinalHull[0,0]],[FinalHull[-1,1],FinalHull[0,1]], 'b-', picker=5)
	# plt.plot(Points[:,0],Points[:,1],".r")
	# plt.axis('auto')
	# plt.show()
	# plt.pause(0.1)
	return FinalHull

def main():
	try:
		N = int(sys.argv[1])
	except:
		N = int(input("Introduce N: "))
  
	# By default we build a random set of N points with coordinates in [0,300)x[0,300):
	Points = np.array([(np.random.randint(-300,300),np.random.randint(-300,300)) for i in range(N)])

	print("Generated Points: ")
	for p in Points:
		print(p)

	Final_Hull = JarvisMarch(Points)

	print("Points in the Hull:")
	print(Final_Hull)
	
	# We use the predefined figure
	plt.title("Jarvis March")
	plt.plot(Final_Hull[:,0],Final_Hull[:,1], 'b-', picker=5)
	plt.plot([Final_Hull[-1,0],Final_Hull[0,0]],[Final_Hull[-1,1],Final_Hull[0,1]], 'b-', picker=5)
	plt.plot(Points[:,0],Points[:,1],".r")
	plt.axis('auto')
	plt.show()

if __name__ == '__main__':
	main()
