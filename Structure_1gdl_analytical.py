
"""
Solução analítica e numérica
Sistema 1GdL - Estrutura Principal
Autor: Marcos Wilson Rodrigues de Lima 
"""

import csv
import numpy as np
import pandas as pd
from TLCD_functions import estrutura_principal_analitico

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

#Calculando e gravando resultados
f = open('Structure_1gdl_analytical.csv', 'w', newline='', encoding = 'utf-8')
w = csv.writer(f)

H_analitico = np.zeros(len(Omg_exc))
H_forca_bruta = np.zeros(len(Omg_exc))


for i in range(0, len(Omg_exc)):
    H_analitico[i] = estrutura_principal_analitico(Omg_exc[i], ws, es)
    w.writerow([Omg_exc[i], H_analitico[i]])
print('finalizado')