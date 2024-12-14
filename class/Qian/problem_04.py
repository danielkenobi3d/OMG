import pymel.core as pm


def create_triangle_1(offset_x=0, offset_y=0):
    steps = 5
    for index_y in range(steps):
        for index_x in range(steps - index_y):
            transform, pcube = pm.polyCube()
            pcube.width.set(.5)
            pcube.height.set(.5)
            pcube.depth.set(.5)
            transform.translateY.set(index_y + offset_y)
            transform.translateX.set(index_x + offset_x)


def create_triangle_2(offset_x=0, offset_y=0):
    steps = 5
    for index_y in range(steps):
        for index_x in range(steps - index_y):
            transform, pcube = pm.polyCube()
            pcube.width.set(.5)
            pcube.height.set(.5)
            pcube.depth.set(.5)
            transform.translateY.set(-index_y + offset_y)
            transform.translateX.set(index_x + offset_x)


def create_triangle_3(offset_x=0, offset_y=0):
    steps = 5
    for index_y in range(steps):
        for index_x in range(steps - index_y):
            transform, pcube = pm.polyCube()
            pcube.width.set(.5)
            pcube.height.set(.5)
            pcube.depth.set(.5)
            transform.translateY.set(index_y + offset_y)
            transform.translateX.set(-index_x + offset_x)


def create_triangle_4(offset_x=0, offset_y=0):
    steps = 5
    for index_y in range(steps):
        for index_x in range(steps - index_y):
            transform, pcube = pm.polyCube()
            pcube.width.set(.5)
            pcube.height.set(.5)
            pcube.depth.set(.5)
            transform.translateY.set(-index_y + offset_y)
            transform.translateX.set(-index_x + offset_x)


create_triangle_1(offset_x=-5, offset_y=0)
create_triangle_2(offset_x=-5, offset_y=9)
create_triangle_3(offset_x=4, offset_y=0)
create_triangle_4(offset_x=4, offset_y=9)

