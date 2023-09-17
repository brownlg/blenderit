def get_object_by_name(name):
    """
    Returns the object with the specified name if it exists, otherwise returns None.

    Args:
    - name (str): The name of the object to find.

    Returns:
    - bpy.types.Object or None: The found object or None if not found.
    """
    return bpy.data.objects.get(name)
