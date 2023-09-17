def create_material(name, rgb_color):
    """
    Create a new material with the given name and RGB color.

    Args:
    - name (str): The name of the material.
    - rgb_color (tuple): A tuple of RGB values between 0 and 1, plus an alpha channel (R, G, B, A).

    Returns:
    - bpy.types.Material: The created material.
    """
    material = bpy.data.materials.new(name=name)
    material.diffuse_color = rgb_color
    return material

