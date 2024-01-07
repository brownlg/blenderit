import bpy

def merge_overlapping_vertices(obj, merge_distance=0.001):
    """
    Merge overlapping vertices of an object.

    Args:
    - obj (bpy.types.Object): The object to merge vertices.
    - merge_distance (float): Maximum distance between vertices to merge. Default is 0.001.
    """
    
    # Ensure the object is a mesh
    if obj.type != 'MESH':
        print("Object is not a mesh.")
        return

    # Make sure the object is in edit mode
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')

    # Select all vertices
    bpy.ops.mesh.select_all(action='SELECT')

    # Merge vertices by distance
    bpy.ops.mesh.remove_doubles(threshold=merge_distance)

    # Return to object mode
    bpy.ops.object.mode_set(mode='OBJECT')

# Example usage
# obj = bpy.context.object  # The object to update
# merge_overlapping_vertices(obj, merge_distance=0.001)
