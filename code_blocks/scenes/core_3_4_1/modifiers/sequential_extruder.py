def sequential_extruder(obj, start_position, xz_patterns, yz_patterns, z_slice_tickness, normal_vector):      
    prev_xz_scale = 1
    prev_yz_scale = 1
    
    # Select the starting face to extrude 
    # TODO: the 0.05 multiplier if too small then you lose precision and will FAIL!! will be a hard problem to debug
    ray_start = mathutils.Vector(start_position) + mathutils.Vector(tuple(x * 0.1 for x in normal_vector))
    ray_direction = mathutils.Vector(tuple(x * -1 for x in normal_vector))      
    face_index, marker_name = ray_selector(obj, ray_start, ray_direction, marker=False)
    
    if face_index is None:
        print("Face index NONE ERROR 1")
        return
    
    # Now scale the rest:
    for i in range(0, len(xz_patterns)):  
        print("Extrusion:" + str(i))              
        # EXTRUDE FACE:        
        extrude_individual_face(obj, face_index, z_slice_tickness[i])
        
    #     # SCALE the extruded FACE:
        ray_start = mathutils.Vector(ray_start) + mathutils.Vector(tuple(x * z_slice_tickness[i] for x in normal_vector))                
        face_index, marker_name = ray_selector(obj, ray_start, ray_direction, marker=False)
        
        if face_index is None:
            print("Face index NONE ERROR 2")
            print(ray_start)
            print(ray_direction)
            return
        
        scale_face(obj, face_index, xz_patterns[i], yz_patterns[i], 1)  
        
    #     # face index should remain good even after scale
        
    return obj
    