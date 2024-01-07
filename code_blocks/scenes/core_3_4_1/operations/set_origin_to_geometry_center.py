def set_origin_to_geometry_center(obj):
    """
    Set an object's origin to the center of its geometry using Blender's built-in function.

    Args:
    - obj (bpy.types.Object): The object to update.
    """

    # Ensure the object is a mesh and is the active object
    if obj.type != 'MESH':
        print("Object is not a mesh.")
        return

    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

    # Set the origin to the center of geometry
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')

    # Deselect the object
    obj.select_set(False)

# Example usage
# obj = bpy.context.object  # The object to update
# set_origin_to_geometry_center(obj)
