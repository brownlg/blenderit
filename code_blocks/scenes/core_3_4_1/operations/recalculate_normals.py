import bpy

def recalculate_normals(obj):
    """
    Recalculate the normals of a mesh object, making them point outward.

    Args:
    - obj (bpy.types.Object): The mesh object to recalculate normals.
    """

    # Ensure the object is a mesh
    if obj.type != 'MESH':
        print("Object is not a mesh.")
        return

    # Switch to object mode to ensure the operation applies correctly
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Select the object
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)

    # Recalculate normals
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.editmode_toggle()

# Example usage
# obj = bpy.context.object  # The object to recalculate normals
# recalculate_normals(obj)
