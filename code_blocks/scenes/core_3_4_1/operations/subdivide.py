import bpy
def subdivide_object(obj, subdivisions=1, smoothness=0):
    """
    Subdivide a given Blender object.
    
    Args:
    - obj (bpy.types.Object): The object to be subdivided.
    - subdivisions (int): The number of subdivisions. Default is 1.
    - smoothness (float): The smoothness of the subdivisions. Ranges from 0 (sharp) to 1 (smooth). Default is 0.
    
    Returns:
    - bpy.types.Object: The subdivided object.
    """
    
    # Ensure the object is selected and set as the active object
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    
    # Enter edit mode
    bpy.ops.object.mode_set(mode='EDIT')
    
    # Select all faces
    bpy.ops.mesh.select_all(action='SELECT')
    
    # Apply the subdivision with smoothness
    bpy.ops.mesh.subdivide(number_cuts=subdivisions, smoothness=smoothness)
    
    # Return to object mode
    bpy.ops.object.mode_set(mode='OBJECT')
    
    return obj
