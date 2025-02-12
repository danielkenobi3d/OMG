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