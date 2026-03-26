import numpy as np
import matplotlib.pyplot as plt

"""
The Visualize class is responsible for generating an image of the trajectory using matplotlib.
This is a static image with no animation capabilities.

This has one function for displaying the graph. Technically we could store the simulator
but this is not currently implemented
"""
class Visualize:
	def plot(self, steps, times, trajectory, method_name, dt=None):
		traject_arr = np.array(trajectory)
		x, y, z = traject_arr[:, 0], traject_arr[:, 1], traject_arr[:, 2]
		
		fig = plt.figure()
		ax = fig.add_subplot(projection='3d')
		
		if dt:
			label = f"Method: {method_name} | time: {round(times[-1], 2)}s | timesteps: {steps} | dt = {dt}"
		else:
			label = f"Method: {method_name} | time: {round(times[-1], 2)}s | timesteps: {steps}"
		
		ax.plot(x, y, z, lw=.1, label=label)
		ax.set_title(f"Lorenz Attractor")
		plt.legend()
		
		plt.show()
		

class Animate:
	def animate(self, steps, time, trajectory, method_name):
		pass