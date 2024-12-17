import maya.cmds as cmds

def create_and_align_to_locators():
    base = cmds.polySphere(name="base_sphere", radius=0.5)[0]
    locs = [cmds.listRelatives(loc, parent=True)[0] for loc in cmds.ls(type="locator")]

    for i, loc in enumerate(locs):
        new = cmds.duplicate(base, name=f"sphere_{i}")[0]
        pos = cmds.xform(loc, q=True, ws=True, t=True)
        rot = cmds.xform(loc, q=True, ws=True, ro=True)
        cmds.xform(new, ws=True, t=pos)
        cmds.xform(new, ws=True, ro=rot)

    cmds.delete(base)

create_and_align_to_locators()
