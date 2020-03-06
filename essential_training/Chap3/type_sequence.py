#!/usr/bin/env python3
# lists are mutable and indexed
test_list = ['a', 'b', 'c', 'd', 'e']
list_id_before = id(test_list)
# when change this element the id() of this list will remain the same
test_list[2] = 42 
test_list.append('f')
list_id_after = id(test_list)

print('before: {}, after: {}, {}'.format(list_id_before, list_id_after, list_id_before == list_id_after))
# for loop is sequencing through the list
for i in test_list:
    print('i is {}'.format(i))

# once again tuples are immutable
test_tuple = ('a', 'b', 'c', 'd', 'e')

for i in test_tuple:
    print('i is {}'.format(i))

test_tuple[4]

# objects id's
another_test_tuple = (1, "two", 3.0, [1, 'x'], 'five')
more_test_tuple = (1, "two", 3.0, [1, 'x'], 'five')
test_int = 1

# different objects
id(another_test_tuple)
id(more_test_tuple)
# same objects
id(another_test_tuple[0])
id(more_test_tuple[0])
id(test_int)
# yet they are different objects
id(another_test_tuple[3])
id(more_test_tuple[3])
# yet! they are same
id(another_test_tuple[3][0])
id(more_test_tuple[3][0])
id(test_int)

# if with is can be used to check if one object is the same as another
def check_objects(object_one, object_2):
    if object_one is object_2:
        result = 'yep'
    else:
        result = 'nope'
    return result

print(check_objects(another_test_tuple, more_test_tuple)) # nope (see "different objects" part)
print(check_objects(another_test_tuple[0], more_test_tuple[0])) # yep (see "same objects" part)


# if you want to know if object is of yhis type or that type you can use isinstance
if isinstance(another_test_tuple, tuple):
    print('yep')
else:
    print('nope')