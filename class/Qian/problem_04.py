import pymel.core as pm


def create_joint_from_locators():
    input_group = pm.group(empty=True, name="joint_grp")
    list_of_locators = pm.ls('locator*', type='transform')

    previous_joint= None
    for each in list_of_locators:
        print(each)
        transform_joint = pm.joint()
        pm.matchTransform(transform_joint, each)
        if previous_joint:
            pm.parent(transform_joint, previous_joint)
            previous_joint = transform_joint

def create_controls_from_locators(list_of_locators):
    controls_group = pm.group(empty=True, name="ctl_grp")

    list_of_joints = pm.ls('joint*')

    previous_control= None
    for each, joint_name in zip(list_of_locators, list_of_joints):
        print(each)
        transform_ctl, create_circle = pm.circle()
        pm.matchTransform(transform_ctl, each)
        if not previous_control:
            pm.parent(transform_ctl, controls_group)
        else:
            pm.parent(transform_ctl, previous_control)

        pm.parentConstraint(transform_ctl, joint_name, mo=True)
        previous_control = transform_ctl

create_joint_from_locators()

list_of_locators = pm.ls('locator*', type='transform')
create_controls_from_locators(list_of_locators)