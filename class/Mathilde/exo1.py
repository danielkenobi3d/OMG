import pymel.core as pm


def replace():
    list_of_objects = pm.ls(selection=True)

    for locator in list_of_objects:
        new_cube, creation = pm.polyCube()
        pm.matchTransform(new_cube, locator)


replace()
