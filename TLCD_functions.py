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

def forca_bruta_1gdl(z0, t, ms, ks, cs, f0, Omg_exc):
  #Z - u (movimento da estrutura)
  z = odeint(estrutura_principal_forca_bruta, z0, t, args=(ms, ks, cs, f0, Omg_exc))
  #RMS
  u0 = np.sqrt(np.mean(np.square(z[int(len(t)/3):int(len(t)),0])))*np.sqrt(2)
  return u0

#TLCD isolado
@numba.jit
def tlcd_estrutura(w, t, e_L, wa, alfa, u0, Omg_exc):
  vp = -(0.5)*(e_L)*abs(w[1])*w[1]-((2*np.pi*wa)**2)*w[0]-(alfa)*-((2*np.pi*Omg_exc)**2)*u0*np.cos(2*np.pi*Omg_exc*t)
  wp = w[1]
  return (wp, vp)

def tlcd_n_linear(tlcd_estrutura, winit, t, e_L, wa, alfa, u0, Omg_exc):
    warr = odeint(tlcd_estrutura, winit, t, args=(e_L, wa, alfa, u0, Omg_exc))
    w0 = np.sqrt(np.mean(np.square(warr[int(0.6*len(warr)):int(len(warr)),0])))*np.sqrt(2)
    return w0