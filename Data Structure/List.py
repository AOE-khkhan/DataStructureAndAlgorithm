list1 = ['Java','Python','CSharp','JavaScript',1997]

#list indexing
print(f'Indexing : {list1[1]}')

# slicing
print(f'Slicing {list1[1:3]}')

#updating List
list1[2] = 'C++'
print(f'Updating {list1}')

list2 = ['Math','Physics','Chemistry']
# append
list1.append(list2)
print(list1)
# extend
list1.extend(list2)
print(list1)