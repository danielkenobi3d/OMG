import pymel.core as pm
import math

locators = []
for each in range(60):
    locators.append(pm.spaceLocator())
amplitud = 2
phase = 0  # math.pi
offset = 0
samples_number = 20
resolution_a = math.pi / samples_number  # this value is in degrees
resolution_x = 10 / samples_number  # this value is in maya units
math.sin(math.radians(90))

for index, sample_loc in enumerate(locators):
    sample_loc.translateX.set(resolution_x * index)
    y_position = amplitud * math.sin(resolution_a * index + phase) + offset
    sample_loc.translateY.set(y_position)

