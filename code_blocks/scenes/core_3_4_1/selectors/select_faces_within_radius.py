
def select_faces_within_radius(obj, empty_obj, radius):
    # Make sure the object is a mesh and the context object is suitable
    if obj.type != 'MESH':
        print("The target object must be a mesh.")
        return []
    
    # Switch to object mode for clean context
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Create a BMesh object and load the mesh data into it
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    
    # Get the location of the empty object
    empty_location = empty_obj.location
    
    # Deselect all faces in the BMesh
    for face in bm.faces:
        face.select = False
    
    # List to hold the indices of selected faces
    selected_face_indices = []
    
    # Select faces within the radius
    for face in bm.faces:
        face_location = obj.matrix_world @ face.calc_center_median()
        distance = (face_location - empty_location).length
        if distance <= radius:
            face.select = True
            selected_face_indices.append(face.index)
    
    # Update & Free BMesh
    bm.to_mesh(obj.data)
    bm.free()
    
    return selected_face_indices
