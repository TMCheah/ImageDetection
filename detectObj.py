# detectObj.py

import cv2 as cv
import numpy as np
import classified as classify

#function to detect object's corner
def cornerDetection(cropImg, oriImg, pt):
	# grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cropImg = np.float32(cropImg)
	corners = cv.goodFeaturesToTrack(cropImg, 100, 0.01, 10)
	corners = np.int0(corners)	#cast to int32 or int64

	#plot a dots on every corner detected
	for corner in corners:
		x, y = corner.ravel()
		cv.circle(oriImg, (x+pt[0], y+pt[1]), 3, 255, -1)
	
	#return all the corner points
	return corners

#read in sub images
imgB = cv.imread('ImageB.jpg')
imgC = cv.imread('ImageC.jpg')
imgD = cv.imread('ImageD.jpg')
imgE = cv.imread('ImageE.jpg')

#read in template in greyscale
templateDetection = cv.imread('template.jpg', 0)
template = cv.imread('template.jpg', 0)
#convern sub image to grayscale
grey1 = cv.cvtColor(imgB, cv.COLOR_BGR2GRAY)
grey2 = cv.cvtColor(imgC, cv.COLOR_BGR2GRAY)
grey3 = cv.cvtColor(imgD, cv.COLOR_BGR2GRAY)
grey4 = cv.cvtColor(imgE, cv.COLOR_BGR2GRAY)

#get the corner point of the template object
template_corner = cornerDetection(templateDetection, templateDetection, ([0,0]))

#declare and initialize the template's shape
h,w = template.shape[::-1]

#get the return value from the matchTemplate 
#the closer the similarity in the image, the higher the value
res1 = cv.matchTemplate(grey1, template, cv.TM_CCOEFF_NORMED)
res2 = cv.matchTemplate(grey2, template, cv.TM_CCOEFF_NORMED)
res3 = cv.matchTemplate(grey3, template, cv.TM_CCOEFF_NORMED)
res4 = cv.matchTemplate(grey4, template, cv.TM_CCOEFF_NORMED)

#set threshold value for ImageB
threshold = 0.74
#filter and get the pixel location if the calue of res1 is more or equal than the threshold
loc1 = np.where(res1 >= threshold) #loc is the list of points that are matched in template3.jpg image.

#setThreshold value for ImageC
threshold = 0.98
#filter and get the pixel location if the calue of res2 is more or equal than the threshold
loc2 = np.where(res2 >= threshold) #loc is the list of points that are matched in template3.jpg image.

#setThreshold value for ImageD
threshold = 0.5
#filter and get the pixel location if the calue of res3 is more or equal than the threshold
loc3 = np.where(res3 >= threshold) #loc is the list of points that are matched in template3.jpg image.

#setThreshold value for ImageE
threshold = 0.5
#filter and get the pixel location if the calue of res4 is more or equal than the threshold
loc4 = np.where(res4 >= threshold) #loc is the list of points that are matched in template3.jpg image.

#if loc1 is not empty
if loc1[0].size != 0:
	#extract the point location
	for pt in zip(*loc1[::-1]):
		#draw a rectangle around the object
		cv.rectangle(imgB, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)

	#crop the original image 
	cropImageB = np.zeros([w, h])
	cropImageB = grey1[pt[1]:pt[1]+h, pt[0]:pt[0]+w]
	#pass the cropped image, original image and the points for corder detection
	imgB_corner = cornerDetection(cropImageB, imgB, pt)
#if loc1 is empty
else:
	imgB_corner = cornerDetection(grey1, imgB, ([0,0]))

#if loc2 is not empty
if loc2[0].size != 0:
	#extract the point location
	for pt in zip(*loc2[::-1]):
		#draw a rectangle around the object
		cv.rectangle(imgC, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)
	
	#crop the original image 	
	cropImageC = np.zeros([w, h])
	cropImageC = grey2[pt[1]:pt[1]+h, pt[0]:pt[0]+w]
	#pass the cropped image, original image and the points for corder detection
	imgC_corner = cornerDetection(cropImageC, imgC, pt)
#if loc2 is empty
else:
	imgC_corner = cornerDetection(grey2, imgC, ([0,0]))
	
#if loc3 is not empty	
if loc3[0].size != 0:
	#extract the point location
	for pt in zip(*loc3[::-1]):
		#draw a rectangle around the object
		cv.rectangle(imgD, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)
		
	#crop the original image 
	cropImageD = np.zeros([w, h])
	cropImageD = grey3[pt[1]:pt[1]+h, pt[0]:pt[0]+w]
	#pass the cropped image, original image and the points for corder detection
	imgD_corner = cornerDetection(cropImageD, imgD, pt)
#if loc3 is empty
else:
	imgD_corner = cornerDetection(grey3, imgD, ([0,0]))

#if loc4 is not empty
if loc4[0].size != 0:
	#extract the point location
	for pt in zip(*loc4[::-1]):
		#draw a rectangle around the object
		cv.rectangle(imgE, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)
		
	#crop the original image 
	cropImageE = np.zeros([w, h])
	cropImageE = grey4[pt[1]:pt[1]+h, pt[0]:pt[0]+w]
	#pass the cropped image, original image and the points for corder detection
	imgE_corner = cornerDetection(cropImageE, imgE, pt)
#if loc4 is empty
else:
	imgE_corner = cornerDetection(grey4, imgE, ([0,0]))


#display all image
cv.imshow('ImageA', templateDetection)
cv.imshow('ImageB',imgB)
cv.imshow('ImageC',imgC)
cv.imshow('ImageD',imgD)
cv.imshow('ImageE',imgE)

#calculate the avg distance between template's corner and sub images' corner
#d1 = ImageA to ImageB
d1 = classify.calculateDistance(template_corner, imgB_corner)
#d2 = ImageA to ImageC
d2 = classify.calculateDistance(template_corner, imgC_corner)
#d3 = ImageA to ImageD
d3 = classify.calculateDistance(template_corner, imgD_corner)
#d4 = ImageA to ImageE
d4 = classify.calculateDistance(template_corner, imgE_corner)

#display the distance
print("d1 = ", d1)
print("d2 = ", d2)
print("d3 = ", d3)
print("d4 = ", d4)

#calcuate the mean shift, then use the avg distance and threshold value to determine if object found. 
MeanShiftThreshold = classify.meanShift(d1,d2,d3,d4)
print("ImageB: ", "Object found" if d1 < MeanShiftThreshold else "Object not found")
print("ImageC: ", "Object found" if d2 < MeanShiftThreshold else "Object not found")
print("ImageD: ", "Object found" if d3 < MeanShiftThreshold else "Object not found")
print("ImageE: ", "Object found" if d4 < MeanShiftThreshold else "Object not found")


cv.waitKey(0)
cv.destroyAllWindows()