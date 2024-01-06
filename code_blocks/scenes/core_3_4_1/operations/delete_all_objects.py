def delete_all_objects():
    """
    Delete all objects in the current Blender scene.
    """
    if bpy.context.selected_objects:
        # Ensure the mode is set to 'OBJECT'
        bpy.ops.object.mode_set(mode='OBJECT')
        
        # Deselect all objects first
        bpy.ops.object.select_all(action='DESELECT')
        
        # Select all objects in the scene
        bpy.ops.object.select_all(action='SELECT')
        
        # Delete the selected objects
        bpy.ops.object.delete()


def delete_except_keep_collection():
    """
    Delete all objects in the current Blender scene except those in the "Keep" collection.
    """
    if bpy.context.scene.objects:
        # Ensure the mode is set to 'OBJECT'
        bpy.ops.object.mode_set(mode='OBJECT')
        
        #Get the "Keep" collection
        keep_collection = bpy.data.collections.get("Keep")
        
        #Get the objects in the "Keep" collection
        keep_objects = set(keep_collection.objects) if keep_collection else set()
        
        #Deselect all objects first
        bpy.ops.object.select_all(action='DESELECT')
        
        # Loop through all objects in the scene and select those not in the "Keep" collection
        flag_found = False
        for obj in bpy.context.scene.objects:
            if obj not in keep_objects:
                obj.select_set(True)
                flag_found = True
        
        # Delete the selected objects
        if flag_found:
            bpy.ops.object.delete()

def hide_objects_in_keep_collection(hide=True):
    """
    Toggle visibility of all objects in the 'Keep' collection.

    Parameters:
    - hide: If True, hide the objects. If False, show the objects.
    """
    
    if bpy.context.scene.objects:
        # Get the "Keep" collection
        keep_collection = bpy.data.collections.get("Keep")
        
        if keep_collection is None:
            print("No 'Keep' collection found.")
            return
        
        # Loop through all objects in the "Keep" collection and set their visibility
        for obj in keep_collection.objects:
            obj.hide_viewport = hide

def delete_object(obj):
    """
    Delete a specified object from the Blender scene.

    Args:
    - obj (bpy.types.Object): The object to be deleted.
    """

    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Select the object
    obj.select_set(True)

    # Set the object as the active object
    bpy.context.view_layer.objects.active = obj

    # Delete the object
    bpy.ops.object.delete()
