   

def create_torso(start_position):
    
    xz_patterns = [   
        0.35, #neck
        1.25, #shoulder top
        1.25, #shoulder bottom
        1,
        1,
        1    
    ]

    yz_patterns = [        
        0.5, #neck
        1, #shoulder top
        1, #shoulder bottom
        1,
        1,
        1
    ]
    
    z_slice_tickness = [        
        0.04, #neck
        0.045, # shoulder top        
        0.045, # shoulder bottom
        0.045, # belly
        0.05,  # lower bellow              
        0.045  # waist
    ]
    
    slice_names = [
        'neck',
        'shoulder_top',
        'shoulder_bottom',
        'belly',
        'lower belly',
        'waist'
    ]
    
    # angle is around extrusion axis normal
    dimensions = [
        { 'angle' : 0, 'name' : 'front' },
        { 'angle' : 90, 'name' : 'right' },
        { 'angle' : 180, 'name' : 'back' },
        { 'angle' : 270, 'name' : 'left' }
    ]
    
    
    # DNA:
    instructions = [
        { 'command' : 'push', 'value' : 0.25 , 'target_marker' : 'should_top-front' }        
    ]
    
    
    # Create the initial cube
    cube_obj = create_plane(start_position)
    
    # # # Scale the bottom of the cube first:
    ray_start = mathutils.Vector(start_position) - mathutils.Vector((0, 0, 1))
    ray_direction = mathutils.Vector((0, 0, 1))
    face_index, marker_name = ray_selector(cube_obj, ray_start, ray_direction, marker=False)        
   
    scale_face(cube_obj, face_index, 0.075, 0.04, 1)       
        
    translate_object(cube_obj, (0,-0.025,0.025)) 
    
    start_slice = slice_names.index('waist')
    end_slice = slice_names.index('shoulder_top')
    
    sequential_extruder(
        cube_obj, 
        start_position, 
        [ xz_patterns[i] for i in range(start_slice, end_slice, 1 if start_slice < end_slice else -1) ],
        [ yz_patterns[i] for i in range(start_slice, end_slice, 1 if start_slice < end_slice else -1) ],
        [ z_slice_tickness[i] for i in range(start_slice, end_slice, 1 if start_slice < end_slice else -1) ],        
        (0,0,1)
    )
    
    # Tag the head
    
    
    
    
 
    return cube_obj
