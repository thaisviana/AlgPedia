#! /usr/bin/env python

"""
Solve linear system using LU decomposition and Gaussian elimination
"""

import numpy as np
from scipy.linalg import lu, inv

def gausselim(A,B):
    """
    Solve Ax = B using Gaussian elimination and LU decomposition.
    A = LU   decompose A into lower and upper triangular matrices
    LUx = B  substitute into original equation for A
    Let y = Ux and solve:
    Ly = B --> y = (L^-1)B  solve for y using "forward" substitution
    Ux = y --> x = (U^-1)y  solve for x using "backward" substitution
    :param A: coefficients in Ax = B
    :type A: numpy.ndarray of size (m, n)
    :param B: dependent variable in Ax = B
    :type B: numpy.ndarray of size (m, 1)
    """
    print "A.size = ", A.size, "B.size = ", B.size
    # LU decomposition with pivot
    pl, u = lu(A, permute_l=True)
    # forward substitution to solve for Ly = B
    y = np.zeros(B.size)
    for m, b in enumerate(B.flatten()):
        print ##########################
        print "y.size = ", y.size, 
        print "m = ", m
        print "pl.size = ", pl.size
        print "pl[m,m] = ", pl[m,m]
        y[m] = b
        # skip for loop if m == 0
        if m:
            for n in xrange(m):
                y[m] -= y[n] * pl[m,n]
        y[m] /= pl[m, m]

    # backward substitution to solve for y = Ux
    x = np.zeros(B.size)
    lastidx = B.size - 1  # last index
    for midx in xrange(B.size):
        m = B.size - 1 - midx  # backwards index
        x[m] = y[m]
        if midx:
            for nidx in xrange(midx):
                n = B.size - 1  - nidx
                x[m] -= x[n] * u[m,n]
        x[m] /= u[m, m]
    return x

if __name__ == '__main__':

    P = [[0.2,0.3333333333333333,0.16666666666666666,0.8333333333333334],
        [1.0,0.0,0.5,1.0],
        [0.03125,0.03125,0.18181818181818182,0.34375],
        [0.0,0.4,0.2,1.0],
        [0.5,0.0,0.5,1.0],
        [1.0,1.0,1.0,1.0],
        [1.0,0.0,0.5,1.0],
        [1.0,0.0,1.0,1.0],
        [0.09090909090909091,0.09090909090909091,1.0,1.0],
        [0.0,0.4,0.2,1.0],
        [0.0,0.0,0.5,1.0],
        [0.0,1.0,1.0,1.0],
        [0.0,0.0,0.5,1.0],
        [1.0,0.0,1.0,1.0],
        [1.0,1.0,1.0,1.0],
        [1.0,0.0,0.5,1.0],
        [1.0,0.0,0.0,1.0],
        [1.0,0.0,1.0,1.0],
        [0.09090909090909091,0.09090909090909091,1.0,1.0]]

    D = [[0.0041785,0,0,0.149373225,0.3983286,0.3983286,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0.0083631,0,0,0.148745535,0,0.39665476,0.39665476,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0.0154262,0,0,0.14768607,0,0.39382952,0.39382952,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0.0262242,0,0,0,0,0,0.14606637,0.38951032,0.38951032,0,0,0,0,0,0,0],
        [0,0,0,0,0.0410857,0,0,0,0,0,0.143837145,0,0.38356572,0.38356572,0,0,0,0,0],
        [0,0,0,0,0,0.0593236,0,0,0,0,0,0.14110146,0,0.37627056,0.37627056,0,0,0,0],
        [0,0,0,0,0,0,0.0789426,0,0,0,0,0,0.13815861,0,0,0.36842296,0.36842296,0,0],
        [0,0,0,0,0,0,0,0.0968151,0,0,0,0,0,0.135477735,0,0.36127396,0.36127396,0,0],
        [0,0,0,0,0,0,0,0,0.1094264,0,0,0,0,0,0.13358604,0,0,0.35622944,0.35622944],
        [0,0,0,0,0,0,0,0,0,0.1139852,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0.1094264,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0.0968151,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0.0789426,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0.0593236,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0410857,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0262242,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0154262,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0083631,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0041785]]


    x = gausselim(np.array(P), np.array(D))
    print x
