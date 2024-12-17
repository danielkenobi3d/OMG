import pymel.core as pm

def triangle(size, positionX=0, positionY=0):
    cubes = []
    for row in range(size):
        for col in range(size - row):
            t, c = pm.polyCube()
            t.translateX.set(positionX + col + row)
            t.translateY.set(positionY + row)
            t.translateZ.set(0)
            cubes.append(t)
    return cubes

steps = 4
cubes = triangle(steps)

for cube in cubes:
    cube.translateX.set(cube.translateX.get() + 1)

finalGroup = pm.group(cubes, name="finalGroup")
pm.xform(finalGroup, piv=[0, steps, 0], ws=True)

for i in range(3):
    copy = pm.duplicate(finalGroup, name="tempGroup")[0]
    pm.rotate(copy, 0, 0, 90*(i+1), r=True)
    pm.makeIdentity(copy, apply=True, t=True, r=True, s=True, n=False)
    children = pm.listRelatives(copy, children=True, type='transform')
    pm.parent(children, finalGroup)
    pm.delete(copy)
