def bevel_object_edges(obj, bevel_width=0.1):
    """
    Bevel the edges of a given object.
    
    Args:
    - obj (bpy.types.Object): The object to be beveled.
    - bevel_width (float): The width of the bevel. Default is 0.1.
    
    Returns:
    - bpy.types.Object: The beveled object.
    """
    
    # Ensure the mode is set to 'OBJECT'
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Ensure the object is selected and set as the active object
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    
    # Enter edit mode
    bpy.ops.object.mode_set(mode='EDIT')
    
    # Select all edges
    bpy.ops.mesh.select_all(action='SELECT')
    
    # Apply the bevel
    bpy.ops.mesh.bevel(offset=bevel_width)
    
    # Return to object mode
    bpy.ops.object.mode_set(mode='OBJECT')
    
    return obj
