import pymel.core as pm

def hextech_01 (taille, positionX=0, positionY=0):
    for y in range(taille):
        for x in range(taille-y):
            cube, shape = pm.polyCube()
            pm.move(cube,x+positionX,y+positionY,0)

def hextech_02 (taille, positionX=8, positionY=8):
    for y in range(taille):
        for x in range(taille-y):
            cube, shape = pm.polyCube()
            pm.move(cube,-x+positionX,-y+positionY,0)

def hextech_03 (taille, positionX=0, positionY=8):
    for y in range(taille):
        for x in range(taille-y):
            cube, shape = pm.polyCube()
            pm.move(cube,x+positionX,-y+positionY,0)


def hextech_04 (taille, positionX=8, positionY=0):
    for y in range(taille):
        for x in range(taille-y):
            cube, shape = pm.polyCube()
            pm.move(cube,-x+positionX,y+positionY,0)

hextech_01(4)
hextech_02(4)
hextech_03(4)
hextech_04(4)