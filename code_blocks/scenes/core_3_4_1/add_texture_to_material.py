
def add_texture_to_material(mat, texture_path):
    """
    Add a texture to a Blender material.
    
    Args:
    - mat (bpy.types.Material): The material to which the texture should be added.
    - texture_path (str): Path to the texture image.
    
    Returns:
    - bpy.types.ShaderNodeTexImage: The created texture node.
    """
    
    # Ensure material uses nodes
    mat.use_nodes = True
    
    # Add a texture node and load the texture
    tex_node = mat.node_tree.nodes.new("ShaderNodeTexImage")
    tex_node.image = bpy.data.images.load(texture_path)
    
    # Connect the texture node to the "Base Color" input of the BSDF
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    mat.node_tree.links.new(bsdf.inputs["Base Color"], tex_node.outputs["Color"])
    
    return tex_node