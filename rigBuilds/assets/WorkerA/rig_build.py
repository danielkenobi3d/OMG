from OMG.rigBuilds.assets.Intern.custom_rig import rigBiped
import pymel.core as pm


def custom_source():
    pm.rename('Worker_grp', 'geo')

    


def build_biped_rig():
    rig_biped = rigBiped.RigByped()
    rig_biped.build()
    pm.parent('geo', 'rig')
    pm.parent('environment', 'rig')


