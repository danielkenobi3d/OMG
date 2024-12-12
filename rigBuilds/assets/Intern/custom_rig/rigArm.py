from RMPY.rig.biped.rig import arm
from RMPY.rig.biped.rig import hand
from RMPY.rig import rigBase
# from RMPY.rig.biped.rig import armSpaceSwitch
# from RMPY.rig.biped.rig import handSpaceSwitch
from RMPY.rig import rigOutput


class RigArmModel(rigBase.BaseModel):
    def __init__(self, **kwargs):
        super(RigArmModel, self).__init__(**kwargs)
        self.l_arm = arm.Arm()
        self.r_arm = arm.Arm()
        self.l_hand = hand.Hand()
        self.r_hand = hand.Hand()
        # self.l_arm_space_switch = armSpaceSwitch.ArmSpaceSwitch()
        # self.r_arm_space_switch = armSpaceSwitch.ArmSpaceSwitch()
        # self.l_hand_space_switch = handSpaceSwitch.HandSpaceSwitch()
        # self.r_hand_space_switch = handSpaceSwitch.HandSpaceSwitch()
        self.l_rig_output = rigOutput.RigOutput()
        self.r_rig_output = rigOutput.RigOutput()


class RigArm(rigBase.RigBase):
    def __init__(self, *args, **kwargs):
        super(RigArm, self).__init__(*args, **kwargs)
        self._model = RigArmModel()

        self.arm_root = [u'{}_clavicle01_reference_pnt', u'{}_arm01_reference_pnt', u'{}_elbow01_reference_pnt',
                         u'{}_wrist01_reference_pnt']

        self.leg_root = [u'{}_leg01_reference_pnt', u'{}_Knee01_reference_pnt', u'{}_ankle01_reference_pnt']

        self.fingers = [u'{}_leg01_reference_pnt', u'{}_Knee01_reference_pnt', u'{}_ankle01_reference_pnt',
                        u'{}_ankleFeet01_reference_pnt']
        self.hand_root = [u'{}_palm01_reference_pnt']

    def build(self):
        self.l_arm.create_point_base(*[each.format('L') for each in self.arm_root])
        # self.l_arm.set_parent(self.spine, create_hierarchy_joints=True, output_joint_rig=self.l_rig_output)

        self.r_arm.create_point_base(*[each.format('R') for each in self.arm_root])
        # self.r_arm.set_parent(self.spine, create_hierarchy_joints=True, output_joint_rig=self.r_rig_output)

        self.l_hand.create_point_base(*[each.format('L') for each in self.hand_root])
        self.l_hand.set_parent(self.l_arm, create_hierarchy_joints=True, output_joint_rig=self.l_rig_output)

        # self.l_arm_space_switch.build(self.l_arm, self.rig_world, self.cog)
        # self.l_hand_space_switch.build(self.l_hand, self.rig_world, self.l_arm)

        self.r_hand.create_point_base(*[each.format('R') for each in self.hand_root])
        self.r_hand.set_parent(self.r_arm, create_hierarchy_joints=True, output_joint_rig=self.r_rig_output)


        # self.r_arm_space_switch.build(self.r_arm, self.rig_world, self.cog)
        # self.r_hand_space_switch.build(self.r_hand, self.rig_world, self.r_arm)