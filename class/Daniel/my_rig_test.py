import pymel.core as pm
from RMPY.rig import rigFK
root_points = pm.ls('L_test00_reference_grp')[0]

test_rig = rigFK.RigFK()
test_rig.create_point_base(*root_points.getChildren())

print(test_rig.joints)
print(test_rig.controls)
print(test_rig.rig_system.root)
print(test_rig.rig_system.controls)
print(test_rig.rig_system.joints)
print(test_rig.rig_system.settings)
print(test_rig.rig_system.kinematics)
print(test_rig.rig_system.display)