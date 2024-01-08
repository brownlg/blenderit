
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
    boolean_modifier.operation = 'DIFFERENCE'
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



def apply_boolean_subtraction_all(parent_obj, subtract_obj):
    """
    Apply a Boolean subtraction of 'subtract_obj' from 'parent_obj' and all its children.

    Args:
    - parent_obj (bpy.types.Object): The parent object.
    - subtract_obj (bpy.types.Object): The object to subtract.
    """
    
    # List to store parent and all its children
    objects_to_modify = [parent_obj] + list(parent_obj.children)
   
    # Apply Boolean subtraction to each object
    for obj in objects_to_modify:        
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)
  
        # Create a Boolean modifier
        boolean_modifier = obj.modifiers.new(name="BooleanSubtract", type='BOOLEAN')
        
        if boolean_modifier is not None:
            boolean_modifier.operation = 'DIFFERENCE'
            boolean_modifier.object = subtract_obj
        
            # Apply the modifier (optional, if you want to keep the modifier live, comment out this part)
            #bpy.context.view_layer.objects.active = obj
            bpy.ops.object.modifier_apply(modifier=boolean_modifier.name)



def apply_boolean_subtraction_children(parent_obj, subtract_obj):
    """
    Apply a Boolean subtraction of 'subtract_obj' from children of 'parent_obj'

    Args:
    - parent_obj (bpy.types.Object): The parent object.
    - subtract_obj (bpy.types.Object): The object to subtract.
    """
    
    # List to store parent and all its children
    objects_to_modify = list(parent_obj.children)
   
    # Apply Boolean subtraction to each object
    for obj in objects_to_modify:        
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)
  
        # Create a Boolean modifier
        boolean_modifier = obj.modifiers.new(name="BooleanSubtract", type='BOOLEAN')
        
        if boolean_modifier is not None:
            boolean_modifier.operation = 'DIFFERENCE'
            boolean_modifier.object = subtract_obj
        
            # Apply the modifier (optional, if you want to keep the modifier live, comment out this part)
            #bpy.context.view_layer.objects.active = obj
            bpy.ops.object.modifier_apply(modifier=boolean_modifier.name)


# Example usage
# obj_a = bpy.context.scene.objects['ObjectName']  # Replace 'ObjectName' with the name of your parent object
# obj_b = bpy.context.scene.objects['OtherObjectName
