import bpy
import bmesh
from mathutils import Vector

def set_origin_to_bottom_center(obj, align = 'bottom'):
    """
    Set an object's origin to the bottom center of its geometry.

    Args:
    - obj (bpy.types.Object): The object to update.
    """

    if obj.type != 'MESH':
        print("Object is not a mesh.")
        return

    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

    # Create a bmesh to access the mesh data
    bm = bmesh.new()
    bm.from_mesh(obj.data)

    # Calculate the lowest Z coordinate and the average X and Y coordinates
    if align == 'top':        
        align_z = max(v.co.z for v in bm.verts)
    else:
        align_z = min(v.co.z for v in bm.verts)
        
    avg_x = sum(v.co.x for v in bm.verts) / len(bm.verts)
    avg_y = sum(v.co.y for v in bm.verts) / len(bm.verts)

    # Define the bottom center position in world space
    bottom_center_world = obj.matrix_world @ Vector((avg_x, avg_y, align_z))

    # Move the 3D cursor to this position
    bpy.context.scene.cursor.location = bottom_center_world

    # Set the origin to the 3D cursor without moving the object
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

    obj.select_set(False)
    bm.free()

# Example usage
# obj = bpy.context.object  # The object to update
# set_origin_to_bottom_center(obj)
