# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:34:04 2019

@author: nerguri
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON=255
OFF=0
vals=[ON, OFF]

def update(frameNum, img, grid, N): 

	# copy grid since we require 8 neighbors 
	# for calculation and we go line by line 
	newGrid = grid.copy() 
	for i in range(N): 
		for j in range(N): 

			# compute 8-neghbor sum 
			# using toroidal boundary conditions - x and y wrap around 
			# so that the simulaton takes place on a toroidal surface. 
			total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
						grid[(i-1)%N, j] + grid[(i+1)%N, j] +
						grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
						grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255) 
            
			# apply Conway's rules 
			if grid[i, j] == ON: 
				if (total < 2) or (total > 3): 
					newGrid[i, j] = OFF 
			else: 
				if total == 3: 
					newGrid[i, j] = ON 

	# update data 
	img.set_data(newGrid) 
	grid[:] = newGrid[:] 
	return img, 

N = 100
updateInterval = 50

grid = np.array([])
    
grid = np.zeros(N*N).reshape(N,N)

glider = np.array([[0, 0, 255], 
					[255, 0, 255], 
					[0, 255, 255]]) 
grid[1:1+3, 1:1+3] = glider

fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ), 
								frames = 10, 
								interval=updateInterval, 
								save_count=50) 
# # of frames? 
# set output file 
#if args.movfile: 
#ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264']) 


plt.show()