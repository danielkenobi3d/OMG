import pymel.core as pm


def cube_replace():
    je_comprends_pas_python = pm.ls('locator* ', type='transform')

    for locator in je_comprends_pas_python:
        cube, creation = pm.polyCube()
        pm.matchTransform(cube, locator)
        pm.delete(locator)


cube_replace()