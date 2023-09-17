def generate_unique_id():
    """
    Generate a unique ID.
    
    Returns:
    - str: A unique ID as a string.
    """
    unique_id = str(uuid.uuid4())
    return unique_id
