#! python3

import numpy as np
import matplotlib.pyplot as plt


G = 1.0
M = 1.0
Re = 1.0

def plot_earth(fig,r=Re):
	"""
	Plots a circle (planet) with the radius given. Default value
	is the radius of the Earth
	"""
	x = np.linspace(-1,1,1000)
	yp = np.sqrt(r**2 - x**2)
	yn = -1*np.sqrt(r**2 - x**2)
	fig.plot(x,yp,color="black")
	fig.plot(x,yn,color="black")

def derive(params):
	"""
	function that returns the derivative each individual element
	given in the parameter list
	params => [x, y, vx, vy]
	returns => [vx,vy,ax,ay]

	Since this is a single planet gravitational simulation, ax and ay
	represent the acceleration due to gravity caused by the planet.
	"""
	x,y,dx,dy=params
	r = (x**2 + y**2)**0.5
	return np.array([dx,dy,-G*M*x/(r**3),-G*M*y/(r**3)])

def check_in(x,y,R=Re):
	"""
	a function that receives the x and y coordinates of the orbiter and the
	radius of the planet being orbitted (default being radius of the Earth)
	and returns whether the orbitter is within the planet or not (aka, has
	the orbiter crashed)
	"""
	r = np.sqrt(x**2 + y**2)
	return r <= R



def run(initial_param,fig,N=15000,h=0.001,energy_debug=False):
	"""
	a function that runs the simulation given the inital parameters, the number
	of iterations each simulation must go through (default => 15000), and the
	'h' value, smaller of which would take more time but also more accurate results.
	initial_param => [x0,y0,vx0,vy0]

	This numerical simulation uses Euler's Method (and not Runge-Kutta or better
	but more complicated methods)
	"""
	data = np.zeros((N,4))
	data[0] = initial_param
	for t in range(N-1):

		# using Euler's method
		# f(x_i+1) = f(x_i) + h*f'(x_i)
		# except since this is a numpy array, we can update all
		# functions/variables at the same time.

		data[t+1] = data[t] + h*(derive(data[t]))

		# the below statement is to end the simulation
		# if the orbiter crashes/lands
		if check_in(data[t+1][0],data[t+1][1]):
			break

	fig.plot(data[:,0],data[:,1])

	if energy_debug:
		return data

def plot_energy(data,t,fig):
	# data => [x,y,vx,vy]
	# KE = T = 0.5*m*(vx**2 + vy**2)
	# PE = U = G*M*m/(x**2 + y**2)**0.5

	m = 0.2

	T = 0.5*m*(data[:,2]**2 + data[:,3]**2)
	U = -G*M*m/(np.sqrt(data[:,0]**2 + data[:,1]**2))


	fig.plot(T,label="Kinetic Energy")
	fig.plot(U,label="Potential Energy")
	fig.plot((T+U),label="Total Energy")
	fig.legend()




print("simulation start")


for (t,vxs) in enumerate(np.linspace(1,1.3,5)):
	# running through all vxs from 1 to 1.3
	
	# creating multiple plots for the same orbit

	fig, axs = plt.subplots(1,2,figsize=(19,10))

	plot_earth(fig=axs[0])
	axs[0].axis('equal')
	data = run([0,1.0,vxs,0],energy_debug=True,fig=axs[0])

	plot_energy(data,t,fig=axs[1])
	plt.savefig("orbit-energy-vx-{}.pdf".format(t))
	plt.close()

	# comment out below code if no energy-debug




print("simulation over.")

