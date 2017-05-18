# -*- coding: utf-8 -*-
"""
Created on Thu May 18 06:31:28 2017

@author: Njabulo Mbanjwa, CP tut3 Question3
"""
from __future__ import division, print_function
import numpy as np

n= 101
tfin= 2*np.pi
dt= tfin/(n-1)
s= np.arange(n)
y= np.sinc(dt*s)
fy= np.fft.fft(y)
wps= np.linspace(0,2*np.pi,n+1)[:-1]
basis= 1.0/n*np.exp(1.0j * wps * s[:,np.newaxis])
recon_y= np.dot(basis,fy)
yerr= np.max(np.abs(y-recon_y))

print('yerr:',yerr)

lin_fy= np.linalg.solve(basis,y)
fyerr= np.max(np.abs(fy-lin_fy))

print('fyerr',fyerr)



