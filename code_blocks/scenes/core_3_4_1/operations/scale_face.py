
def scale_face(obj, face_index, x=0.5, y=0.5, z=0.5):
    bpy.ops.object.mode_set(mode='OBJECT')
    mesh = obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)
    bm.faces.ensure_lookup_table()
    
    face = bm.faces[face_index]
    
    bmesh.ops.scale(bm, vec=(x, y, z), verts=face.verts)
    
    bm.to_mesh(mesh)
    bm.free()
    bpy.ops.object.mode_set(mode='OBJECT')
