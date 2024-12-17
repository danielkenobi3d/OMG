import pymel.core as pm


def triangle(size, positionX=0, positionY=0):
    for each_y in range(size):
        for each_x in range(size - each_y):
            cube_create = each_x * pm.polyCube()
            pm.move(each_x + positionX, each_y + positionY, 0)


def triangle2(size, positionX, positionY):
    for each_y in range(size):
        for each_x in range(size - each_y):
            cube_create = each_x * pm.polyCube()
            pm.move(each_x - positionX, -each_y - positionY, 0)


def triangle3(size, positionX, positionY):
    for each_y in range(size):
        for each_x in range(size - each_y):
            cube_create = each_x * pm.polyCube()
            pm.move(-each_x + positionX, -each_y - positionY, 0)


def triangle4(size, positionX, positionY):
    for each_y in range(size):
        for each_x in range(size - each_y):
            cube_create = each_x * pm.polyCube()
            pm.move(-each_x - positionX, each_y + positionY, 0)


triangle(4, 0, 0)
triangle2(4, 0, -8)
triangle3(4, 8, -8)
triangle4(4, -8, 0)