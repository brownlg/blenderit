def attach_marker(obj, face_index, marker_name):
    if obj is None or obj.type != 'MESH':
        print("Invalid object provided. Must be a mesh object.")
        return None

    if face_index >= len(obj.data.polygons) or face_index < 0:
        print(f"Invalid face index {face_index}.")
        return None

    bpy.ops.object.mode_set(mode='OBJECT')

    bpy.ops.object.empty_add(location=(0, 0, 0))
    empty = bpy.context.active_object
    empty.name = marker_name
    empty.empty_display_type = 'SPHERE'
    empty.scale = (0.02, 0.02, 0.02)

    face_center = obj.data.polygons[face_index].center
    empty.location = obj.matrix_world @ face_center

    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')

    bm = bmesh.from_edit_mesh(obj.data)
    bm.faces.ensure_lookup_table()

    face = bm.faces[face_index]
    
    # Only select up to the first 3 vertices
    for vert in list(face.verts)[:3]:
        vert.select = True

    bmesh.update_edit_mesh(obj.data)
    
    bpy.ops.object.vertex_parent_set()

    return empty
