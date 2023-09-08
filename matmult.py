#Matrix Multiplication
#Kevin Lai 101288231

import math

#function that takes a given matrix and multiplies it by a given scalar and returns a new list containing the results
#parameters: matrix: list representing 2D matrices: Scale: scalar to be multiplied by the given matrix
#return values: new_list: new list with results of the given matrix multiplied by the given scalar
def mult_scalar(matrix, scale):
	new_list = []
	for i in range(len(matrix)):
		new_list.append([])
		for j in range(len(matrix[i])):
			new_list[i].append(0)
			new_list[i][j] = matrix[i][j] * scale

	return new_list

#function that takes a given matrix and multiplies it by another given matrix and returns a new list containing the results
#parameters: a: list representing 2D matrices: b: list representing 2D matrices
#return values: new_list: new list with results of the given matrix multiplied by another given matrix
def mult_matrix(a, b):
	new_list = []

	if(len(a[0]) == len(b)):
		for i in range(len(a)):
			new_list.append([])
			for j in range(len(b[0])):
				new_list[i].append(0)
				for k in range(len(b)):
					new_list[i][j] += (a[i][k] * b[k][j])
	else:
		return None

	return new_list

#function that takes  two vectors and calculates the Euclidean distance between the two vectors
#parameters: a: list representing a vector: b: list representing vector
#return values: math.sqrt(total): the Euclidean distance between the two vectors
def euclidean_dist(a,b):
	if not a or not b:
		return None
	if len(a[0]) != len(b[0]):
		return None

	total = 0

	for i in range(len(a[0])):
		total += pow(a[0][i]-b[0][i],2)

	return math.sqrt(total)
