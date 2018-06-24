#! python3

import numpy as np
import matplotlib.pyplot as plt


G = 1.0
M = 1.0
Re = 1.0

def plot_earth(r=Re):
	"""
	Plots a circle (planet) with the radius given. Default value
	is the radius of the Earth
	"""
	x = np.linspace(-1,1,1000)
	yp = np.sqrt(r**2 - x**2)
	yn = -1*np.sqrt(r**2 - x**2)
	plt.plot(x,yp,color="black")
	plt.plot(x,yn,color="black")

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



def run(initial_param,N=15000,h=0.01):
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

	plt.plot(data[:,0],data[:,1])


print("simulation start")


for (t,vxs) in enumerate(np.linspace(1,1.3,5)):
	# running through all vxs from 1 to 1.3
	plt.figure()
	plt.axis('equal')
	plot_earth()
	run([0,1.0,vxs,0])
	plt.savefig("orbit-vx-{}.pdf".format(t))
	plt.figure(clear=True)

print("simulation over.")