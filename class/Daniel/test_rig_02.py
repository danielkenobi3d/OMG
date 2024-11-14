import pymel.core as pm
from RMPY.rig import rigLaces
root_points = pm.ls('L_test00_reference_grp')[0]

test_rig = rigLaces.RigLaces()
# controls_number
test_rig.create_point_base(*root_points.getChildren(), joint_number=20, curve_distance = .5)
