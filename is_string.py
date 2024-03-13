def is_string(text):
    return isinstance(text, str)


print(is_string('hello'))                    # True
print(is_string(['hello']))                  # False
print(is_string('this is a long sentence'))  # True
print(is_string({'a': 2}))                    # False