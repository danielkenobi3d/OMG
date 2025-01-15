prefix_geometry_list = []

definition = dict(
    jaw=dict(
        type='blend_shape_definition',
        isSymetrical=False,
        baseMesh='character',
        control='C_facial00_mouth_ctr',
        blendShapes=dict(midOpen={'connection': 'jawOpen', 'value': 5},
                         fullOpen={'connection': 'jawOpen', 'value': 10},
                         puffFront={'connection': 'jawOpen', 'value': -10},
                         mouthLeft={'connection': 'mouthLR', 'value': 10},
                         mouthRight={'connection': 'mouthLR', 'value': -10},
                         upperLipPucker={'connection': 'upperLipRollInOut', 'value': 10},
                         upperLipLipsIn={'connection': 'upperLipRollInOut', 'value': -10},
                         lowLipPucker={'connection': 'lowLipRollInOut', 'value': 10},
                         lowLipLipsIn={'connection': 'lowLipRollInOut', 'value': -10},
                         kiss={'connection': 'wideNarrow', 'value': -10},
                         bucinator={'connection': 'wideNarrow', 'value': 10},
                         jawForward={'connection': 'jawForwardBackward', 'value': 10},
                         jawBackward={'connection': 'jawForwardBackward', 'value': -10},
                         upperLipUp={'connection': 'upperLipUp', 'value': 10},
                         lowLipDwn={'connection': 'lowLipDown', 'value': 10},
                         fullSmileLipUp={'connection': 'fullSmileLipUp', 'value': 10},
                         fullSmile={'connection': 'fullSmile', 'value': 10}
                         ),
        attributes=dict(jawOpen={'type': 'float', 'min': 0, 'max': 10},
                        mouthLR={'type': 'float', 'min': -10, 'max': 10},
                        upperLipRollInOut={'type': 'float', 'min': -10, 'max': 10},
                        lowLipRollInOut={'type': 'float', 'min': -10, 'max': 10},
                        wideNarrow={'type': 'float', 'min': -10, 'max': 10},
                        jawForwardBackward={'type': 'float', 'min': -10, 'max': 10},
                        upperLipUp={'type': 'float', 'min': 0, 'max': 10},
                        lowLipDown={'type': 'float', 'min': 0, 'max': 10},
                        fullSmileLipUp={'type': 'float', 'min': 0, 'max': 10},
                        fullSmile={'type': 'float', 'min': 0, 'max': 10}
                        ),
        order=['jawOpen', 'mouthLR', 'upperLipRollInOut', 'lowLipRollInOut', 'wideNarrow', 'jawForwardBackward',
               'upperLipUp', 'lowLipDown', 'fullSmileLipUp', 'fullSmile']
        ),

)
eyes_dict = dict(
    eyes=dict(
        type='blend_shape_definition',
        isSymetrical=True,
        baseMesh='character',
        control='L_aim00_eye_grp',
        blendShapes=dict(LlookLeft={'connection': 'rotateY', 'value': 18},
                         LlookRight={'connection': 'rotateY', 'value': -18},
                         LlookUp={'connection': 'rotateZ', 'value': 18},
                         LlookDwn={'connection': 'rotateZ', 'value': -18},
                         ),
        attributes=dict(rotateY={'type': 'float', 'min': -18, 'max': 18},
                        rotateZ={'type': 'float', 'min': -18, 'max': 18},),
        order=['rotateY', 'rotateZ']
    )
)

correctives_dict = dict(
        jawCorrectives=dict(
            type='blend_shape_definition',
            isSymetrical=False,
            baseMesh='character',
            control='C_joint00_jaw_ctr',
            blendShapes=dict(jawOpen={'connection': 'rotateZ', 'value': 12}),
            attributes=dict(rotateZ={'type': 'float', 'min': 0, 'max': 10}),
            order=['rotateZ']
            ),
)

direct_blendshape = { }
# 'character': 'C_BOD_Y001_HIGH'

jaw_layer = ['character']


if __name__ == '__main__':
    import pymel.core as pm
    selection_list=[]
    for each_dictionary in [definition, eyes_dict]:
        for each_setup in each_dictionary.keys():
            for each_blendshape in each_dictionary[each_setup]['blendShapes'].keys():
                if not pm.objExists(each_blendshape):
                    print ('{} not found'.format(each_blendshape))
                if not pm.ls(each_blendshape)[0].getParent().name() == 'blendshapes':
                    selection_list.append(each_blendshape)
    pm.select(selection_list)


