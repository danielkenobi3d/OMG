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


def import_geometry():
    env = environment.Environment()
    pm.importFile(env.get_latest_version(modelling=True))

def import_reference_points():
    for each in data_save_load.available_maya_files():
        data_save_load.import_maya_file(each)

def custom_rig():

    #Create the FK_Rig
    def FKrig_robot() :
        list_objects_FK = pm.ls('C_robot0*', type='transform')
        jnt_list_FK = []
        ctrl_list_FK = []
        incr = 0

        for locator in list_objects_FK:
            position = locator.getTranslation(space='world')
            new_joint = pm.joint(position=position)
            jnt_list_FK.append(new_joint)

        for jnt in jnt_list_FK :
            pm.rename(jnt, newname=f"robot_FK'{incr}_jnt")
            incr= incr +1

        FK_jnt_grp = pm.group('robot_FK_0_jnt', name='FK_jnt_grp')

        incr = 0
        previous_control = None
        for jnt in jnt_list_FK:
            new_ctrl, create = pm.circle()
            pm.matchTransform(new_ctrl, jnt)
            ctrl_list_FK.append(new_ctrl)
            pm.parentConstraint(new_ctrl, jnt, mo=True)

            if not previous_control:
                pm.rename(previous_control, newname='FK_ctrl_0')
                FK_ctrl_grp = pm.group('FK_ctrl_0', name='FK_ctrl_grp')
            else:
                control_reset = pm.group(empty=True, name=f"controlReset_0{incr}")
                pm.matchTransform(control_reset, new_ctrl)
                pm.parent(new_ctrl, control_reset)
                pm.parent(control_reset, previous_control)
                pm.rename(new_ctrl, newname=f"robot_FK'{incr}_ctrl")

            #new_ctrl.offsetParentMatrix.set(new_ctrl.matrix.get())
            #new_ctrl.translate.set(0,0,0)
            #new_ctrl.rotate.set(0, 0, 0)
            #new_ctrl.scale.set(1, 1 , 1)

            previous_control = new_ctrl
            incr = incr+1
        pm.group(FK_jnt_grp,FK_ctrl_grp, n='FK_rig')

    def IKrig_robot():
        list_objects_IK = pm.ls('C_robot0*', type='transform')
        jnt_list_IK = []
        incr = 0

        for locator in list_objects_IK:
            position = locator.getTranslation(space='world')
            new_joint = pm.joint(position=position)
            jnt_list_IK.append(new_joint)

        for jnt in jnt_list_IK:
            pm.rename(jnt, newname=f"robot_IK'{incr}_jnt")
            incr = incr + 1

        IK_jnt_grp = pm.group('robot_IK_0_jnt', name='IK_jnt_grp')

        ik_handle = pm.ikHandle(sj='robot_IK_1_jnt', ee='robot_IK_4_jnt', sol="ikRPsolver", name="LimbIKHandle")

        #Create elbow_ctrl
        elbow_ctrl, create = pm.circle()
        pm.matchTransform(elbow_ctrl, 'C_robot_reference_pnt_elbow')
        pm.parent('C_robot_reference_pnt_elbow',elbow_ctrl)
        pm.rename(elbow_ctrl,newname='IK_elbow_ctrl')

        pm.poleVectorConstraint('C_robot_reference_pnt_elbow', 'LimbIKHandle', name="PoleVector")

        IK_ctrl, create = pm.circle()
        pm.matchTransform(IK_ctrl, 'robot_IK_4_jnt')
        pm.rename(IK_ctrl,newname='IK_ctrl')
        pm.parent('LimbIKHandle', IK_ctrl)
        IK_ctrl_grp = pm.group('IK_elbow_ctrl','IK_ctrl', n='IK_ctrl_grp')
        pm.makeIdentity('IK_elbow_ctrl',apply=True, t=0, r=0, s=1)

        IK_rig_grp = pm.group(IK_jnt_grp,IK_ctrl_grp, n='IK_rig')


    def IKFK_switch():
        IKFK_switch_ctrl, create = pm.circle()
        pm.matchTransform(IKFK_switch_ctrl,'IK_elbow_ctrl')
        pm.rename(IKFK_switch_ctrl, newname='IKFK_switch_ctrl')
        pm.makeIdentity(IKFK_switch_ctrl, apply = True)
        pm.move(3,3,0, IKFK_switch_ctrl)
        pm.addAttr(IKFK_switch_ctrl, shortName='IKFK_switch', longName='IKFK_switch', minValue=0, maxValue=10)

        pm.createNode('floatConstant')
        pm.createNode('reverse')
        pm.createNode('multiply1')
        pm.createNode('multiply2')
        pm.setAttr('floatConstant.InFloat', 0.1)

        pm.connectAttr('IKFK_switch_ctrl.ikFKswitch', 'multiply1.input[1]')
        pm.connectAttr('IKFK_switch_ctrl.ikFKswitch', 'multiply2.input[1]')
        pm.connectAttr('floatConstant.OutFloat', 'multiply1.input[0]')
        pm.connectAttr('floatConstant.OutFloat', 'multiply2.input[0]')
        pm.connectAttr('multiply2.Output', 'reverse.input[x]')



    FKrig_robot()
    IKrig_robot()
    IKFK_switch()




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


