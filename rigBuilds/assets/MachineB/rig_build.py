from builder.pipeline import environment
from builder.pipeline.mgear import io
from RMPY.core import data_save_load
from RMPY.core import search_hierarchy
from RMPY.core import controls
import pymel.core as pm
from pathlib import Path
from OMG.rigBuilds.assets.default_character import rig_facial


def import_geometry():
    env = environment.Environment()
    pm.importFile(env.get_latest_version(modelling=True))

def import_reference_points():
    for each in data_save_load.available_maya_files():
        data_save_load.import_maya_file(each)

def custom_rig():

    #Create the FK_Rig
    #gets the list of locators
    list_objects = pm.ls('C_robot0*', type='transform')
    joint_group = pm.group(empty=True, name='Joints_Group')
    jnt_list = []

    ctrl_group = pm.group(empty=True, name='ctrl_Group')
    ctrl_list = []

    previous_control = None
    previous_jnt = None


    for locator in list_objects:
        position = locator.getTranslation(space='world')
        new_joint = pm.joint(position=position, name="joint_" + locator)
        jnt_list.append(new_joint)

        if not previous_jnt:
            new_group = pm.group(new_joint)
            pm.parent(new_group, joint_group)

        previous_jnt = new_joint

    for jnt in jnt_list:
        pm.group(jnt)
        new_ctrl, create = pm.circle()
        pm.matchTransform(new_ctrl, jnt)
        ctrl_list.append(new_ctrl)
        pm.parentConstraint(new_ctrl, jnt, mo=True)

        if not previous_control:
            pm.parent(new_ctrl, ctrl_group)
        else:
            # control_reset = pm.group(empty=True, name='controlReset')
            # pm.matchTransform(control_reset, new_ctrl)
            # pm.parent(new_ctrl, control_reset)
            # pm.parent(control_reset, previous_control)
            new_ctrl.offsetParentMatrix.set(new_ctrl.matrix.get())
            new_ctrl.translate.set(0,0,0)
            new_ctrl.rotate.set(0, 0, 0)
            new_ctrl.scale.set(1, 1 , 1)

        previous_control = new_ctrl



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


