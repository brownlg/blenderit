def pattern_selector(obj, pattern_start_point_center, selection_size, direction_vector, pattern=['x..', '.x.', '..x'], max_distance=1000.0, marker=True):
    """
    Create a list of face indexes hit by rays originating from points defined by the pattern.
    
    Args:
    obj (bpy.types.Object): The object to test rays against.
    pattern_start_point_center (tuple): Center point for the pattern.
    selection_size (tuple): Dimensions of the pattern (width, height).
    direction_vector (tuple): Direction of the rays.
    pattern (list of str): A list where each string represents a row of rays. 'x' marks where a ray originates.
    max_distance (float): Maximum distance for the rays.
    
    Returns:
    list: List of face indexes hit by the rays.
    """
    
    # Initialize list to store face indexes
    face_indexes = []
    
    # Convert tuples to vectors
    center = mathutils.Vector(pattern_start_point_center)
    #direction = mathutils.Vector(direction_vector)
    
    # Calculate spacing based on the selection size and pattern dimensions
    row_count = len(pattern)
    col_count = len(pattern[0])
    dx = selection_size[0] / (col_count - 1)
    dy = selection_size[1] / (row_count - 1)
    
    marker_names = []
    
    # Loop through the pattern and calculate start points for rays
    for i, row in enumerate(pattern):
        for j, cell in enumerate(row):
            if cell == 'x':
                # Calculate the offset from the center for this ray
                offset = mathutils.Vector((dx * j - selection_size[0] / 2, dy * i - selection_size[1] / 2, 0))
                
                # Calculate the start point for this ray
                start_point = center + offset
                print(start_point)
                
                # Call the ray_selector function to get the face index
                face_index, marker_name = ray_selector(obj, start_point, direction_vector, max_distance, marker)
                
                if marker_name is not None:
                    marker_names.append(marker_name)
                
                # Append to list if we hit a face
                if face_index is not None:
                    face_indexes.append(face_index)
    
    return face_indexes, marker_names


