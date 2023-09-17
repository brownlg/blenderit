def extrude_faces_by_indices(obj, face_indices, distance=1.0):
    """
    Extrude specified faces of a BMesh object by a given distance.
    
    Parameters:
          obj (bpy.types.Object): The Blender object with the geometry.
        face_indices (list): List of face indices to be extruded.
        distance (float, optional): Distance of the extrusion along the face normal. Defaults to 1.0.
    
    Returns:
        None: Modifies the BMesh object in-place.
    """
    
    bpy.ops.object.mode_set(mode='OBJECT')

    
    # Initialize BMesh from the object's mesh data
    mesh = obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)
    
    # Ensure the face indices are valid
    bm.faces.ensure_lookup_table()
    
    faces_to_extrude = [bm.faces[i] for i in face_indices]
    translation_vector = faces_to_extrude[0].normal * distance

    extruded = bmesh.ops.extrude_discrete_faces(bm, faces=faces_to_extrude)
    #extruded_verts = [v for v in extruded['faces'] if isinstance(v, bmesh.types.BMVert)]    
    
      # Translate the new geometry
    extruded_faces = extruded["faces"]
    bmesh.ops.translate(bm, vec=extruded_faces[0].normal * distance, verts=[v for f in extruded_faces for v in f.verts])
    
    
    # Update & Free BMesh
    bm.to_mesh(mesh)
    bm.free()

    
    # bmesh.ops.translate(bm, vec=translation_vector, verts=extruded_verts)    
    
    # bm.normal_update()    
    # bm.to_mesh(bpy.context.object.data)
