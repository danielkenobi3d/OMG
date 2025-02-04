import pymel.core as pm
rename_controls_dict = {
    'C_fk00_Spine_ctr':'C_joint00_Spine_ctr',
    'C_fk00_head_ctr':'C_joint00_head_ctr',
    'C_fk00_neck_ctr':'C_joint00_neck_ctr',
    'C_fk01_Spine_ctr':'C_joint01_Spine_ctr',
    'C_fk02_Spine_ctr':'C_joint02_Spine_ctr',
    'C_fk03_Spine_ctr':'C_joint03_Spine_ctr',
    'L_fk00_ankleFeet_ctr':'L_joint00_ankleFeet_ctr',
    'L_fk00_arm_ctr':'L_joint00_arm_ctr',
    'L_fk00_leg_ctr':'L_joint00_leg_ctr',
    'L_fk01_ankleFeet_ctr':'L_joint01_ankleFeet_ctr',
    'L_fk01_arm_ctr':'L_joint01_arm_ctr',
    'L_fk01_leg_ctr': 'L_joint01_leg_ctr',
    'L_ikIK00_arm_ctr': 'L_jointIK00_arm_ctr',
    'L_ikIK00_leg_ctr': 'L_jointIK00_leg_ctr',
    'L_ikPoleVectorIK00_arm_ctr':'L_jointPoleVectorIK00_arm_ctr',
    'L_ikPoleVectorIK00_leg_ctr':'L_jointPoleVectorIK00_leg_ctr',
    'R_fk00_ankleFeet_ctr':'R_joint00_ankleFeet_ctr',
    'R_fk00_arm_ctr':'R_joint00_arm_ctr',
    'R_fk00_leg_ctr':'R_joint00_leg_ctr',
    'R_fk01_ankleFeet_ctr':'R_joint01_ankleFeet_ctr',
    'R_fk01_arm_ctr':'R_joint01_arm_ctr',
    'R_fk01_leg_ctr':'R_joint01_leg_ctr',
    'R_ikIK00_arm_ctr':'R_jointIK00_arm_ctr',
    'R_ikIK00_leg_ctr': 'R_jointIK00_leg_ctr',
    'R_ikPoleVectorIK00_arm_ctr':'R_jointPoleVectorIK00_arm_ctr',
    'R_ikPoleVectorIK00_leg_ctr':'R_jointPoleVectorIK00_leg_ctr',
}

not_found_controls = ['C_fk00_rig_ctr', 'C_object00_cap_ctr', 'C_object00_glass_ctr', 'C_object01_cap_ctr', 'C_object01_glass_ctr', 'C_root00_eyes_ctr',
 'L_aim00_eye_ctr', 'L_fk00_ear_ctr', 'L_fk01_ear_ctr','L_fk02_ear_ctr', 'L_fk03_ear_ctr', 'R_aim00_eye_ctr', 'R_fk00_ear_ctr',  'R_fk01_ear_ctr','R_fk02_ear_ctr', 'R_fk03_ear_ctr']

def rename():
    for each in rename_controls_dict:
        pm.rename(each, rename_controls_dict[each])
