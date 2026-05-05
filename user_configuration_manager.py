def add_setting(settings, setting_tuple):
    key, value = setting_tuple
    key = key.lower()
    value = value.lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"
def update_setting(settings, setting_tuple):
   
    key, value = setting_tuple
    key = key.lower()
    value = value.lower()

   
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
  
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
def delete_setting(settings, key):
   
    key = key.lower()

    
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    
    
    return "Setting not found!"
def view_settings(settings):
    
    if not settings:
        return "No settings available."
    
   
    output = "Current User Settings:"
    
    
    for key, value in settings.items():
        output += f"\n{key.capitalize()}: {value}"
        
    return output + "\n"

test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'font_size': 'medium'
}


print(view_settings(test_settings))


print(add_setting(test_settings, ('Language', 'English')))


print(update_setting(test_settings, ('THEME', 'Light')))


print(delete_setting(test_settings, 'font_size'))


print("\nFinal State:")
print(view_settings(test_settings))
