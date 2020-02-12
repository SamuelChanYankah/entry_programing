#K-Means clustering implementation

#Some hints on how to start have been added to this file.
#You will have to add more code than just the hints provided here for the full implementation.

# The below modules are required to run the program

import csv
import math
import matplotlib.pyplot as plt
import numpy as np
import random
import statistics


# ====
# Define a function that computes the distance between two data points

# Calculates the distance between two coordinates
def dist(x1, y1, x2, y2):
	distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
	return distance

# Finds the closest of three points to a given point
def closestPoint(p1, p2, p3, p4):
	d1 = dist(p1[0], p1[1], p2[0], p2[1])
	d2 = dist(p1[0], p1[1], p3[0], p3[1])
	d3 = dist(p1[0], p1[1], p4[0], p4[1])
	minD = min([d1, d2, d3])
	if minD == d1:
		return 1
	elif minD == d2:
		return 2
	else:
		return 3

# ====
# Define a function that reads data in from the csv files  HINT: http://docs.python.org/2/library/csv.html

# Asks the user which data they would like to use
year = int(input("Type 1 for 1953, 2 for 2008, or 3 for both: "))

# Number of iterations that the algorithm will complete
iterations = 4


# Reads one of three CSV files, depending on the user's choice
# Returns a dictionary with the Keys being the countries in the CSV file, and the Values being the birthrate and life expectancy as a list
def readCSV(data):
	if (data == 1):
		file = 'data1953.csv'

	elif (data == 2):
		file = 'data2008.csv'
		
	elif (data == 3):
		file = 'dataBoth.csv'

	with open(file) as csvfile:
		read = csv.reader(csvfile)
		countries = {}

		for row in read:
			if (row[0] != "Countries"):
				countries[row[0]] = [float(row[1]), float(row[2])]

	return countries

# Reads the user's choice of CSV file: data from 1953, 2008, or both
year = readCSV(year)

# Returns a list of the birthrates of all the countries in the dictionary
def birthrate(countries):
	brList = []
	for country in countries:
		brList.append(countries.get(country)[0])
	return brList

# Returns a list of the life expectancies of all teh countries in the dictionary
def lifeExp(countries):
	leList = []
	for country in countries:
		leList.append(countries.get(country)[1])
	return leList

# ====
# Write the initialisation procedure

# The X values for the plots will be the birthrates of all the countries
# The Y values will be the life expectancies
x = birthrate(year)
y = lifeExp(year)

# A list of the data for all the countries in the dictionary
listXY = list(year.values())

# Number of clusters hardcoded to 3
K = 3

# Selects three random coordinates from the list of the data for the countries in the dictionary
centroids = random.sample(listXY, K)

# Stores each centroid in its own variable
c1 = centroids[0]
c2 = centroids[1]
c3 = centroids[2]

# Creates a set of axes based on the user's choice of iterations 
fig, ax = plt.subplots(math.ceil(iterations/2), 2) 

# Labels the axes and ensures the labels are on the outside of the outermost subplots
for a in ax.flat:
    a.set(xlabel='Birthrate', ylabel='Life Expectancy')
for a in ax.flat:
    a.label_outer()

# For the first iteration of the algorithm, all the data is scattered in black
ax[0, 0].scatter(x, y, color = 'k')

# The randomly selected centroids are scattered in red, blue, and green respectively
ax[0, 0].scatter(c1[0], c1[1], color = 'b')
ax[0, 0].scatter(c2[0], c2[1], color = 'g')
ax[0, 0].scatter(c3[0], c3[1], color = 'r')


# ====
# Implement the k-means algorithm, using appropriate looping

# These values are used to move to the next subplot with each iteration
currentX = 0
currentY = 0

# Dictionary created to divide countries based on which centroid is closest
clusters = ['r', 'g', 'b']
countriesInClusters = {key: [] for key in clusters}

# The function of the algorithm
def kmeans(year):

	# At the beginning of each iteration (after the first), the next subplot is selected
	# Either the subplot to the right or the first subplot on the next line is chosen depending on which subplot was used last
	global currentX, currentY

	if currentY == 0:
		currentY += 1

	else:
		currentY -= 1
		currentX += 1

	# The centroids are to be reassigned with each iteration
	global c1, c2, c3

	# Lists of the x and y coordinates for each cluster/group
	# These lists are used to calculate the mean values for each cluster
	g1x = []
	g1y = []
	g2x = []
	g2y = []
	g3x = []
	g3y = []

	# Allows for reassignment of the clusters and the dictionary of which countries appear in those clusters
	global clusters
	global countriesInClusters 

	countriesInClusters = {key: [] for key in clusters}

	# Used to monitor convergence
	rSqDist = 0
	gSqDist = 0
	bSqDist = 0

	# Groups the data based on which centroid is closest
	for key in year:
		point = year[key]
		md = closestPoint(point, c1, c2, c3)
		if md == 1:
			g1x.append(point[0])
			g1y.append(point[1])
			countriesInClusters['r'].append(key)
			rSqDist += (dist(point[0], point[1], c1[0], c1[1]) ** 2)

		elif md == 2:
			g2x.append(point[0])
			g2y.append(point[1])
			countriesInClusters['g'].append(key)
			gSqDist += (dist(point[0], point[1], c2[0], c2[1]) ** 2)

		else:
			g3x.append(point[0])
			g3y.append(point[1])
			countriesInClusters['b'].append(key)
			bSqDist += (dist(point[0], point[1], c3[0], c3[1]) ** 2)

	# Changes the colour of the points to reflect the changes in clusters with each iteration
	ax[currentX, currentY].scatter(g1x, g1y, color = 'm')
	ax[currentX, currentY].scatter(g2x, g2y, color = 'y')
	ax[currentX, currentY].scatter(g3x, g3y, color = 'c')

	ax[currentX, currentY].scatter(c1[0], c1[1], color = 'r')
	ax[currentX, currentY].scatter(c2[0], c2[1], color = 'g')
	ax[currentX, currentY].scatter(c3[0], c3[1], color = 'b')

	# Reassigns the centroids as the mean values of each cluster in the current iteration
	c1 = [(statistics.mean(g1x)), statistics.mean(g1y)]
	c2 = [(statistics.mean(g2x)), statistics.mean(g2y)] 
	c3 = [(statistics.mean(g3x)), statistics.mean(g3y)]
	
	# Prints squared distances at the end of each iterations to monitor convergence
	print(rSqDist, gSqDist, bSqDist)

# Runs the algorithm as many times as the user chooses
for i in range(iterations - 1):
	kmeans(year)
	i += 1

# Shows the plot after all the iterations have run
plt.show()

# ====
# Print out the results

# Formatted sentences showing how many and which countries are in each cluster
red = str.format("There are {} countries in the red cluster: {}. \n\n", len(countriesInClusters['r']), ", ".join(countriesInClusters['r']))
green = str.format("There are {} countries in the green cluster: {}. \n\n", len(countriesInClusters['g']), ", ".join(countriesInClusters['g']))
blue = str.format("There are {} countries in the blue cluster: {}. \n\n", len(countriesInClusters['b']), ", ".join(countriesInClusters['b']))

# The mean data for each cluster
redBirthrate = c1[0]
redLifeExp = c1[1]
greenBirthrate = c2[0]
greenLifeExp = c2[1]
blueBirthrate = c3[0]
blueLifeExp = c3[1]

# Formatted sentence showing the mean data of each cluster
redMean = str.format("The mean birthrate of the red cluster is {} and the mean life expectency is {}.\n\n", redBirthrate, redLifeExp)
blueMean = str.format("The mean birthrate of the green cluster is {} and the mean life expectency is {}.\n\n", greenBirthrate, greenLifeExp)
greenMean = str.format("The mean birthrate of the blue cluster is {} and the mean life expectency is {}.\n\n", blueBirthrate, blueLifeExp)

# Prints the formatted sentences
print(red, green, blue)
print(redMean, blueMean, greenMean)
