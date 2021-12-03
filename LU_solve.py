import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

def lu(A):
    n = A.shape[0]
    U = A.copy()
    L = np.eye(n, dtype=np.double)
    
    for i in range(n):
        factor = U[i+1:, i] / U[i,i]
        L[i+1:, i] = factor
        U[i+1:] -= factor[:, np.newaxis] * U[i]
    return L, U

def plu(A):
    n = A.shape[0]
    U = A.copy()
    L = np.eye(n, dtype=np.double)
    P = np.eye(n, dtype=np.double)
    
    for i in range(n):
        for k in range(i,n):
            if ~np.isclose(U[i,i], 0.0):
                break
            U[[k, k+1]] = U[[k+1, k]]
            P[[k, k+1]] = P[[k+1, k]]
        factor = U[i+1:, i] / U[i,i]
        L[i+1:, i] = factor
        U[i+1:] -= factor[:, np.newaxis] * U[i]
    return P, L, U

def forward_substitution(L, b):
    n = L.shape[0]
    y = np.zeros_like(b, dtype=np.double)
    y[0] = b[0]/L[0, 0]
    for i in range(1,n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i,i]
        
    return y

def back_substitution(U, y):
    n = U.shape[0]
    x = np.zeros_like(y, dtype=np.double)
    x[-1] = y[-1] / U[-1, -1]
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i:], x[i:])) / U[i,i]
    return x

def lu_solve(A, b):
    L, U = lu(A)
    y = forward_substitution(L, b)
    return back_substitution(U, y)

A = np.array([[1,4,5], [6, 8, 22], [32, 5., 5]])
b = np.array([1,2,3.])
print(lu_solve(A, b))