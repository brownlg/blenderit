def add_color_to_object(obj, color=(1, 1, 1, 1)):
    """
    Add a material with a specified color to a Blender object.
    
    Args:
    - obj (bpy.types.Object): The object to which the material should be added.
    - color (tuple): A tuple representing RGBA values (range: 0-1). Default is white.
    
    Returns:
    - bpy.types.Material: The created material.
    """
    
    # Create a new material
    mat = bpy.data.materials.new(name="Colored_Material")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = color
    
    # Assign the material to the object
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)
    
    return mat