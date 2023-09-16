def extrude_individual_face(obj, face_index, distance=1.0):
    """
    Extrude an individual face of an object by a specific distance along its normal.
    
    Args:
    - obj (bpy.types.Object): The target object
    - face_index (int): Index of the face to extrude
    - distance (float): Distance to extrude the face along its normal. Default is 1.0.
    """
    # Make sure you are in 'OBJECT' mode
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Initialize the BMesh
    mesh = obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)
    
    # Validate internal index table
    bm.faces.ensure_lookup_table()
    
    # Reference the face to be extruded
    face = bm.faces[face_index]
    
    # Perform the extrusion
    extruded = bmesh.ops.extrude_discrete_faces(bm, faces=[face])
    
    # Translate the new geometry
    extruded_faces = extruded["faces"]
    bmesh.ops.translate(bm, vec=extruded_faces[0].normal * distance, verts=[v for f in extruded_faces for v in f.verts])
    
    
    # Update & Free BMesh
    bm.to_mesh(mesh)
    bm.free()
