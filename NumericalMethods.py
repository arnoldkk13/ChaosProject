"""
numerical_methods houses the code for numerical methods used in the Lorenz 
Attractor model. This uses the strategy design pattern to choose numerical methods
either at runtime or using a passed in flag.
This is written by Kyle Arnold for Math435
"""
import numpy as np

"""
Forward Euler (or Explicit Euler) is the simplest method that computes updates based 
off of the current location and the current time step derivative.
"""
class ForwardEuler:
	"""
	Performs one step of the forward euler and updates all states
	"""
	def step(self, system, dt):
		dx, dy, dz = system.compute_derivatives(system.state)
		derivative = np.array([dx, dy, dz])
		system.state = system.state + dt * derivative
		system.trajectory.append(system.state.copy())
		return dt, True # The time derivative does not change and the state is always accepted
	
"""
The Dormand-Prince 45 method is a 5th and 4th order Runge-Kutta method
that is used to model the Lorenz system. The
"""	
class DormandPrince45:
	def __init__(self):
		"""Butcher Tableau for dopri45"""
		self.A = np.array([
		[0, 0, 0, 0, 0, 0, 0],
		[1/5, 0, 0, 0, 0, 0, 0],
		[3/40, 9/40, 0, 0, 0, 0, 0],
		[44/45, -56/15, 32/9, 0, 0, 0, 0],
		[19372/6561, -25360/2187, 64448/6561, -212/729, 0, 0, 0],
		[9017/3168, -355/33, 46732/5247, 49/176, -5103/18656, 0, 0],
		[35/384, 0, 500/1113, 125/192, -2187/6784, 11/84, 0]
		])

		self.C = np.array([0, 1/5, 3/10, 4/5, 8/9, 1, 1])

		"""4th and 5th Order Coefficients"""
		self.b_high = np.array([35/384, 0, 500/1113, 125/192, -2187/6784, 11/84, 0])
		self.b_low = np.array([5179/57600,0,7571/16695,393/640,-92097/339200,187/2100,1/40])
	
		self.stages = 7
		self.order = 5 

class HeunEuler:
	def __init__(self):
		"""Butcher Tableau for Heun-Euler 2(1) method"""
		self.A = np.array([
			[0,   0],
			[1,   0],
			[1/2, 1/2]  # This row is just for Heun's final combination
		])

		self.C = np.array([0, 1, 1])  # Nodes (c)

		"""1st and 2nd Order Coefficients"""
		self.b_high = np.array([1/2, 1/2, 0])  # 2nd order (Heun)
		self.b_low = np.array([1,   0,   0])  # 1st order (Euler)

		self.stages = 3

class RungeKutta:
	def __init__(self, method):
		
		self.method = method()
	"""
	Uses an adaptive step distance based on the error and tolerance we set up
	"""
	def adaptive_step(self, dt, error, order, tol=1e-3):
		safety = .9
		min_dt = 1e-6  # don't allow dt below this
		# If error is too small to be tracked, increase the timestep 
		if error == 0:
			return dt * 2
		
		scale = safety * (tol / error) ** (1/order)
		
		dt_new = min_dt
        
		if dt_new < min_dt:
			print(f"Warning: dt clipped to min_dt={min_dt}")
			dt_new = min_dt
		
		return dt * np.clip(scale, min=.1, max=5.0) 
	
	## TODO: Write the runge_kutta_stepper method that takes in the method name and returns the step
	# That we use for this
	"""
	Performs one step with the specified Runge Kutta method
	"""
	def step(self, system, dt, tol=1e-3):
		A = self.method.A
		C = self.method.C
		b_high = self.method.b_high
		b_low = self.method.b_low
		stages = self.method.stages
		order = self.method.order

		k = [None] * stages

		for i in range(stages):
			y_temp = system.state.copy()

			for j in range(i):
				y_temp += dt * A[i][j] * k[j]

			k[i] = system.compute_derivatives(y_temp)

		y_high = system.state.copy()
		y_low  = system.state.copy()

		for i in range(stages):
			y_high += dt * b_high[i] * k[i]
			y_low  += dt * b_low[i]  * k[i]

		error = np.linalg.norm(y_high - y_low)

		dt_new = self.adaptive_step(dt, error, order, tol)

		if error < tol:
			system.state = y_high
			return dt_new, True
		else:
			return dt_new, False
