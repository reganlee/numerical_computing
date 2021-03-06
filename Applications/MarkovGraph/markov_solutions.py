import numpy as np
from numpy import linalg as la

# This file is also used in the voronoi lab.

def prob_1():
	#problem 1
	#part 1
	A = np.array([[.75, .5], [.25, .5]])
	print A.dot(A)[0,0]
	#part 2
	print la.matrix_power(A, 20)[0,0]

def prob_2():
	#problem 2
	#part 1
	A = np.array([[1./4, 1./3, 1./2], [1./4, 1./3, 1./3], [1./2, 1./3, 1./6]])
	print A
	#part 2
	print A.dot(A)[0,1]
	#part 3
	#it is fine if they just raised the matrix to a few powers and did the comparison themselves
	Anew = A.dot(A)
	prev = A.copy()
	tol = .0000001
	iters = 1
	maxiters = 100
	while la.norm(prev-Anew) > tol:
		prev[:] = Anew
		Anew[:] = A.dot(Anew)
		if iters > maxiters:
			print "exceeded ", maxiters, " iterations."
			break
		iters += 1
	if iters is not maxiters+1:
		print "reached steady state after ", iters, " iterations."
	print Anew

def prob_3:
	#problem 3
	A = np.array([[0, 0, 1, 0, 1, 0, 1],
				  [1, 0, 0, 0, 0, 1, 0],
				  [0, 0, 0, 0, 0, 1, 0],
				  [1, 0, 0, 0, 1, 0, 0],
				  [0, 0, 0, 1, 0, 0, 0],
				  [0, 0, 1, 0, 0, 0, 1],
				  [0, 1, 0, 0, 0, 0, 0]], dtype=np.int64)
	A5 = la.matrix_power(A,5)
	coords = np.where(A5==np.max(A5))
	#note: indexing from 0
	print "maximum of 5 step connections at: ", zip(coords[0], coords[1])
	A7 = la.matrix_power(A,7)
	coords = np.where(A7==0)
	print "no 7 step connection for: ", zip(coords[0], coords[1])

def laplacian(A):
    """Calculate the Laplacian of a graph represented by the adjacency matrix A"""
    
    #check that A is integer and unweighted
    if A.dtype != np.int or np.any(A>1) or np.any(A<0):
        raise ValueError("This is not an unweighted graph.")
    if np.any(A.diagonal() != 0) or (A.T != A):
        raise ValueError("This graph is directed or contains self-edges.")
    
    D = np.diagflat(A.sum(axis=1))
    L = D - A
    return L
