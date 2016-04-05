#!/usr/bin/python
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

m = np.genfromtxt('MINT_Krho_S_wave.txt', skip_header=1,delimiter=',')
m1 = np.genfromtxt('DP4.txt', skip_header=1, skip_footer=5e5)
f1 = np.genfromtxt("DP4.txt", skip_header=500001)

m12 = m[:,0]
m34 = m[:,1]
c12 = m[:,2]
c34 = m[:,3]
phi = m[:,4]

m12_1 = m1[:,0]
m34_1 = m1[:,1]
c12_1 = m1[:,2]
c34_1 = m1[:,3]
phi_1 = m1[:,4]

weights = .5e-5 * np.ones_like(m12)

plt.figure(figsize=(12,6))
plt.hist(m12,100, weights=weights,alpha=0.5,label='MINT')
plt.hist(m12_1,100, weights=f1/np.sum(f1),alpha=0.5, label='GooFit')
plt.title(r'$(K^*\rho^0)_S\ m(\pi^+\pi^-)$', fontsize=20)
plt.legend()
plt.savefig("KRS_m12.png")

plt.figure(figsize=(12,6))
plt.hist(m34,100, weights=weights,alpha=0.5,label='MINT')
plt.hist(m34_1,100, weights=f1/np.sum(f1),alpha=0.5, label='GooFit')
plt.title(r'$(K^*\rho^0)_S\ K^-\pi^-$', fontsize=20)
plt.legend()
plt.savefig("KRS_m34.png")

plt.figure(figsize=(12,6))
plt.hist(phi,100, weights=weights,alpha=0.5,label='MINT')
plt.hist(phi_1,100, weights=f1/np.sum(f1),alpha=0.5, label='GooFit')
plt.title(r'$(K^*\rho^0)_S \ \phi$', fontsize=20)
plt.legend()
plt.savefig("KRS_phi.png")

plt.figure(figsize=(12,6))
plt.hist(c12,100, weights=weights,alpha=0.5,label='MINT')
plt.hist(c12_1,100, weights=f1/np.sum(f1),alpha=0.5, label='GooFit')
plt.title(r'$(K^*\rho^0)_S \ \cos(\theta_{12})$', fontsize=20)
plt.legend()
plt.savefig("KRS_c12.png")

plt.figure(figsize=(12,6))
plt.hist(c34,100, weights=weights,alpha=0.5,label='MINT')
plt.hist(c34_1,100, weights=f1/np.sum(f1),alpha=0.5, label='GooFit')
plt.title(r'$(K^*\rho^0)_S \ \cos(\theta_{34})$', fontsize=20)
plt.legend()
plt.savefig("KRS_c34.png")