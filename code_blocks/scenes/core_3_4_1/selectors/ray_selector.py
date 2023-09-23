
def ray_selector(obj, start_point, direction_vector, max_distance=1000.0, marker=True, marker_name = "?"):
    """
    Find the first face of an object that intersects with a ray originating from a given point using bmesh.
    
    Args:
    - obj (bpy.types.Object): The target object to test for intersections.
    - start_point (mathutils.Vector): The starting point of the ray.
    - direction_vector (mathutils.Vector): The direction of the ray.
    - max_distance (float): Maximum distance the ray should be tested. Default is 1000 units.
    
    Returns:
    - int: Index of the intersected face. Returns None if no intersection is found.
    """
    
    print("Ray cast selector on object with " + str(len(obj.data.polygons)) + " polygons")
    
    
    direction_vector = mathutils.Vector((direction_vector))
    
    # Ensure the object has a mesh with polygons
    if obj.type != 'MESH' or len(obj.data.polygons) == 0:
        return None
    
    # Create a bmesh from the object
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    bm.transform(obj.matrix_world)  # transform the bmesh by the object's world matrix

    # Create a BVH Tree from the bmesh for efficient ray casting
    bvh = mathutils.bvhtree.BVHTree.FromBMesh(bm)
    
    # Cast the ray
    hit = bvh.ray_cast(start_point, direction_vector, max_distance)
    
    bm.free()  # always free the bmesh after using it
    
    if hit:        
        location, normal, face_index, _ = hit
        print("Ray hit : " + str(face_index))
        
        if marker:
            if marker_name == "?":                
                marker_name = generate_unique_id() 
            
            attach_marker(obj, face_index, marker_name)
        else:
            marker_name = None
            
        return face_index, marker_name
    
    return None, None
