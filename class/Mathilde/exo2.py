import pymel.core as pm
import random


def random_cube():
    for each in range(5):
        square_limit_x = random.randrange(0, 10)
        square_limit_y = random.randrange(0, 10)
        square_limit_z = random.randrange(0, 10)

        cube_creation, creation = pm.polyCube()
        pm.move(cube_creation, square_limit_x, square_limit_y, square_limit_z, moveXYZ=True, relative=True,
                objectSpace=True)


random_cube()
