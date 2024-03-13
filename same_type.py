def are_same_type(some_list):


    return all(isinstance(x, type(some_list[0])) for x in some_list)


print(are_same_type(['hello', 'world', 'long sentence']))  # True
print(are_same_type([1, 2, 9, 10]))                        # True
print(are_same_type([['hello'], 'hello', ['bye']]))        # False
print(are_same_type([['hello'], [1, 2, 3], [{'a': 2}]]))   # True
print(are_same_type([['hello'], set('hello')]))            # False