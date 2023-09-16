def delete_face(obj, face_index):
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
        # Delete the face by its index
        bm.faces.remove(bm.faces[face_index])
        
        # Update the object mesh data from bmesh
        bm.to_mesh(mesh)
        mesh.update()

        # Free the bmesh
        bm.free()
    else:
        print("Invalid face index.")

