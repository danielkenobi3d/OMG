from OMG.rigBuilds.assets.Intern.custom_rig import rigBiped
from OMG.rigBuilds.assets.Intern.custom_rig import rigArm
import importlib
importlib.reload(rigArm)
import pymel.core as pm


def build_biped_rig():
    rig_arm = rigArm.RigArm()
    rig_arm.build()
    pm.parent('geo', 'rig')
    pm.parent('environment', 'rig')