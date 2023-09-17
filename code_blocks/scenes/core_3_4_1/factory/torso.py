# using only the fn that we created

def torso_calculate_scale(pattern, pattern_size):
    count_x = pattern.count("X")    
    scale_factor = count_x / pattern_size if pattern_size > 0 else 1
    return scale_factor


def sequential_extruder(obj, start_position, xz_patterns, yz_patterns, z_slice_tickness, pattern_size_xz, pattern_size_yz, normal_vector):      
    # Now scale the rest:
    for i in range(len(xz_patterns)-2, -1, -1):  
        print(i)      
        xz_scale = torso_calculate_scale( xz_patterns[i], pattern_size_xz)
        yz_scale = torso_calculate_scale( yz_patterns[i], pattern_size_yz)
        
        relative_xz_scale = xz_scale / prev_xz_scale
        relative_yz_scale = yz_scale / prev_yz_scale
        
        prev_xz_scale = xz_scale
        prev_yz_scale = yz_scale
        
        # Step 1: Use ray select to choose the top face
        # Project a ray from a point above the start position and above the size of the cube
        ray_start = mathutils.Vector(start_position) +#NORMAL VECTOR)
        ray_direction = mathutils.Vector((0, 0, -1))
        
        face_index, marker_name = ray_selector(obj, ray_start, ray_direction, marker=False)
        
        if face_index is not None:            
            scale_face(cube_obj, face_index, relative_xz_scale, relative_yz_scale, 1)            
            extrude_individual_face(cube_obj, face_index, z_slice_tickness[i])
        else:
            print(f"No face found for ray starting at {ray_start}")
            
    return cube_obj
    

def create_torso(start_position):
    
    xz_patterns = [
        "---X--------",
        "--XXXX---",
        "--XXXX---",
        "----X----",
        "XXXXXXXXX",
        "XXXXXXXXX",
        "XXXXXXXXX",
        "XXXXXXXXX",
    ]

    yz_patterns = [
        "----X----",
        "--XXX--",
        "--XX--",
        "--XX--",
        "--XX--",        
        "--XX--",
        "--XX--",
        "--XX--"
    ]
    
    z_slice_tickness = [
        0.005,
        0.025,
        0.07,
        0.04,
        0.05,
        0.075,        
        0.075,        
        0.25
    ]
    
    
    # Create the initial cube
    cube_obj = create_cube(start_position, 0.25)
    
    # Scale the bottom of the cube first:
    ray_start = mathutils.Vector(start_position) - mathutils.Vector((0, 0, 1))
    ray_direction = mathutils.Vector((0, 0, 1))
    face_index, marker_name = ray_selector(cube_obj, ray_start, ray_direction, marker=False)        
    
    pattern_size_xz = len(xz_patterns[-1])
    pattern_size_yz = len(yz_patterns[-1])
    
    xz_scale = torso_calculate_scale(xz_patterns[-1], pattern_size_xz)
    yz_scale = torso_calculate_scale(yz_patterns[-1], pattern_size_yz)
        
    relative_xz_scale = xz_scale / 1
    relative_yz_scale = yz_scale / 1
    scale_face(cube_obj, face_index, relative_xz_scale, relative_yz_scale, 1)       
    prev_xz_scale = 1
    prev_yz_scale = 1     
    
    sequential_extruder
    
    # # Now scale the rest:
    # for i in range(len(xz_patterns)-2, -1, -1):  
    #     print(i)      
    #     xz_scale = torso_calculate_scale( xz_patterns[i], pattern_size_xz)
    #     yz_scale = torso_calculate_scale( yz_patterns[i], pattern_size_yz)
        
    #     relative_xz_scale = xz_scale / prev_xz_scale
    #     relative_yz_scale = yz_scale / prev_yz_scale
        
    #     prev_xz_scale = xz_scale
    #     prev_yz_scale = yz_scale
        
    #     # Step 1: Use ray select to choose the top face
    #     # Project a ray from a point above the start position and above the size of the cube
    #     ray_start = mathutils.Vector(start_position) + mathutils.Vector((0, 0, 1 + i))
    #     ray_direction = mathutils.Vector((0, 0, -1))
        
    #     face_index, marker_name = ray_selector(cube_obj, ray_start, ray_direction, marker=False)
        
    #     if face_index is not None:            
    #         scale_face(cube_obj, face_index, relative_xz_scale, relative_yz_scale, 1)            
    #         extrude_individual_face(cube_obj, face_index, z_slice_tickness[i])
    #     else:
    #         print(f"No face found for ray starting at {ray_start}")
            
    return cube_obj
