import pymel.core as pm
import math

cubes = []
for each in range(15):
    cubes.append(pm.polyCube()[0])

amplitud = 13
phase = 0
offset = 1
samples_number = 15
resolution_a = math.pi / 12
resolution_x = 20 / samples_number
math.sin(math.radians(90))

for index, sample_cube in enumerate(cubes):
    sample_cube.translateX.set(resolution_x * index)
    y_height = amplitud * math.sin(resolution_a * index + phase) + offset
    sample_cube.scaleY.set(y_height)
