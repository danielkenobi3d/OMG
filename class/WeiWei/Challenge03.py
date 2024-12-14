import pymel.core as pm


def triangle(InitialPositionX, InitialPositionY):
    for position_y in range(4):
        for each in range(4-position_y):
            transform_cube, creation_cube = pm.polyCube()
            transform_cube.translateY.set(creation_cube.width.get()*position_y + InitialPositionY)
            transform_cube.translateX.set(creation_cube.width.get()*each + InitialPositionX)

triangle(0,0)












#for each in range(4):
    #transform_cube, creation_cube = pm.polyCube()
    #transform_cube.translateY.set(creation_cube.width.get()*0)
    #transform_cube.translateX.set(creation_cube.width.get()*each)

#for each in range(5,8):
    #transform_cube, creation_cube = pm.polyCube()

    #transform_cube.translateY.set(creation_cube.width.get() * each - 4)

#for each in range(3):
    #transform_cube, creation_cube = pm.polyCube()
    #transform_cube.translateY.set(creation_cube.width.get()*1)
    #transform_cube.translateX.set(creation_cube.width.get()*each)

#for each in range(2):
    #transform_cube, creation_cube = pm.polyCube()
    #transform_cube.translateY.set(creation_cube.width.get()*2)
    #transform_cube.translateX.set(creation_cube.width.get()*each)

#for each in range(1):
    #transform_cube, creation_cube = pm.polyCube()
    #transform_cube.translateY.set(creation_cube.width.get()*3)
    #transform_cube.translateX.set(creation_cube.width.get()*each)