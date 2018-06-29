# Gravity Simulator
A simple planetary gravity simulator using numerical methods -- specifically [Euler's Method](https://en.wikipedia.org/wiki/Euler_method). [Runge-Kutta method](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods) is more accurate, but is a lot more complicated for this _particular_ beginner's project, so.

## How to download:
Your computer needs to have [python installed](https://www.python.org/getit/) (python3 on Unix systems) for this program to predictably function.

Since this is a scientific computing project (in python) you would need a lot of scientific packages, specifically:
1. `matplotlib`
2. `numpy`

The easiest way is to get [Anaconda](https://www.anaconda.com/) which is a pretty large package, but gets everything you need to get things up and running.

The more complicated way is to use `pip` and install `matplotlib` and `numpy`.

## Usage : 
```
	python gravity.py
```
And that's all there is to it.

(Unix users might have to use python3 instead of python)



# Features
This program is a very simple simulator where it has some kind of orbiting probe located above a particular planet (the specifications of which can be altered in the source code). The horizontal velocity ranges from 1 all the way to 1.3 units which gives you a fair idea about the different kinds of orbits that an orbiter can perform.

Additionally, after receiving some feedback (mostly from Reddit (thanks [r/python](https://www.reddit.com/r/python))) I've added a function that also calculates the total energy of the planet-orbiter system. So, when you run the program now, you will see the different orbits (that you might have chosen) along with their corresponding Kinetic Energy, Potential Energy and Total Energy of the orbiter.

This repo also includes some sample orbits in case you want to check them out.


## TODO:
Currently, the only way to play around with the parameters is by directly editing them in the source code. Hopefully, the source code is well documented enough so that it doesn't seem impossible to edit the right things in the right places.

Also a future update might include the Runge-Kutta method, as well as a comparison between the Euler simulation and the Runge-Kutta simulation.

