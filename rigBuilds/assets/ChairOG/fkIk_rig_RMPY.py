from builder.pipeline import environment
from builder.pipeline.mgear import io
from RMPY.core import data_save_load
from RMPY.core import search_hierarchy
from RMPY.core import controls
import pymel.core as pm
from pathlib import Path
from ufe.PyUfe.PathString import string
from RMPY.rig import rigBase


class MyRig(rigBase.RigBase):
    def __init__(self):
        super().__init__()
        self.jnt_list_FK = []
        #self.jnt_list_IK = []
        #self.jnt_list_result = []
        self.ctrl_list_FK = []
        #self.parent_constraints = []

        #self.IK_ctrl = None
        self.FKrig_robot()
        #self.IKrig_robot()
        #self.resultjnt()
        #self.IKFK_switch()


    #Create the FK_Rig
    def FKrig_robot(self) :
        list_objects_FK = pm.ls('C_chair0*', type='transform')
        self.jnt_list_FK = []
        self.ctrl_list_FK = []
        incr = 0

        for locator in list_objects_FK:
            position = locator.getTranslation(space='world')
            new_joint = pm.joint(position=position)
            self.jnt_list_FK.append(new_joint)

        for jnt in self.jnt_list_FK :
            pm.rename(jnt, newname=f"chair_FK'{incr}_jnt")
            incr= incr +1

        FK_jnt_grp = pm.group('chair_FK_0_jnt', name='FK_jnt_grp')

        incr = 0
        previous_control = None
        for jnt in self.jnt_list_FK:
            new_ctrl, create = pm.circle()
            pm.matchTransform(new_ctrl, jnt)
            self.ctrl_list_FK.append(new_ctrl)
            pm.parentConstraint(new_ctrl, jnt, mo=True)

            if not previous_control:
                pm.rename(previous_control, newname='chair_ctrl_0')
                FK_ctrl_grp = pm.group('chair_ctrl_0', name='FK_ctrl_grp')
            else:
                control_reset = pm.group(empty=True, name=f"controlReset_0{incr}")
                pm.matchTransform(control_reset, new_ctrl)
                pm.parent(new_ctrl, control_reset)
                pm.parent(control_reset, previous_control)
                pm.rename(new_ctrl, newname=f"chair_FK'{incr}_ctrl")

            #new_ctrl.offsetParentMatrix.set(new_ctrl.matrix.get())
            #new_ctrl.translate.set(0,0,0)
            #new_ctrl.rotate.set(0, 0, 0)
            #new_ctrl.scale.set(1, 1 , 1)

            previous_control = new_ctrl
            incr = incr+1
        pm.parent(FK_jnt_grp, self.rig_system.joints)
        pm.parent(FK_ctrl_grp, self.rig_system.controls)

        # pm.group(FK_jnt_grp,FK_ctrl_grp, n='FK_rig')

    def IKrig_robot(self):
        list_objects_IK = pm.ls('C_robot0*', type='transform')
        self.jnt_list_IK = []
        incr = 0

        for locator in list_objects_IK:
            position = locator.getTranslation(space='world')
            new_joint = pm.joint(position=position)
            self.jnt_list_IK.append(new_joint)

        for jnt in self.jnt_list_IK:
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

        self.IK_ctrl, create = pm.circle()
        pm.matchTransform(self.IK_ctrl, 'robot_IK_4_jnt')
        pm.rename(self.IK_ctrl,newname='IK_ctrl')
        pm.parent('LimbIKHandle', self.IK_ctrl)
        IK_ctrl_grp = pm.group('IK_elbow_ctrl','IK_ctrl', n='IK_ctrl_grp')

        # IK_rig_grp = pm.group(IK_jnt_grp,IK_ctrl_grp, n='IK_rig')
        pm.parent(IK_jnt_grp, self.rig_system.joints)
        pm.parent(IK_ctrl_grp, self.rig_system.controls)

        pm.makeIdentity('IK_elbow_ctrl', apply = True, t=True, r=True, s=True)

        pm.makeIdentity('IK_ctrl',apply = True, t=True, r=True, s=True)


    def resultjnt(self):
        list_objects_result = pm.ls('C_robot0*', type='transform')
        self.jnt_list_result  = []
        incr = 0

        for locator in list_objects_result:
            position = locator.getTranslation(space='world')
            new_joint = pm.joint(position=position)
            self.jnt_list_result.append(new_joint)
        for jnt in self.jnt_list_result:
            pm.rename(jnt, newname=f"robot_result'{incr}_jnt")
            incr = incr + 1

        result_jnt_grp = pm.group(name='result_jnt_grp', empty=True)
        pm.parent('robot_result_0_jnt', result_jnt_grp)
        pm.parent(result_jnt_grp, self.rig_system.joints)


        for fk_joint, ik_joint, result_jnt in zip(self.jnt_list_FK, self.jnt_list_IK, self.jnt_list_result):
            pm.parentConstraint(fk_joint, result_jnt)
            parent_constraint = pm.parentConstraint(ik_joint, result_jnt)
            self.parent_constraints.append(parent_constraint)

    def IKFK_switch(self):
        IKFK_switch_ctrl, create = pm.circle()
        pm.parent(IKFK_switch_ctrl, self.rig_system.controls)
        pm.matchTransform(IKFK_switch_ctrl,'IK_elbow_ctrl')
        pm.rename(IKFK_switch_ctrl, newname='IKFK_switch_ctrl')
        pm.makeIdentity(IKFK_switch_ctrl, apply = True)
        pm.move(3,3,0, IKFK_switch_ctrl)
        pm.makeIdentity(IKFK_switch_ctrl, apply = True)
        pm.addAttr(IKFK_switch_ctrl, shortName='IKFK_switch', longName='IKFK_switch', minValue=0, maxValue=10, keyable=True)
        pm.addAttr(IKFK_switch_ctrl, shortName='FK_vis', longName='FK_vis', minValue=0, maxValue=10, keyable=True)
        pm.addAttr(IKFK_switch_ctrl, shortName='IK_vis', longName='IK_vis', minValue=0, maxValue=10, keyable=True)

        floatConstant = pm.createNode('floatConstant')
        reverse = pm.createNode('reverse')
        multiply1=pm.createNode('multiply', name= 'multiply1',)
        multiply2 = pm.createNode('multiply', name= 'multiply2')
        pm.setAttr(floatConstant.inFloat, 0.1)

        # pm.connectAttr(IKFK_switch_ctrl.IKFK_switch, multiply1.input[1])
        IKFK_switch_ctrl.IKFK_switch >> multiply1.input[1]
        IKFK_switch_ctrl.IKFK_switch >> multiply2.input[1]
        floatConstant.outFloat >> multiply1.input[0]
        floatConstant.outFloat >> multiply2.input[0]
        multiply2.output >> reverse.inputX

        for each_parent_constraint in self.parent_constraints:
            weights = each_parent_constraint.getWeightAliasList()

            multiply1.output >> weights[1]
            reverse.outputX >> weights[0]

        pm.setDrivenKeyframe('IK_ctrl_grp.visibility',cd =IKFK_switch_ctrl.IK_vis, dv=0, v=False)
        pm.setDrivenKeyframe('IK_ctrl_grp.visibility',cd =IKFK_switch_ctrl.IK_vis, dv=10, v=True)
        pm.setDrivenKeyframe('FK_ctrl_grp.visibility',cd =IKFK_switch_ctrl.FK_vis, dv=0, v=False)
        pm.setDrivenKeyframe('FK_ctrl_grp.visibility',cd =IKFK_switch_ctrl.FK_vis, dv=10, v=True)

        pm.setDrivenKeyframe(IKFK_switch_ctrl.IK_vis, cd = IKFK_switch_ctrl.IKFK_switch, dv=0, v=0)
        pm.setDrivenKeyframe(IKFK_switch_ctrl.IK_vis, cd = IKFK_switch_ctrl.IKFK_switch, dv=10, v=10)
        pm.setDrivenKeyframe(IKFK_switch_ctrl.FK_vis, cd = IKFK_switch_ctrl.IKFK_switch, dv=10, v=0)
        pm.setDrivenKeyframe(IKFK_switch_ctrl.FK_vis, cd = IKFK_switch_ctrl.IKFK_switch, dv=0, v=10)

if __name__ == '__main__':
    robot_rig = my_rig()
    print(robot_rig.jnt_list_result)
    print(robot_rig.ctrl_list_FK)

    

