import pymel.core as pm


list_of_locators = pm.ls('locator*', type='transform')


for each in list_of_locators:
    transform_cube, creation_cube = pm.polyCube(w=2)
    pm.matchTransform(transform_cube, each)
