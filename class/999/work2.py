import pymel.core as pm
import random

def create_random_objects(count=10, max_x=10, max_y=10, shape='cube'):
    for each in range(count):
        obj = pm.polyCube()[0]

        x = random.randrange(0, max_x)
        y = random.randrange(0, max_y)

        pm.move(obj, x, y, 0, moveXYZ=True)

        rotation = random.random() * 360
        pm.rotate(obj, 0, rotation, 0)

if __name__ == '__main__':
    create_random_objects(20, 20, 20)