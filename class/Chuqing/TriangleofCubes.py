#replace object
import pymel.core as pm

list_of_Locators = pm.ls('locator*', type='transform')

for each in list_of_Locators:
       transform_circle, creation_node = pm.circle()
       pm.matchTransform(transform_circle, each)

#random position
import pymel.core as pm
import random

for each in range(20):
      random_X = random.randrange(0, 10)
      random_Y = random.randrange(0, 10)
      random_Z = random.randrange(0, 10)
      transform_cube, creation_node = pm.polyCube()
      transform_cube_random = pm.move(transform_cube, random_X, random_Y, random_Z, moveXYZ=True, relative=True, objectSpace=True)

#triangle cubes
import pymel.core as pm
steps = 10
for index_Y in range(steps):
    for index_X in range(steps):
        transform_cubes, cube_creation = pm.polyCube()
        transform_cubes.translateX.set(index_X)
        transform_cubes.translateY.set(index_Y)

list_of_cubes = pm.ls('pCube*', type='transform')




transform_cubes_newX = transform_cubes.translateX.set(add_positionX())
transform_cubes_newY = transform_cubes.translateY.set(20)


#FK rig
import pymel.core as pm

list_of_Locators = pm.ls('locator*', type='transform')

for each in list_of_Locators:
    new_joint = pm.joint()
    pm.matchTransform(new_joint, each)

Joint_group = pm.group(empty=True, n='joint_grp')
pm.parent('joint1', Joint_group)
list_of_joints = pm.ls('joint*', type='transform')

for each in list_of_joints:
    transform_circle, creation_node = pm.circle()
    pm.matchTransform(transform_circle, each)
    pm.parentConstraint(transform_circle, each, mo=True)
    pm.parentConstraint(transform_circle, each, mo=True)

List_of_conrtol = pm.ls('nurbsCircle*', type='transform')

for each in List_of_conrtol:
    control_group = pm.group(empty=True, n='control_grp')
    pm.matchTransform(control_group, each)
    pm.parent(each, control_group)

rig_group = pm.group(empty=True, n='rig')
pm.parent(Joint_group, rig_group)
pm.parent('control_grp', rig_group)

pm.parent('control_grp1', 'nurbsCircle1')
pm.parent('control_grp2', 'nurbsCircle2')
pm.parent('control_grp3', 'nurbsCircle3')
pm.parent('control_grp4', 'nurbsCircle4')
pm.parent('control_grp5', 'nurbsCircle5')
pm.parent('control_grp6', 'nurbsCircle6')
pm.parent('control_grp7', 'nurbsCircle7')
pm.parent('control_grp8', 'nurbsCircle8')
pm.parent('control_grp9', 'nurbsCircle9')

from RMPY import nameConvention
name_conv = nameConvention.NameConvention()
name_conv.default_names['system'] = 'reference'
selection = pm.ls(selection=True)


def rename_selection():
	selection = pm.ls(selection=True)
	fix_shapes(*selection)
	for index, each in enumerate(selection):
		side = 'C'
		system_name = 'rig'
		name = 'joint'
		# name_conv.rename_name_in_format(each, side=side, system=system_name, name='shoe{}'.format(chr(65+index)))
		# name_conv.rename_name_in_format(each, side=side, system=system_name, name='finger{}'.format(chr(65 + index)))
		name_conv.rename_name_in_format(each, side=side, system=system_name, name=name)
		# name_conv.rename_name_in_format(each, side=side, system=system_name, name='muscle')


def set_in_name():
	selection = pm.ls(selection=True)
	for each in selection:
		name_conv.rename_set_from_name(each, 'C', 'side')


def fix_shapes(*scene_object_list):
	for index, each_object in enumerate(scene_object_list):
		each_object.rename('geometry{}'.format(65+index))
		shapes_list = each_object.getShapes()
		object_name = str(each_object).split('|')[-1]
		for each in shapes_list:
			each.rename('{}Shape'.format(object_name))


# set_in_name()
rename_selection()



