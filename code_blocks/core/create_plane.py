def create_plane(location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1)):
    """
    Create a plane in Blender with the option to set location, rotation, and scale.
    
    Args:
    - location (tuple): 3D tuple indicating the location of the plane. Default is (0, 0, 0).
    - rotation (tuple): 3D tuple indicating the rotation of the plane in radians. Default is (0, 0, 0).
    - scale (tuple): 3D tuple indicating the scale of the plane. Default is (1, 1, 1).
    
    Returns:
    - bpy.types.Object: The created plane object.
    """
    
    # Create a new plane mesh
    bpy.ops.mesh.primitive_plane_add(location=location, rotation=rotation, scale=scale)
    
    # Return the created plane object
    return bpy.context.active_object

# Usage example:
plane = create_plane(location=(2, 2, 2), scale=(2, 2, 1))
