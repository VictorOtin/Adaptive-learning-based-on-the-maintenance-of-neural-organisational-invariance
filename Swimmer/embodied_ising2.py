import numpy as np
from itertools import combinations
import matplotlib.pyplot as plt
from swimmer import SwimmerEnv


class ising:
	# Initialize the network
	def __init__(self, netsize, Nsensors=1, Nmotors=1):  # Create ising model

		self.size = netsize		#Network size
		self.Ssize = Nsensors  # Number of sensors
		self.Msize = Nmotors  # Number of sensors

		self.h = np.zeros(netsize)
		self.J = np.zeros((netsize, netsize))
		self.max_weights = 2

		self.randomize_state()

		self.env = SwimmerEnv()
		self.env.goal_position = 1.5 * np.pi / 3
		self.env.max_speed = .045
		self.observation = self.env.reset()
		#self.max_angle_j0 = -0.61 #-35º 
		#self.min_angle_j0 = -1.39 #-80º
		self.max_angle_j0 = -1
		self.min_angle_j0 = -1

		self.Beta = 1.0
		self.defaultT = max(100, netsize * 20)

		self.Ssize1 = 0
		#self.maxspeed = self.env.max_speed
		self.Update(-1)

	def get_state(self, mode='all'):
		if mode == 'all':
			return self.s
		elif mode == 'motors':
			return self.s[-self.Msize:]
		elif mode == 'sensors':
			return self.s[0:self.Ssize]
		elif mode == 'input':
			return self.sensors
		elif mode == 'non-sensors':
			return self.s[self.Ssize:]
		elif mode == 'hidden':
			return self.s[self.Ssize:-self.Msize]

	def get_state_index(self, mode='all'):
		return bool2int(0.5 * (self.get_state(mode) + 1))

	# Randomize the state of the network
	def randomize_state(self):
		self.s = np.random.randint(0, 2, self.size) * 2 - 1
		self.sensors = np.random.randint(0, 2, self.Ssize) * 2 - 1

	# Randomize the position of the agent
	def randomize_position(self):
		self.observation = self.env.reset()

	# Set random bias to sets of units of the system
	def random_fields(self, max_weights=None):
		if max_weights is None:
			max_weights = self.max_weights
		self.h[self.Ssize:] = max_weights * \
			(np.random.rand(self.size - self.Ssize) * 2 - 1)

	# Set random connections to sets of units of the system
	def random_wiring(self, max_weights=None):  # Set random values for h and J
		if max_weights is None:
			max_weights = self.max_weights
		for i in range(self.size):
			for j in np.arange(i + 1, self.size):
				if i < j and (i >= self.Ssize or j >= self.Ssize):
					self.J[i, j] = (np.random.rand(1) * 2 - 1) * self.max_weights

	# Update the position of the agent
	def Move(self):
		action = self.s[-self.Msize:]
#		print(action)
		observation, reward, done, info = self.env.step(action)
		#print(action, self.s[-self.Msize:],observation)

	# Transorm the sensor input into integer index
	def SensorIndex(self, x, xmax):
		if abs(x)>xmax:
			medida = 15
		else:
			medida = int(np.floor((x + xmax) / (2 * xmax + 10 *
                                	    np.finfo(float).eps) * 2**(self.Ssize/6)))
		return medida

	# Update the state of the sensor
	def UpdateSensors(self):
		self.speed_x = self.SensorIndex(self.env.sim.data.qvel[0,]/self.env.vmaxbody , self.env.vmaxbody*1.3) 
		self.sensors[0:2] = 2 * bitfield(self.speed_x, int(self.Ssize/8)) - 1
		self.speed_y = self.SensorIndex(self.env.sim.data.qvel[1,]/self.env.vmaxbody , self.env.vmaxbody*1.3) 
		self.sensors[2:4] = 2 * bitfield(self.speed_y, int(self.Ssize/8)) - 1
#		self.speed_ind_leg2_j0 = self.SensorIndex(self.env.joints[2].speed/self.env.vmaxhip , self.env.vmaxhip*1.3)
#		self.sensors[8:12] = 2 * bitfield(self.speed_ind_leg2_j0, int(self.Ssize/6)) - 1
#		self.speed_ind_leg2_j1 = self.SensorIndex(self.env.joints[3].speed/self.env.vmaxknee , self.env.vmaxknee*1.3)
#		self.sensors[12:16] = 2 * bitfield(self.speed_ind_leg2_j1, int(self.Ssize/6)) - 1
#		self.hull_height = self.SensorIndex(self.env.hull.position[0] , 500)
#		self.sensors[16:20] = 2 * bitfield(self.hull_height, int(self.Ssize/6)) - 1
#		self.hull_vel = self.SensorIndex(self.env.hull.linearVelocity[0] , 5)
#		self.sensors[20:] = 2 * bitfield(self.hull_vel, int(self.Ssize/6)) - 1
		#print(self.sensors)
		self.body_pos_x = self.SensorIndex(self.env.sim.data.qpos[0,] , 20)
		self.sensors[4:6] = 2 * bitfield(self.body_pos_x, int(self.Ssize/8)) - 1
		self.body_pos_y = self.SensorIndex(self.env.sim.data.qpos[1,] , 20)
		self.sensors[6:8] = 2 * bitfield(self.body_pos_y, int(self.Ssize/8)) - 1
#		print(self.env.sim.data.qpos[0,], self.env.sim.data.qpos[1,])

	# Execute step of the Glauber algorithm to update the state of one unit
	def GlauberStep(self, i=None): 
		if i is None:
			i = np.random.randint(self.size)

		I = 0
		if i < self.Ssize:
			I = self.sensors[i]

		eDiff = 2 * self.s[i] * (self.h[i] + I +
		                         np.dot(self.J[i, :] + self.J[:, i], self.s))
		if eDiff * self.Beta < np.log(1 / np.random.rand() - 1):    # Glauber
			self.s[i] = -self.s[i]

	# Update random unit of the agent
	def Update(self, i=None):
		if i is None:
			i = np.random.randint(-1, self.size)
		if i == -1:
			self.Move()
			self.UpdateSensors()
		else:
			self.GlauberStep(i)

	# Sequentially update state of all units of the agent in random order
	def SequentialUpdate(self):
		for i in np.random.permutation(range(-1, self.size)):
			self.Update(i)

	# Step of the learning algorith to ajust correlations to the critical regime
	def AdjustCorrelations(self, T=None):
		if T is None:
			T = self.defaultT

		self.m = np.zeros(self.size)
		self.c = np.zeros((self.size, self.size))
		self.C = np.zeros((self.size, self.size))

		# Main simulation loop:
		self.x = np.zeros(T)
		samples = []
		for t in range(T):

			self.SequentialUpdate()
			#self.x[t] = self.position
			self.m += self.s
			for i in range(self.size):
				self.c[i, i + 1:] += self.s[i] * self.s[i + 1:]
		self.m /= T
		self.c /= T
		for i in range(self.size):
			self.C[i, i + 1:] = self.c[i, i + 1:] - self.m[i] * self.m[i + 1:]

		c1 = np.zeros((self.size, self.size))
		for i in range(self.size):
			inds = np.array([], int)
			c = np.array([])
			for j in range(self.size):
				if not i == j:
					inds = np.append(inds, [j])
				if i < j:
					c = np.append(c, [self.c[i, j]])
				elif i > j:
					c = np.append(c, [self.c[j, i]])
			order = np.argsort(c)[::-1]
			c1[i, inds[order]] = self.Cint[i, :]
		self.c1 = np.triu(c1 + c1.T, 1)
		self.c1 *= 0.5


		self.m[0:self.Ssize] = 0
		self.m1[0:self.Ssize] = 0
		self.c[0:self.Ssize, 0:self.Ssize] = 0
		self.c[-self.Msize:, -self.Msize:] = 0
		self.c[0:self.Ssize, -self.Msize:] = 0
		self.c1[0:self.Ssize, 0:self.Ssize] = 0
		self.c1[-self.Msize:, -self.Msize:] = 0
		self.c1[0:self.Ssize, -self.Msize:] = 0
		dh = self.m1 - self.m
		dJ = self.c1 - self.c
		#print(self.m1,self.m)
		#print("dh, dJ:",dh,",",dJ)
		return dh, dJ

	# Algorithm for poising an agent in a critical regime
	def CriticalLearning(self, Iterations, T=None):
		u = 0.01
		count = 0
		dh, dJ = self.AdjustCorrelations(T)
		fit = max(np.max(np.abs(self.c1 - self.c)), np.max(np.abs(self.m1 - self.m)))

		for it in range(Iterations):
			count += 1
			self.h += u * dh
			self.J += u * dJ
			#print(self.h,self.J)
			if it % 10 == 0:
				self.randomize_state()
				self.randomize_position()
			Vmax = self.max_weights
			for i in range(self.size):
				if np.abs(self.h[i]) > Vmax:
					self.h[i] = Vmax * np.sign(self.h[i])
				for j in np.arange(i + 1, self.size):
					if np.abs(self.J[i, j]) > Vmax:
						self.J[i, j] = Vmax * np.sign(self.J[i, j])

			dh, dJ = self.AdjustCorrelations(T)
			fit = np.max(np.abs(self.c1 - self.c))
			#if count % 1 == 0:
			#	print(self.env.hull.position[0],self.env.hull.linearVelocity[0])
			#	mid = (self.env.max_position + self.env.min_position) / 2
				# print(				self.size,
    #                                 count,
    #                                 fit,
    #                                 np.mean(np.abs(self.J)),
    #                                 np.max(np.abs(self.J)),
    #                                 (np.min(self.x) - mid) / np.pi * 3,
    #                                 (np.max(self.x) - mid) / np.pi * 3)


# Transform bool array into positive integer
def bool2int(x):
    y = 0
    for i, j in enumerate(np.array(x)[::-1]):
        y += j * 2**i
    return int(y)

# Transform positive integer into bit array
def bitfield(n, size):
    x = [int(x) for x in bin(int(n))[2:]]
    x = [0] * (size - len(x)) + x
    return np.array(x)
