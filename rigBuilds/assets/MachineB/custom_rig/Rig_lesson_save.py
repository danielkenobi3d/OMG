import pymel.core as pm
from RMPY.rig import rigBase
controls = ['nurbsCircle1', 'nurbsCircle2', 'nurbsCircle3', 'nurbsCircle4', 'nurbsCircle5']
ik_handle = pm.ikHandle(sj= , ee=, sol="ikRPsolver", name="LimbIKHandle")
pm.poleVectorConstraint(self.controls_dict['poleVector'], ik_handle, name="PoleVector")
my_rig = rigBase.RigBase()

my_rig.create.group.point_base(controls)

pm.makeIdentity( , apply=True, t=0, r=1, s=0)
pm.createNode('reverse')
pm.createNode('floatConstant')
pm.connectAttr('nurbsCircle6.ikFKswitch','multiply2.input[1]')
inFloat


# Create the FK_Rig
def FKrig_robot():
    list_objects_FK = pm.ls('C_robot0*', type='transform')
    jnt_list_FK = []
    ctrl_list_FK = []
    incr = 0

    for locator in list_objects_FK:
        position = locator.getTranslation(space='world')
        new_joint = pm.joint(position=position)
        jnt_list_FK.append(new_joint)

    for jnt in jnt_list_FK:
        pm.rename(jnt, newname=f"robot_FK'{incr}_jnt")
        incr = incr + 1

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

        # new_ctrl.offsetParentMatrix.set(new_ctrl.matrix.get())
        # new_ctrl.translate.set(0,0,0)
        # new_ctrl.rotate.set(0, 0, 0)
        # new_ctrl.scale.set(1, 1 , 1)

        previous_control = new_ctrl
        incr = incr + 1
    pm.group(FK_jnt_grp, FK_ctrl_grp, n='FK_rig')
    return jnt_list_FK


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

    # Create elbow_ctrl
    elbow_ctrl, create = pm.circle()
    pm.matchTransform(elbow_ctrl, 'C_robot_reference_pnt_elbow')
    pm.parent('C_robot_reference_pnt_elbow', elbow_ctrl)
    pm.rename(elbow_ctrl, newname='IK_elbow_ctrl')

    pm.poleVectorConstraint('C_robot_reference_pnt_elbow', 'LimbIKHandle', name="PoleVector")

    IK_ctrl, create = pm.circle()
    pm.matchTransform(IK_ctrl, 'robot_IK_4_jnt')
    pm.rename(IK_ctrl, newname='IK_ctrl')
    pm.parent('LimbIKHandle', IK_ctrl)
    IK_ctrl_grp = pm.group('IK_elbow_ctrl', 'IK_ctrl', n='IK_ctrl_grp')
    pm.makeIdentity('IK_elbow_ctrl', apply=True, t=0, r=0, s=1)

    IK_rig_grp = pm.group(IK_jnt_grp, IK_ctrl_grp, n='IK_rig')


def resultjnt(jnt_list_FK):
    list_objects_result = pm.ls('C_robot0*', type='transform')
    jnt_list_result = []
    incr = 0

    for locator in list_objects_result:
        position = locator.getTranslation(space='world')
        new_joint = pm.joint(position=position)
        jnt_list_result.append(new_joint)
    for jnt in jnt_list_result:
        pm.rename(jnt, newname=f"robot_result'{incr}_jnt")
        incr = incr + 1

    result_jnt_grp = pm.group('robot_result_0_jnt', name='result_jnt_grp')
    incr = 0
    for each in jnt_list_result:
        pm.parentConstraint(each, jnt_list_FK[incr])
        incr = incr + 1


def IKFK_switch():
    IKFK_switch_ctrl, create = pm.circle()
    pm.matchTransform(IKFK_switch_ctrl, 'IK_elbow_ctrl')
    pm.rename(IKFK_switch_ctrl, newname='IKFK_switch_ctrl')
    pm.makeIdentity(IKFK_switch_ctrl, apply=True)
    pm.move(3, 3, 0, IKFK_switch_ctrl)
    pm.addAttr(IKFK_switch_ctrl, shortName='IKFK_switch', longName='IKFK_switch', minValue=0, maxValue=10)

    floatConstant = pm.createNode('floatConstant')
    reverse = pm.createNode('reverse')
    multiply1 = pm.createNode('multiply', name='multiply1', )
    multiply2 = pm.createNode('multiply', name='multiply2')
    pm.setAttr(floatConstant.inFloat, 0.1)

    # pm.connectAttr(IKFK_switch_ctrl.IKFK_switch, multiply1.input[1])
    IKFK_switch_ctrl.IKFK_switch >> multiply1.input[1]
    pm.connectAttr(IKFK_switch_ctrl.IKFK_switch, multiply2.input[1])
    pm.connectAttr(floatConstant.outFloat, multiply1.input[0])
    pm.connectAttr(floatConstant.outFloat, multiply2.input[0])
    pm.connectAttr(multiply2.output, reverse.inputX)


fk_list = FKrig_robot()
IKrig_robot()
resultjnt()
IKFK_switch()

