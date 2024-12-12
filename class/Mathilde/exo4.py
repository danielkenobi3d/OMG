import pymel.core as pm


def FK_rig():
    list_objects = pm.ls(selection=True)
    joint_group = pm.group(empty=True, name='Joints_Group')
    jnt_list = []

    for locator in list_objects:
        position = locator.getTranslation(space='world')
        new_joint = pm.joint(position=position, name=locator + "_joint")
        jnt_list.append(new_joint)

    ctrl_group = pm.group(empty=True, name='ctrl_Group')
    ctrl_list = []

    for jnt in jnt_list:
        new_ctrl = pm.circle()
        pm.matchTransform(new_ctrl, jnt)
        ctrl_list.append(new_ctrl)
        pm.parentConstraint(new_ctrl, jnt, mo=True)


FK_rig()


