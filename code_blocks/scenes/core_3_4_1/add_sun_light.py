def add_sun_light(location=(0, 0, 0), energy=1.0, angle=0.1, color=(1, 1, 1)):
    """
    Add a Sun light source to the scene.
    
    Args:
    - location (tuple): The location to place the sun, as (x, y, z) coordinates.
    - energy (float): The energy level of the light.
    - angle (float): The angle of the light source, affecting the sharpness of shadows.
    - color (tuple): RGB color values for the light, as (R, G, B) where each value is between 0 and 1.
    """
    
    # Add the light object
    bpy.ops.object.light_add(type='SUN', location=location)
    
     # Make sure we're in object mode
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Get the added object and light data
    sun_light = bpy.context.object
    sun_data = sun_light.data
    
    # Set the light properties
    sun_data.energy = energy
    sun_data.angle = angle
    sun_data.color = color
