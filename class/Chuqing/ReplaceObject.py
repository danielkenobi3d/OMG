#replace object
import pymel.core as pm

list_of_Locators = pm.ls('locator*', type='transform')
transform, creation_node = pm.circle()

for each in list_of_Locators:
       transform_circle, creation_node = pm.circle()
       pm.matchTransform(transform_circle, each)

#random position
import pymel.core as pm
import random

for each in range(20):
      random_X = random.randrange(0, 10)
      random_Y = random.randrange(0, 10)
      random_Z = random.randrange(0, 10)
      transform_cube, creation_node = pm.polyCube()
      transform_cube_random = pm.move(transform_cube, random_X, random_Y, random_Z, moveXYZ=True, relative=True, objectSpace=True)

