
def c_mm_dev(value_mm):    
    return float(value_mm) / 10.0

def factory_box_dev(w_mm, l_mm, h_mm, wt_mm, bt_mm):
        
    # Box Attributes:
    props = {
        'width' : c_mm(w_mm),
        'height' : c_mm(h_mm),
        'length' : c_mm(l_mm),
        'wall_tickness' :c_mm(wt_mm),
        'base_thickness' : c_mm(bt_mm)
    }

    # Create shelf base --------------------------------------------------------
    base = create_cube((0,0,0), 1)

    # Extend the top face to make the base flat and wide
    base_faces = select_cube_faces(base)
    set_origin_to_bottom_center(base)
    set_object_position(base, (0,0,0))

    translate_face(base, base_faces['top'], (0, 0, float(props['height'])-1.0))
    translate_face(base, base_faces['right'], (0, float(props['width'])/2.0-0.5,0))
    translate_face(base, base_faces['left'], (0, -(float(props['width'])/2.0-0.5),0))

    translate_face(base, base_faces['front'], ((float(props['length'])/2.0-0.5),0,0))
    translate_face(base, base_faces['back'], (-(float(props['length'])/2.0-0.5),0,0))

    ### punch a hole in the box
    hammer = create_object_from_face(base, base_faces['top'], (0,0,1))
    set_origin_to_geometry_center(hammer)
    hammer_bottom = ray_selector(hammer, (0,0,hammer.location.z+1.0), (0,0,-1), max_distance=500.0)[0]
    hammer_top = duplicate_face_inplace(hammer, hammer_bottom)    
    extrude_individual_face(hammer, hammer_top , props['height'])
    set_origin_to_geometry_center(hammer)

    merge_overlapping_vertices(hammer)

    hammer_faces = select_cube_faces(hammer)
    translate_face(hammer, hammer_faces['right'], (0, -float(props['wall_tickness']), 0))
    translate_face(hammer, hammer_faces['left'],  ( 0, float(props['wall_tickness']), 0))
    translate_face(hammer, hammer_faces['front'], (-float(props['wall_tickness']), 0, 0))
    translate_face(hammer, hammer_faces['back'],  ( float(props['wall_tickness']), 0, 0))

    set_origin_to_bottom_center(hammer)
    set_object_position(hammer, (0,0, float(props['base_thickness'])))
    boolean_subtract(base, hammer)
    delete_object(hammer)

    #Cleanup
    recalculate_normals(base)
    
    return base
