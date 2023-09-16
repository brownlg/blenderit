def create_cube(position = (0,0,0)):
    """
    Create a cube in the Blender scene with specified parameters.
    
    Args:
    None
    
    Returns:
    - bpy.types.Object: The created cube object.
    """
    
    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=position)
    
    # Return the active object (which is the cube we just created)
    return bpy.context.active_object
