def assign_materials_to_object(object_name, materials):
    """
    Assign a list of materials to a Blender object.

    Args:
    - object_name (str): The name of the object to which the materials will be assigned.
    - materials (list): A list of bpy.types.Material objects to assign to the object.

    Returns:
    None
    """
    obj = bpy.data.objects.get(object_name)
    
    if obj is None:
        print(f"No object found with name {object_name}.")
        return
    
    # Clear existing materials
    obj.data.materials.clear()
    
    # Assign new materials
    for mat in materials:
        obj.data.materials.append(mat)
