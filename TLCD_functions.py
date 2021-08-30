# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 16:12:43 2021

@author: Marcos
"""
import math
import numpy as np
from scipy.integrate import odeint
import numba

#Estrutura Principal
@numba.jit
def estrutura_principal_analitico(Omg_exc, wn, es):
    w = (Omg_exc)/wn
    H = (1/np.sqrt(np.square((1-np.square(w)))+np.square(2*es*w)))
    return H

@numba.jit
def estrutura_principal_forca_bruta(z, t, m, k, c, f0, Omg_exc):
  x = z[0]
  v = z[1]
  dxdt = v
  dvdt = -(c/m)*v - (k/m)*x + (1/m)*(f0*k*np.cos(Omg_exc*2*np.pi*t))  #f = f0*cos(Omg_exc*t)
  dzdt = [dxdt, dvdt]
  return dzdt