from builder.pipeline import environment
from builder.pipeline.mgear import io
from RMPY.core import data_save_load
from RMPY.core import search_hierarchy
from RMPY.core import controls
import pymel.core as pm
from pathlib import Path
from OMG.rigBuilds.assets.default_character import rig_facial
from ufe.PyUfe.PathString import string
from RMPY.rig import rigBase
from OMG.rigBuilds.assets.MachineB import fkIk_rig
from OMG.rigBuilds.assets.MachineB import fkIk_rig_RMPY
import importlib
importlib.reload(fkIk_rig)
importlib.reload(fkIk_rig_RMPY)

def import_geometry():
    env = environment.Environment()
    pm.importFile(env.get_latest_version(modelling=True))

def import_reference_points():
    for each in data_save_load.available_maya_files():
        data_save_load.import_maya_file(each)

def custom_rig():
    # robot_rig = fkIk_rig.my_rig()
    robot_rig = fkIk_rig_RMPY.MyRig()

def load_skinning_data():
    env = environment.Environment()
    root_node = pm.ls('geo', '*_GEO_GRP')[0]
    print(root_node)
    list_of_objects = search_hierarchy.shape_type_in_hierarchy(root_node)
    for each in list_of_objects:
        if Path(f'{env.data}/skinClusters/{each}.json').exists():
            data_save_load.load_skin_cluster(each)


def load_shapes_data():
    env = environment.Environment()
    controls_shapes = pm.ls('*_ctr', type='transform')
    print(controls_shapes)
    for each in controls_shapes:
        try:
            if Path(f'{env.data}/nurbsCurves/{each}.json').exists():
                data_save_load.load_curves(each)
        except:
            print(f'an error ocurred loading {each}')
    controls.color_now_all_ctrls()


def cleanup():
    all_root_nodes = pm.ls('|*', lockedNodes=False)
    for each in all_root_nodes:
        if str(each) not in ['persp', 'top', 'front', 'side', 'rig']:
            if str(each) in ['environment', 'geo']:
                each.setParent('rig')
            else:
                pm.delete(each)
    for each in pm.ls('*_settings*_pnt'):
        each.visibility.set(False)


def custom_finalize():
    pass


if __name__ == '__main__':
    load_shapes_data()


