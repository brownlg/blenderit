def scale_object(obj, scale_vector):
    """
    Scale an entire object by a given vector.

    Parameters:
    - obj: The object to be scaled.
    - scale_vector: A tuple or list indicating the scale factor for each axis (X, Y, Z).
    """
    
    obj.scale = mathutils.Vector(scale_vector)