import bpy
import mathutils

def set_object_position(obj, new_position):
    """
    Set the absolute position of an object.

    Parameters:
    - obj: The object to move.
    - new_position: A tuple or list indicating the new absolute position coordinates.
    """

    # Set the object's location to the new position
    obj.location = mathutils.Vector(new_position)

# Example usage
# obj = bpy.context.object  # Replace with your object
# new_position = (1, 2, 3)  # Replace with your desired position coordinates
# set_object_position(obj, new_position)
