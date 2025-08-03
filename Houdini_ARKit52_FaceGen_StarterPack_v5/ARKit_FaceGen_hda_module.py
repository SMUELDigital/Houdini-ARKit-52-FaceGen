
# This is the PythonModule section inside the ARKit_FaceGen.hda

import hou
import arkit_shape_generator

def generate_all_blendshapes(node):
    try:
        geo_node = node.node("INPUT")  # expected input subnode
        if geo_node:
            arkit_shape_generator.generate_arkit_blendshapes(geo_node)
            hou.ui.displayMessage("ARKit 52 blendshapes generated successfully.")
        else:
            hou.ui.displayMessage("Input node not found.")
    except Exception as e:
        hou.ui.displayMessage(f"Error during blendshape generation: {str(e)}")
