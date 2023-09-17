def rotate_object(obj, axis, angle_degrees):
    """
    Rotate an object around a specified axis by a certain angle in degrees.
    
    Args:
    - obj (bpy.types.Object): The object to rotate.
    - axis (tuple or list or mathutils.Vector): The axis around which to rotate the object.
    - angle_degrees (float): The angle to rotate by, in degrees.
    """
    # Ensure we're in 'OBJECT' mode
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Convert the angle to radians
    angle_radians = math.radians(angle_degrees)
    
    # Create the rotation matrix
    rot_mat = mathutils.Matrix.Rotation(angle_radians, 4, axis)
    
    # Apply the rotation
    obj.matrix_world = rot_mat @ obj.matrix_world