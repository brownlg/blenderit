def apply_subsurf_modifier(obj, levels=1, render_levels=1, on_cage=False):
    """
    Apply a Subdivision Surface modifier to a given Blender object.
    
    Args:
    - obj (bpy.types.Object): The object to which the modifier should be added.
    - levels (int): Number of subdivisions to use in the viewport. Default is 1.
    - render_levels (int): Number of subdivisions to use when rendering. Default is 1.
    - on_cage (bool): Whether to enable the "On Cage" option. Default is False.
    
    Returns:
    - bpy.types.Object: The object with the Subdivision Surface modifier applied.
    """
    
    # Ensure the object is the active object
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    
    # Add the Subdivision Surface modifier
    subsurf = obj.modifiers.new(name="Subdivision", type='SUBSURF')
    
    # Set the levels for viewport and render
    subsurf.levels = levels
    subsurf.render_levels = render_levels
    
    # Enable or disable the "On Cage" option
    subsurf.show_on_cage = on_cage
    
    return obj