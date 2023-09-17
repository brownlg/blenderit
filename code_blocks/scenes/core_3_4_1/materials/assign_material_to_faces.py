def assign_material_to_faces(obj, face_indices, material_index):
    """
    Assign a specific material to selected faces of an object.

    Args:
    - object_name (str): The name of the object whose faces you want to modify.
    - face_indices (list of int): A list of face indices that should be modified.
    - material_index (int): The index of the material to assign to these faces.

    Returns:
    None
    """
    
    if obj.type != 'MESH':
        print(f"The object is not a mesh.")
        return

    # Make the object the active object and go into Edit Mode
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')
    
    # Deselect all faces
    bpy.ops.mesh.select_all(action='DESELECT')
    
    # Go back to Object Mode to select faces by their index
    bpy.ops.object.mode_set(mode='OBJECT')
    
    for index in face_indices:
        if index >= len(obj.data.polygons) or index < 0:
            print(f"Invalid face index {index}.")
            continue
        
        obj.data.polygons[index].select = True
        obj.data.polygons[index].material_index = material_index
    
    # Update the object data
    obj.data.update()

