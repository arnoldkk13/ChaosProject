"""
numerical_methods houses the code for numerical methods used in the Lorenz 
Attractor model. This is written by Kyle Arnold for Math435
"""
import numpy as np


"""
Verlet integration is a second order symplectic numerical method that is
energy conserving
"""
def verlet_integration():
	pass
	# for body in self.bodies:
	# 	body.v += 0.5 * body.a * Δt

	# # Full-step for position
	# for body in self.bodies:
	# 	body.d += body.v * Δt
	# 	body.positionArray.append(body.d.copy())

	# # Compute all accelerations using their updated position
	# new_accelerations = [self.compute_acceleration(body) for body in self.bodies]

	# # Second half-step for velocity using the new accelerations
	# for body, a_new in zip(self.bodies, new_accelerations):
	# 	body.v += 0.5 * a_new * Δt
	# 	body.a = a_new


"""
The Dormand-Prince 45 method is a 5th and 4th order Runge-Kutta method
that is used to model. This is
"""
def dopri45(self):
		"""Butcher Tableau for dopri45"""
		A = np.array([
		[0, 0, 0, 0, 0, 0, 0],
		[1/5, 0, 0, 0, 0, 0, 0],
		[3/40, 9/40, 0, 0, 0, 0, 0],
		[44/45, -56/15, 32/9, 0, 0, 0, 0],
		[19372/6561, -25360/2187, 64448/6561, -212/729, 0, 0, 0],
		[9017/3168, -355/33, 46732/5247, 49/176, -5103/18656, 0, 0],
		[35/384, 0, 500/1113, 125/192, -2187/6784, 11/84, 0]
	])

		C = np.array([0, 1/5, 3/10, 4/5, 8/9, 1, 1])
  
		"""4th and 5th Order Coefficients"""
		b5 = np.array([35/384, 0, 500/1113, 125/192, -2187/6784, 11/84, 0])
		b4 = np.array([5179/57600,0,7571/16695,393/640,-92097/339200,187/2100,1/40])
	
		return A,b4,b5,C, 7 # Number of Steps for graphing

## TODO: Write the runge_kutta_stepper method that takes in the method name and 

"""
runge_kutta_stepper 
"""
def runge_kutta_stepper(method):
	# Retrieve the butcher tableau for each method
	#      Here, b_low correlates to the array for the lower dimension coefficients and 
	#      b_high correlates to the array for the higher dimension coefficients
	A, b_low, b_high, C, steps = method() 
	
	for i in range(steps):
		pass
	pass 