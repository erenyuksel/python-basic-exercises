def cat_and_mouse(string):
    cat_index = string.find('C')
    mouse_index = string.find('m')

    distance = abs(cat_index - mouse_index)

    if distance <= 3:
        return "Caught!"
    else:
        return "Escaped!"



print(cat_and_mouse('C.....m')) # Escaped
print(cat_and_mouse('C..m'))  # Caught
print(cat_and_mouse('..C..m')) # Caught
print(cat_and_mouse('...C...m')) # Escaped
print(cat_and_mouse('C.m')) # Caught