#problem_02
import pymel.core as pm
import random

for each in range(20):
    print(each)
    transform_cube, creation_node = pm.polyCube()
    pm.move(transform_cube, random.random() * 20, random.random() * 20, random.random() * 20, moveXYZ=True)