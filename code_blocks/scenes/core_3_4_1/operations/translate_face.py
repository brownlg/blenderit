def translate_face(obj, face_index, translation_vector):
    """
    Translate (move) a face on a mesh object by a given vector.

    Parameters:
    - obj: The mesh object.
    - face_index: The index of the face to be translated.
    - translation_vector: A Vector object indicating the translation direction and magnitude.
    """
    
    translation_vector = mathutils.Vector((translation_vector))
    
    # Ensure the object is a mesh
    if obj.type != 'MESH':
        print("Object is not a mesh.")
        return

    # Create a bmesh from the object
    mesh = obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)

    # Ensure the lookup table is updated
    bm.faces.ensure_lookup_table()

    # Ensure the face index is valid
    if face_index < len(bm.faces):
        face = bm.faces[face_index]
        for vert in face.verts:
            vert.co += translation_vector  # Translate vertex coordinates

        # Update the object mesh data from bmesh
        bm.to_mesh(mesh)
        mesh.update()

        # Free the bmesh
        bm.free()
    else:
        print("Invalid face index " + str(face_index) + " on actual len = " + str(len(bm.faces)))
