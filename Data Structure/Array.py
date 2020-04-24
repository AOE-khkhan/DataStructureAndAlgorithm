from array import *

array1 = array('i',[10,20,30,40,50])

print(f'Type Of Array :{type(array1)}')

# insert 60 at index 1.
array1.insert(1,60)
print(f'\nArray after insertion: {array1}')

# delete 40 from array
array1.remove(40)
print(f'Array Remove:{array1}')

#search for an array element
index_pos = array1.index(10)
print(f'Index position for 40 {index_pos}')

#update the element
array1[2] = 90
print(f'Update the Element at index [2] : {array1}')

#speed of Numpy is much faster than Python array