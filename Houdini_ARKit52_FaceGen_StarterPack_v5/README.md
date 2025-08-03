# Houdini ARKit 52 FaceGen Plugin

## Files
- `ARKit_FaceGen.hda`: Main digital asset for blendshape generation
- `arkit_shape_generator.py`: Python logic for procedural deformations
- `arkit_shape_list.json`: ARKit 52 shape definitions
- `tongue_rig.bgeo.sc`: Tongue mesh with rig (FK bones)
- `example_scene.hip`: Houdini project with everything wired


## Tongue Rig Info
- FK rig with 3 bones: `tongue_root`, `tongue_mid`, `tongue_tip`
- Ready to be bound to geometry and exported via FBX.