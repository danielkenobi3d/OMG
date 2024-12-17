from RMPY.rig import rigFK
import pymel.core as pm
from RMPY.rig import rigSingleJoint

root_point = pm.ls('C_main00_reference_grp')[0]
my_rig_fk = rigFK.RigFK()
my_rig_fk.create_point_base(*root_point.getChildren())

watch_root = pm.ls('C_watch00_reference_grp')[0]
rig_watch = rigSingleJoint.RigSingleJoint()
rig_watch.create_point_base(*watch_root.getChildren(), static=True)

rig_watch.set_parent(my_rig_fk)
