import maya.cmds as cmds

def create_triangle_pattern(size, positionX=0, positionY=0):
    cubes = []
    for row in range(size):
        for col in range(size - row):
            cube = cmds.polyCube(name=f"cube_{row}_{col}")[0]
            cmds.xform(cube, ws=True, t=[positionX + col + row, positionY + row, 0])
            cubes.append(cube)

    for cube in cubes:
        pos = cmds.xform(cube, q=True, ws=True, t=True)
        cmds.xform(cube, ws=True, t=[pos[0] + 1, pos[1], pos[2]])

    finalGroup = cmds.group(cubes, name="finalGroup")
    cmds.xform(finalGroup, piv=[0, size, 0], ws=True)

    for i in range(3):
        copy = cmds.duplicate(finalGroup, name="tempGroup")[0]
        cmds.rotate(0, 0, 90*(i+1), copy, ws=True)
        cmds.makeIdentity(copy, apply=True, t=True, r=True, s=True, n=False)
        children = cmds.listRelatives(copy, children=True, type='transform')
        if children:
            cmds.parent(children, finalGroup)
        cmds.delete(copy)

    return finalGroup

create_triangle_pattern(4)
