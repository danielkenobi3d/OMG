import pymel.core as pm


def FK_rig():
    list_objects = pm.ls('locator*', type='transform')
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
            pm.parent(new_joint, joint_group)

        previous_jnt = new_joint

    for jnt in jnt_list:
        new_ctrl, create = pm.circle()
        pm.matchTransform(new_ctrl, jnt)
        ctrl_list.append(new_ctrl)
        pm.parentConstraint(new_ctrl, jnt, mo=True)

        if not previous_control:
            pm.parent(new_ctrl, ctrl_group)
        else:
            pm.parent(new_ctrl, previous_control)

        previous_control = new_ctrl
    pm.delete('locator*')


FK_rig()
