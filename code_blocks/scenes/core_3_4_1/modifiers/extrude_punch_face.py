
def extrude_punch_face(obj, face_index, distance=1.0):
    """
    Extrude a face on a mesh object by a given distance.

    Parameters:
    - obj: The mesh object.
    - face_index: The index of the face to be extruded.
    - distance: The distance to extrude the face.
    """
    
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
        # Create a geometry (face, verts, edges) for extrusion
        extruded = bmesh.ops.extrude_face_region(bm, geom=[face])
        
        # Translate the extruded geometry by the distance
        bmesh.ops.translate(bm, vec=face.normal * distance, verts=[v for v in extruded["geom"] if isinstance(v, bmesh.types.BMVert)])

        # Update the object mesh data from bmesh
        bm.to_mesh(mesh)
        mesh.update()

        # Free the bmesh
        bm.free()
    else:
        print("Invalid face index.")
