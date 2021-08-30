"""
Solução analítica e numérica - PLOTAGEM
Sistema 1GdL - Estrutura Principal
Autor: Marcos Wilson Rodrigues de Lima 
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dados = pd.read_csv('Structure_1gdl_analytical.csv')
dados = dados.dropna()
dados = dados.to_numpy()
Omg_exc = dados[:,0]
H_analitico = dados[:,1]

#valor máximo - Amplitude
H_max = np.amax(H_analitico)

#valor máximo - Amplitude em dB
H_max_db = 20*np.log10(H_max/1000)
H_max_db = float("{:.3f}".format(H_max_db))

#frequência de excitação para Amplitude máxima
ind_max = np.argmax(H_analitico)
Omg_exc[ind_max]= float("{:.3f}".format(Omg_exc[ind_max]))


plt.figure(figsize=(16,8))
plt.plot(Omg_exc, 20*np.log10(H_analitico/1000),label='H - analytical')
plt.plot(Omg_exc[ind_max], H_max_db, '-o', color = 'blue')
plt.text(Omg_exc[ind_max]-0.2, H_max_db +0.5, (Omg_exc[ind_max],H_max_db),fontsize=16)
plt.rc('axes', titlesize=16)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rcParams.update({'font.size': 16})
plt.xlabel("$\Omega_{exc} [Hz]$", fontsize=16)
plt.ylabel('H(i$\Omega$) [dB]')
plt.legend(loc='best', fontsize=16)
plt.grid()
plt.show()