# -*- coding: utf-8 -*-
"""
Created on Thu May 18 06:27:03 2017

@author: Njabulo Mbanjwa, CP tut3 Question1
"""
import numpy as np

class N_body:

#defining the initial variables
	def __init__(self,mass = 0,x_pos = 0, y_pos = 0):
		self.mass = mass
		self.x_pos = x_pos
		self.y_pos = y_pos
#Entries in a dictionary
	var = {'#_particles': 10, 'Gravitational constant': 6.67*10**-11}

	def potential_energy(self,m,x,y):
		r = np.zeros(len(x))
		E_top = np.zeros(len(r))
		f = np.ones(len(r))
		E = np.zeros(len(r))
		k = ()

		for k in range(0,len(m)):

			for i in range(0,len(x)):
				r[i] = np.sqrt((x[k]-x[i])**2 + (y[k]-y[i])**2)
                
				if r[i] != 0:
					f[i] = r[i]

			for i in range(0,len(x)):
				E_top[i] = N_body.var['Gravitational constant']*m[k]*m[i]

			for i in range(0,len(x)):
				if r[i] != 0:
					E[i] = E_top[i]/r[i]
			print (E.sum())

if __name__=="__main__":

	s = N_body.var['#_particles']
	x = np.random.randint(1,10,size=s)
	y = np.random.randint(1,10,size=s)
	m = np.random.randint(1,4,size=s)
	test = N_body(m,x,y)


	print ('The mass  ' + repr(test.mass))
	print ('The x position  ' + repr(test.x_pos))
	print ('The y position  ' + repr(test.y_pos),  "with potentials below")

	energy = test.potential_energy(test.mass,test.x_pos,test.y_pos)


