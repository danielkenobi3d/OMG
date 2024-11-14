from RMPY.core import search_hierarchy
import pymel.core as pm
scene_object = pm.ls(selection=True)[0]
pm.select(search_hierarchy.type_in_hierarchy(scene_object))