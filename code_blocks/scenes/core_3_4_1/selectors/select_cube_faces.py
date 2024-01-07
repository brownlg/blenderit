
def select_cube_faces(cube):
    """
    Select all six faces of a scaled and translated cube using ray selection.

    Args:
    - cube (bpy.types.Object): The cube object.

    Returns:
    - dict: A dictionary containing the indices of the top, bottom, front, back, right, and left faces.
    """

    # Get the center location and scale of the cube
    cube_center =  cube.location
    #cube_center =  mathutils.Vector((0,0,3))

    # Calculate the scaled distances from the center to the cube faces along each axis
    # TODO: warning this assumes a small cube
    scaled_distances = mathutils.Vector((900, 900, 900))  # Adding a small value to ensure the ray starts outside the cube

    # Define ray start points and directions for each face, relative to the cube's center and scale
    ray_params = {
        "top": (cube_center + mathutils.Vector((0, 0, scaled_distances.z)), (0, 0, -1)),
        "bottom": (cube_center + mathutils.Vector((0, 0, -scaled_distances.z)), (0, 0, 1)),
        "front": (cube_center + mathutils.Vector((scaled_distances.x, 0, 0)), (-1, 0, 0)),
        "back": (cube_center + mathutils.Vector((-scaled_distances.x, 0, 0)), (1, 0, 0)),
        "right": (cube_center + mathutils.Vector((0, scaled_distances.y, 0)), (0, -1, 0)),
        "left": (cube_center + mathutils.Vector((0, -scaled_distances.y, 0)), (0, 1, 0))
    }

    face_indices = {}

    # Perform ray selection for each face
    for face, (start_point, direction_vector) in ray_params.items():
        face_index = ray_selector(cube, start_point, direction_vector, max_distance=1000.0, marker=True, marker_name=face,debug=False)[0]
        face_indices[face] = face_index

    return face_indices

# Example usage
# cube = bpy.context.object  # Assuming a cube is the active object
# face_indices = select_cube_faces(cube)
# print(face_indices)
