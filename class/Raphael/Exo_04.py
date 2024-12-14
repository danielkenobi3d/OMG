import pymel.core as pm
from pymel.core.animation import joint

je_comprends_un_peu_mieux_python = pm.ls('locator* ', type='transform')
joint_group = pm.group(empty=True, name = 'Joints_group')
jnt_list = []

for locator in je_comprends_un_peu_mieux_python:
    new_joint = pm.joint(name = 'joint_'+locator)
    pm.matchTransform(new_joint,locator)
    jnt_list.append(new_joint)
    pm.delete(locator)

for joints in jnt_list :
    control,shape = pm.circle()
    pm.matchTransform(control,joints)
    pm.parentConstraint(control,joints, mo=True)
