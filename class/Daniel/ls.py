import pymel.core as pm
root_points = pm.ls('L_test00_reference_grp')[0]
print(root_points.getChildren())



import maya.cmds as cmds
root_points = cmds.ls('L_test00_reference_grp')[0]
print(cmds.listRelatives(root_points, children=True))