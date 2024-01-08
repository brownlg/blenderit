import bpy

def cleanup_mesh(obj, merge_distance=0.001, angle_limit=0.02):
    """
    Clean up a mesh object using Blender's built-in functions.

    Args:
    - obj (bpy.types.Object): The mesh object to clean up.
    - merge_distance (float): The maximum distance between vertices to be merged. Defaults to 0.001.
    """

    if obj.type != 'MESH':
        print("Object is not a mesh.")
        return

    # Switch to object mode and ensure the object is active and selected
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='OBJECT')
    obj.select_set(True)

    # Enter edit mode
    bpy.ops.object.mode_set(mode='EDIT')

    # Merge vertices by distance
    bpy.ops.mesh.remove_doubles(threshold=merge_distance)

    # Limited dissolve to clean up unnecessary vertices and edges
    bpy.ops.mesh.dissolve_limited(angle_limit=angle_limit)
    
    # Delete loose parts (isolated vertices and edges)
    bpy.ops.mesh.delete_loose()
    
    bpy.ops.mesh.dissolve_faces(use_verts=False)
    bpy.ops.mesh.dissolve_edges(use_verts=True, use_face_split=True)


    # Return to object mode
    bpy.ops.object.mode_set(mode='OBJECT')

# Example usage
# obj = bpy.context.object  # The object to clean up after boolean operation
# cleanup_mesh(obj, merge_distance=0.001)
