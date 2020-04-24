import collections

dict1 = {'day1' : 'Mon', 'day2' : 'Tue'}
dict2 = {'day3' : 'Wed', 'day1' : 'Thu'}

res = collections.ChainMap(dict1,dict2)

print(res.maps, '\n')

#print key and values
print(f'Keys : {list(res.keys() )}')
print(f'Values : {list(res.keys() )}')

# print all elements from the result 
for key, value in res.items():
    print(f'{key} = {value}')

# find a specific value in the result
print(f'day3 in res : {("day3" in res)}')

