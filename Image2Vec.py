import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import pytesseract
import subprocess


def equal(c1, c2):
	if abs(c1-c2) < 4:
		return True
	return False

def compare(coordinate_one, coordinate_two):
	#returns 1 if c1 is big.
	if equal(coordinate_one[1], coordinate_two[1]):
		return coordinate_one[0] > coordinate_two[0]
	else :
		return coordinate_one[1] > coordinate_two[1]
		

def sort_contour(coordinates):
	for i in xrange(len(coordinates)):
		for j in xrange(i+1, len(coordinates)):
			if(compare(coordinates[i], coordinates[j])):
				coordinates[i],coordinates[j]=coordinates[j],coordinates[i]
	return coordinates

def find_squares(img):
	squares = []
	coordinates = []
	(cnts, _) = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:20]
	for c in cnts:
	# approximate the contour

		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.1 * peri, True)
		
	# if our approximated contour has four points, then
	# we can assume that we have found our screen
		if len(approx) == 4:

			M = cv2.moments(approx)
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			# print cx, cy
			if(cy<600):
				# cv2.drawContours(image, [approx], -1, (0, 255, 0), 3)
				# cv2.imshow("Game Boy Screen", image)
				# cv2.waitKey(-1)
				squares.append(approx)
				coordinates.append([cx, cy])


	# print coordinates, sort_contour(coordinates)
	sorted_coordinates = sort_contour(coordinates)
	return sorted_coordinates
	# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]

def vector_gen(image):
	image = cv2.imread(image)
	image = cv2.resize(image, (449, 779))

	# print image.shape[:2]
	vector = []
	boundary = [([40, 20, 0], [240, 160, 20])]
	# plt.imshow(image)
	# plt.show()
	for (lower, upper) in boundary:
		# create NumPy arrays from the boundaries
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
		# find the colors within the specified boundaries and apply# the mask
		mask = cv2.inRange(image, lower, upper)
		output = cv2.bitwise_and(image, image, mask = mask)
	 	
	 	inverted = cv2.bitwise_not ( mask );
	 	sorted_coordinates = find_squares(inverted)
	 	width= 30

	 	for coordinate in sorted_coordinates:
			crop_img = image[coordinate[1]-width: coordinate[1]+width, coordinate[0]-width:coordinate[0]+width] # Crop from x, y, w, h -> 100, 200, 300, 400
			# cv2.imshow("c", crop_img)
			# cv2.waitKey()
			grayscaled = cv2.cvtColor(crop_img,cv2.COLOR_BGR2GRAY)
			
			PILimg = Image.fromarray(grayscaled)
			string = pytesseract.image_to_string(PILimg, lang="eng", config="-psm 10")
			# print string
			if string == "":
				string = "I"
			vector.append(str(string).upper())
		# print len(vector)
		vector = [vector[4*i : 4*(i+1)] for i in range(4)]
		return vector


# image = "examples/image.jpg"

# vector = vector_gen(image)

# print vector