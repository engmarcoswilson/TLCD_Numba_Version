

"""
Solução numérica
Sistema 1GdL - Estrutura Principal
Autor: Marcos Wilson Rodrigues de Lima 
"""

import csv
import numba
import numpy as np
import pandas as pd
from TLCD_functions import estrutura_principal_forca_bruta
from TLCD_functions import forca_bruta_1gdl
import time

#Frequência de Excitação
Omg_exc = np.linspace(0, 3, 1000)

#Tempo
n = 5000
t = np.linspace(0, 400, n)

#Características da Estrutura Principal
ms = 176.935 #Kg
ks = 18330  #N/m
cc = 2*np.sqrt(ms*ks)   #Ccrítico
#cs = es*cc
cs = 36.73  #N.s/m
ws = np.sqrt(ks/ms)/(2*np.pi)  #Frequência Natural
es = cs/cc

#Condição inicial
z0 = [0, 0]   # x=0 e v=0

#Dados da Força
f0 = 1
F = f0 * ks   #Amplitude da força

#Execução da Simulação

#Estrutura Principal
f = open('Structure_1gdl_numerical.csv', 'w', newline='', encoding = 'utf-8')
w = csv.writer(f)

H_numerical = np.zeros(len(Omg_exc))

a = time.time()
for i in range(0, len(Omg_exc)):
    H_numerical[i] = forca_bruta_1gdl(z0, t, ms, ks, cs, f0, Omg_exc[i])
    w.writerow([Omg_exc[i], H_numerical[i]])
b=time.time()
print('finalizado')
print('Tempo de execução: ',b-a, ' s')
