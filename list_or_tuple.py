def is_list_or_tuple(variable):
    return isinstance(variable, (list, tuple))

print(is_list_or_tuple('hello'))      # False
print(is_list_or_tuple(['hello']))    # True
print(is_list_or_tuple([2, {}, 10]))  # True
print(is_list_or_tuple({'a': 2}))     # False
print(is_list_or_tuple((1, 2)))       # True
print(is_list_or_tuple(set()))        # False