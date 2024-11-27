from RMPY.rig import  rigFK
import pymel.core as pm
root_point = pm.ls('C_main00_reference_grp')[0]
my_rig_fk = rigFK.RigFK()
my_rig_fk.create_point_base(*root_point.getChildren())