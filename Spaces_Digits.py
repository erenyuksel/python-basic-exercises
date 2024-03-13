def is_only_string(text):
    if not isinstance(text, str):
        return False


    for char in text:
        if char.isdigit() or char.isspace():
            return False

    return True




print(is_only_string('11'))                       # False
print(is_only_string('hello'))                    # True
print(is_only_string(['hello']))                  # ? Please handle this case!! Should return False
print(is_only_string('this is a long sentence'))  # False
print(is_only_string({'a': 2}))                   # ? Please handle this case!! Should return False