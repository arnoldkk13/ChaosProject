from ChaoticSystem import ChaoticSystem
import numpy as np
"""
RosslerAttractor defines the code for the Rossler Attractor, which is
a set of three ODEs defined by Otto Rossler in the 70s. They represent
chaotic dynamics associated with fractal properties (wikipedia).

convection.
The system is defined by the following ODEs:
	dx/dt = -y -z
	dy/dt = x + αy
	dz/dt = β + z(x - γ)
"""
class RosslerAttractor(ChaoticSystem):
	"""
	Initializes the Rossler System coefficients
	"""
	def __init__(self, initial_state=None, α=.1, β=.1, γ=14):
		super().__init__(initial_state)
		# Define coefficients for α, β, and γ by the passed in values
		print(f"Rossler Coefficients: α={α}, β={β}, γ={γ}")
		self.α = α 
		self.β = β
		self.γ = γ

	"""
	Computes the Rossler system derivatives dx, dy, and dz given
	the state x, y, z.
	This is found from the system definition:
	dx/dt = -y -z
	dy/dt = x + αy
	dz/dt = β + z(x - γ)
	"""
	def compute_derivatives(self, state):
		x, y, z = state
  
		dx = -y - z
		dy = x + self.α * y
		dz = self.β + z * (x - self.γ)

		return np.array([dx, dy, dz])

	def jacobian(self, state):
		x, y, z = state
		J = np.array([
        [0, -1, -1],
        [1, self.α, 0],
        [z, 0, x - self.γ]
		])
		return J