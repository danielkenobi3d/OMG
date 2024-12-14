import pymel.core as pm

list_of_locators = pm.ls('locator*', type='transform')

for each in list_of_locators:
    print(each)
    transform_cube, creation_node = pm.polyCube()
    pm.matchTransform(transform_cube, each)

