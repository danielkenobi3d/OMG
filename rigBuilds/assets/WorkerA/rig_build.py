from OMG.rigBuilds.assets.WorkerA.custom_rig import rigBiped
import pymel.core as pm
import importlib
from OMG.rigBuilds.assets.WorkerA.custom_rig import controls_dictionary

importlib.reload(rigBiped)


def custom_source():
    pm.rename('Worker_grp', 'geo')


def custom_rig():
    pm.parentConstraint('C_main00_head_sknjnt', 'C_fk01_jaw_grp', mo=True)
    controls_dictionary.rename()

def build_biped_rig():
    rig_biped = rigBiped.RigByped()
    rig_biped.build()
    pm.parent('geo', 'rig')
    pm.parent('environment', 'rig')


