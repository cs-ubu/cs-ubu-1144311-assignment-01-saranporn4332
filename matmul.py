import numpy as np
import csv


def readm(fname ='A.csv'):
    f = open(fname, 'r') # w,b
    A = []
    for line in f.readline():
        A.append( [float(x) for x in line.strip().split(',')] )
    print(A)
    f.close()
return A

def matmul(A,b):
    m, n = len(A), len(b[0])
    J = len( A[0] ) # A-mxJ #b -Jxn
    if len(A[0]) == len(b):
        #C = [ [0]*n for i in range(n) ]
        C = [[0]*n]*m
       # A[0][0]*b[0][0] + A[0][1]*b[1][0] + A[0][2]*b[2][0]
        for r in range(m):
            for c in range(n): 
                C[r][c] = sum([float(A[c][j])*float(b[j][c]) for j in range(J)])
        return C
    return [] #  ไม่สามารถดูได้
