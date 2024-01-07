def translate_object(obj, translation_vector):
    """
    Translate (move) an entire object by a given vector.

    Parameters:
    - obj: The object.
    - translation_vector: A tuple or list indicating the translation direction and magnitude.
    """
    
    obj.location += mathutils.Vector(translation_vector)

