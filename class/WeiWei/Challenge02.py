import pymel.core as pm
import random



for each in range(15):
    transform_cube, creation_cube = pm.polyCube(w=2)

    pm.move(transform_cube, random.randrange(0,10), random.randrange(0,10), random.randrange(0,10), moveXYZ=True)

    #transform_cube.translateX.set(random.randrange(0,10))
    #transform_cube.translateY.set(random.randrange(0,10))
    #transform_cube.translateZ.set(random.randrange(0,10))


#my_cube01 = pm.ls('pCube*')[0]
#print(my_cube01)