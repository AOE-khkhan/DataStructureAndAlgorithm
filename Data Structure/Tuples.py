tups = ('Python','Java','CSharp','JavaScript')

# indexing 
print(tups[0])

#slicing 
print(tups[0:3])

# merge new tuple
tups2 = ('Scala','Swift')
tups3 = tups + tups2
print(tups3)

del tups2

try:
    print(tups2)
except NameError:
    print('Tups2 is not exists')

