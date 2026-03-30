from ChaoticSystem import ChaoticSystem
import numpy as np
"""
ChuaCurcuit defines the code for Chua's Circuit, which is
a set of three ODEs defined by Leon Chua in a simple electronic
circuit that exhibits chaotic behavior.

The system is defined by the following ODEs:
	dx/dt = α * (y - x - h(x))
	dy/dt = x - y + z
	dz/dt = -βy
where:
	h(x) is a piecewise-linear function representing the nonlinear resistor
"""
class ChuaCircuit(ChaoticSystem):
	"""
	Initializes the Chua System coefficients
	"""
	def __init__(self, initial_state=None, α=9.0, β=14.282, m0=-1.143, m1=-0.714):
		super().__init__(initial_state)
		# Define coefficients for σ, ρ, and β by the passed in values
		print(f"Chua Coefficients: α={α}, β={β}, m0={m0}, m1={m1}")
		self.α = α 
		self.β = β
		self.m0 = m0
		self.m1 = m1 
  
	"""
	Computes the Chua's Circuit derivatives dx, dy, and dz
	given the state x, y, z.
	This is found from the system definition:
	dx/dt = α * (y - x - h(x))
	dy/dt = x - y + z
	dz/dt = -βy
	"""
	def compute_derivatives(self, state):
		x, y, z = state
  
		dx = self.α * (y - x - (self.m1 * x + 0.5 * (self.m0 - self.m1) * (np.abs(x + 1) - np.abs(x - 1))))		
		dy = x - y + z
		dz = -self.β * y

		return np.array([dx, dy, dz])