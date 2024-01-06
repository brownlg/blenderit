
def boolean_subtract(obj_a, obj_b):
    """
    Perform a Boolean subtraction (difference) operation between two objects.

    Args:
    - obj_a (bpy.types.Object): The object from which another object will be subtracted.
    - obj_b (bpy.types.Object): The object to subtract from the first object.

    Returns:
    - bpy.types.Object: The modified object with the Boolean operation applied.
    """

    # Ensure obj_a is the active object
    bpy.context.view_layer.objects.active = obj_a
    obj_a.select_set(True)

    # Add a Boolean modifier to obj_a
    boolean_modifier = obj_a.modifiers.new(name="Boolean", type='BOOLEAN')

    # Set the operation type to 'DIFFERENCE' for subtraction
    boolean_modifier.operation = 'DIFFERENCE'

    # Set the second object (obj_b) as the target of the operation
    boolean_modifier.object = obj_b

    # Optionally, hide obj_b or delete it after the operation
    #obj_b.hide_set(True)  # Hide obj_b
    # bpy.data.objects.remove(obj_b)  # Delete obj_b

    # Apply the modifier (optional, depending on whether you want it non-destructive)
    bpy.ops.object.modifier_apply(modifier=boolean_modifier.name)

    return obj_a

# Example usage
# obj_a = bpy.data.objects['ObjectNameA']  # Replace with your object names
# obj_b = bpy.data.objects['ObjectNameB']
# boolean_subtract(obj_a, obj_b)
