import pymel.core as pm

control_transform = 'nurbsCircle1'
if not 'y_heigh_Amp' in  pm.listAttr(control_transform):
    pm.addAttr(control_transform, longName='y_heigh_Amp',min=0, max=10,k=True)

for each in ['sin_B_y', 'sin_A_y', 'sin_C_y']:
    pm.connectAttr(f'{control_transform}.y_heigh_Amp', f'{each}.amplitude')

import pymel.core as pm
pm.addAttr('nurbsCircle1', longName='enableSym', proxy='nucleus1.enable')
pm.addAttr('nurbsCircle1', longName='startFrame', proxy='nucleus1.startFrame')



