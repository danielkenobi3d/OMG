import pymel.core as pm
import random

for each in range(10):
    cube, shape =pm.polyCube()
    pm.move(cube, random.randrange(0,20), random.randrange(0,20), random.randrange(0,20), moveXYZ=True, relative=True, objectSpace=True)