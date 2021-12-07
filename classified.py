# classified.py

#calculate the avg distance
def calculateDistance(templ_corner, subimg_corner):
	#tuple up the corners to ensure same amount of points
	getTuple = zip(templ_corner, subimg_corner)
	#initialize variable 
	totalDistance = 0
	count = 0
	
	#extract each pixel location to calculateDistance
	for pts in getTuple:
		x1 = pts[0][0][0]	#templ's x
		x2 = pts[1][0][0]	#subimg's x
		y1 = pts[0][0][1]	#templ's y
		y2 = pts[1][0][1]	#subimg's y
		#using the euclidean distance formula
		distance = ((x1-x2)**2+(y1-y2)**2)**0.5
		#accumulate the distance value
		totalDistance = totalDistance + distance
		#accumulate the number of point
		count = count + 1
	
	#calculate the avg distabce
	avgDistance = totalDistance/count
	#return the avg distance
	return avgDistance

#calculate the meanshift	
def meanShift(d0, d1, d2, d3):
	#sort the distance in an array
	d = [d0,d1,d2,d3]
	d.sort()
	
	#calculate the gradient 
	gradient1 = abs(d[0]-d[1])/2
	gradient2 = abs(d[0]-d[1])/2 + abs(d[1]-d[2])/2
	gradient3 = abs(d[1]-d[2])/2 + abs(d[2]-d[3])/2
	gradient4 = abs(d[2]-d[3])/2
	
	#the maximum value of the gradient is the threshold
	threshold = max(gradient1, gradient2, gradient3, gradient4)
	
	#display the gradient
	print("ImageB: gradient1 = ", gradient1)
	print("ImageC: gradient2 = ", gradient2)
	print("ImageD: gradient3 = ", gradient3)
	print("ImageE: gradient4 = ", gradient4)
	print("Mean Shift threshold = ", threshold)
	#return the threshold value
	return threshold