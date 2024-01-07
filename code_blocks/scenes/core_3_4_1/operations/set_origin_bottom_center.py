import bpy
import bmesh
from mathutils import Vector

def set_origin_to_bottom_center(obj):
    """
    Set an object's origin to the bottom center of its geometry.

    Args:
    - obj (bpy.types.Object): The object to update.
    """

    # Ensure the object is a mesh and is the active object
    if obj.type != 'MESH':
        print("Object is not a mesh.")
        return

    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

    # Create a bmesh from the object's mesh data
    mesh = obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)

    # Calculate the lowest Z coordinate and the average X and Y coordinates
    lowest_z = min([v.co.z for v in bm.verts])
    avg_x = sum([v.co.x for v in bm.verts]) / len(bm.verts)
    avg_y = sum([v.co.y for v in bm.verts]) / len(bm.verts)

    # Set the origin to the calculated point
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.mode_set(mode='OBJECT')
    obj.location = obj.matrix_world.inverted() @ Vector((avg_x, avg_y, lowest_z))

    # Set the origin to the cursor
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

    # Deselect the object
    obj.select_set(False)

    # Free the bmesh
    bm.free()

# Example usage
# obj = bpy.context.object  # The object to update
# set_origin_to_bottom_center(obj)
