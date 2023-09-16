def delete_all_objects():
    """
    Delete all objects in the current Blender scene.
    """
    if bpy.context.scene.objects:
        # Ensure the mode is set to 'OBJECT'
        bpy.ops.object.mode_set(mode='OBJECT')
        
        # Deselect all objects first
        bpy.ops.object.select_all(action='DESELECT')
        
        # Select all objects in the scene
        bpy.ops.object.select_all(action='SELECT')
        
        # Delete the selected objects
        bpy.ops.object.delete()
