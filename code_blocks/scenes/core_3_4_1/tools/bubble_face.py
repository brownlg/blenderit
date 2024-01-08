import bpy

def add_sphere(parent_obj, location, radius=0.1):
    """
    Add a UV Sphere at a specified location and attach it to a given object.

    Args:
    - parent_obj (bpy.types.Object): The object to which the sphere will be parented.
    - location (tuple or mathutils.Vector): The location to place the sphere.
    - radius (float): The radius of the sphere. Default is 0.1.
    """
    
    # Create a UV Sphere at the specified location
    bpy.ops.mesh.primitive_uv_sphere_add(radius=radius, location=location, segments=15, ring_count=15)
    
    # Get the newly created sphere object
    sphere = bpy.context.object

    # Set the parent of the sphere to the specified object
    sphere.parent = parent_obj

    # Optional: To keep the sphere's transformation local to the parent:
    sphere.matrix_parent_inverse = parent_obj.matrix_world.inverted()

# Example usage
# parent_obj = bpy.context.object  # The object to parent to
# location = (1, 2, 3)  # The location for the sphere
# add_sphere_and_attach_to_object(parent_obj, location, radius=0.1)
