from operator import index

import pymel.core as pm
import math

SinCubes = []
CosCubes = []
for each in range(60):
    SinCubes.append(pm.polyCube()[0])
    CosCubes.append(pm.polyCube()[0])

amplitude = 5
phase = 0  # math.pi
offset = 0
samples_number = 20
resolution_a = math.pi / samples_number  # this value is in degrees
resolution_x = 10 / samples_number  # this value is in maya units
math.sin(math.radians(90))

for index, sample_loc in enumerate(SinCubes):
    sample_loc.translateX.set(resolution_x * index)
    y_position = amplitude * math.sin(resolution_a * index + phase) + offset
    sample_loc.translateY.set(y_position)

    sample_loc.scaleX.set(0.3)
    y_scale = amplitude * math.sin(resolution_a * index + phase) + offset
    sample_loc.scaleY.set(y_scale)

for index, sample_loc in enumerate(CosCubes):
    sample_loc.translateX.set(resolution_x * index)
    y_position = amplitude * math.cos(resolution_a * index + phase) + offset
    sample_loc.translateY.set(y_position)

    sample_loc.scaleX.set(0.3)
    y_scale = amplitude * math.cos(resolution_a * index + phase) + offset
    sample_loc.scaleY.set(y_scale)