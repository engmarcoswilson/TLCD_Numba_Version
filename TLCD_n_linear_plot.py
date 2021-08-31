# -*- coding: utf-8 -*-
"""
Simulação TLCD não-linear
Leitura arquivos csv (Omg_exc x w0)
Plotagem Omg_exc x w0
Marcos Wilson
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

    
dados = pd.read_csv('TLCD_n_linear.csv')
dados = dados.dropna()
dados = dados.to_numpy()
Omg_exc = dados[:,0]
w0 = dados[:,1]

w0_max = np.amax(w0)
ind_max = np.argmax(w0)
w0_max = float("{:.3f}".format(w0_max))
w0_max_db = 20*np.log10(w0_max/1000)
w0_max_db = float("{:.3f}".format(w0_max_db))
Omg_exc[ind_max] = float("{:.3f}".format(Omg_exc[ind_max]))

plt.figure(figsize=(16,8))
plt.plot(Omg_exc, 20*np.log10(w0/1000),label='$w_{0}$ - nonlinear solution', color='black')
plt.plot(Omg_exc[ind_max], w0_max_db,'-o', color='black')
plt.text(Omg_exc[ind_max]-0.18, w0_max_db +2, (Omg_exc[ind_max],w0_max_db),fontsize=16, color='black')
#plt.xscale("log")
plt.rc('axes', titlesize=16)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rcParams.update({'font.size': 16})
plt.xlabel("$\Omega_{exc} [Hz]$")
plt.ylabel('$w_{0}$ [dB]')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(loc='best', fontsize=14)
plt.grid()
plt.savefig('TLCD_freq_x_w0', format='png')
plt.show()
