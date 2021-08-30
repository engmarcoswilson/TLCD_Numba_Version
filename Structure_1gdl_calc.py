# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 15:03:31 2021

@author: Marcos
"""

import numpy as np
import time
import numba

M = np.array([[1 , 2],
              [3, 4]])
soma = 0.0

def sum_numpy(M):
    soma = np.sum(M)
    return soma

def sum_python(M):
    soma = 0.0
    for i in range(0, len(M)):
        for j in range(0, len(M)):
            soma += M[i, j]
    return soma

@numba.jit
def sum_numba(M):
    soma = 0.0
    for i in range(0, len(M)):
        for j in range(0, len(M)):
            soma += M[i, j]
    return soma