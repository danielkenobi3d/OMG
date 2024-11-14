import pymel.core as pm
from RMPY.rig import rigLaceRing
from RMPY.rig import rigFK
root_points = pm.ls('R_laceRing00_reference_grp')[0]

test_rig = rigFK.RigFK()
test_rig.create_point_base(*root_points.getChildren())

test_rig = rigLaceRing.LaceRing()
test_rig.create_point_base(*root_points.getChildren(), joint_number=20,
                           create_path_surface=True,
                           nurbs_to_poly_output=True,
                           curve_distance=2)
