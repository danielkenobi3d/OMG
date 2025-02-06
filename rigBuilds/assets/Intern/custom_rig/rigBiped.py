from RMPY.rig.biped.rig import arm
from RMPY.rig.biped.rig import rigForwardBackwardFKSpine
from RMPY.rig.biped.rig import hand
from RMPY.rig import rigFK
from RMPY.rig.biped.rig import rig_jaw
from RMPY.rig import rigWorld
from RMPY.rig.biped.rig import neckHead
from RMPY.rig.biped.rig import rigIKFKLegFeet
from RMPY.rig import rigBase
from RMPY.rig import rigProp
from RMPY.rig.biped.rig import armSpaceSwitch
from RMPY.rig.biped.rig import legSpaceSwitch
from RMPY.rig.biped.rig import handSpaceSwitch
from RMPY.rig.biped.rig import rigEyesAim
from RMPY.rig.biped.rig import rigBreast
from RMPY.rig.biped.rig import rigToes
from RMPY.rig.biped.rig import neckHeadSpaceSwitch
from RMPY.rig.biped.rig import rigEyesSpaceSwitch
from RMPY.rig import rigSingleJoint
from RMPY.rig import rigOutput


class RigBypedModel(rigBase.BaseModel):
    def __init__(self, **kwargs):
        super(RigBypedModel, self).__init__(**kwargs)
        self.l_arm = arm.Arm()
        self.r_arm = arm.Arm()
        self.l_hand = hand.Hand()
        self.r_hand = hand.Hand()
        self.l_arm_space_switch = armSpaceSwitch.ArmSpaceSwitch()
        self.r_arm_space_switch = armSpaceSwitch.ArmSpaceSwitch()
        self.l_hand_space_switch = handSpaceSwitch.HandSpaceSwitch()
        self.r_hand_space_switch = handSpaceSwitch.HandSpaceSwitch()
        self.l_rig_output = rigOutput.RigOutput()
        self.r_rig_output = rigOutput.RigOutput()


class RigByped(rigBase.RigBase):
    def __init__(self, *args, **kwargs):
        super(RigByped, self).__init__(*args, **kwargs)
        self._model = RigBypedModel()

        self.arm_root = [u'{}_clavicle01_reference_pnt', u'{}_arm01_reference_pnt', u'{}_elbow01_reference_pnt',
                         u'{}_wrist01_reference_pnt']

        self.hand_root = [u'{}_palm01_reference_pnt']

    @property
    def l_arm(self):
        return self._model.l_arm

    @property
    def r_arm(self):
        return self._model.r_arm

    @property
    def l_hand(self):
        return self._model.l_hand

    @property
    def r_hand(self):
        return self._model.r_hand

    @property
    def l_arm_space_switch(self):
        return self._model.l_arm_space_switch

    @property
    def r_arm_space_switch(self):
        return self._model.l_arm_space_switch

    @property
    def l_hand_space_switch(self):
        return self._model.l_hand_space_switch

    @property
    def r_hand_space_switch(self):
        return self._model.r_hand_space_switch


    def build(self):
        self.l_arm.create_point_base(*[each.format('L') for each in self.arm_root])
        self.l_arm.set_parent('shoulder_bind_JNT', create_hierarchy_joints=False)

        self.r_arm.create_point_base(*[each.format('R') for each in self.arm_root])
        self.r_arm.set_parent('shoulder_bind_JNT', create_hierarchy_joints=False)

        self.l_hand.create_point_base(*[each.format('L') for each in self.hand_root])
        self.l_hand.set_parent(self.l_arm, create_hierarchy_joints=False)

        self.l_arm_space_switch.build(self.l_arm, self.rig_world, self.cog)
        self.l_hand_space_switch.build(self.l_hand, self.rig_world, self.l_arm)

        self.r_hand.create_point_base(*[each.format('R') for each in self.hand_root])
        self.r_hand.set_parent(self.r_arm, create_hierarchy_joints=False)

        self.r_arm_space_switch.build(self.r_arm, self.rig_world, self.cog)
        self.r_hand_space_switch.build(self.r_hand, self.rig_world, self.r_arm)



if __name__ == '__main__':
    rig_biped = RigByped()
    rig_biped.build()








