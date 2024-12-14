import pymel.core as pm

creations = pm.ls('polyCube*')
selection = pm.ls('pCube*', type='transform')

print(pm.objectType(creations[0]), '\n')

for each in zip(creations, transforms):
    each.width.set(5)