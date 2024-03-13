def is_alphanumeric(text):
    if not isinstance(text, str) or len(text) == 0:
        return False
    return all(char.isalnum() for char in text)

print(is_alphanumeric('11'))                       # True
print(is_alphanumeric(['hello']))                  # False
print(is_alphanumeric('this is a long sentence'))  # False
print(is_alphanumeric({'a': 2}))                   # False
print(is_alphanumeric("this is string....!!!"))    # False