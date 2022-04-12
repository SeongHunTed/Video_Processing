list1 = [1,2,3,4]
list2 = [1, 1.5, 'a', 'a', 'words']
tuple1 = (1,2)
tuple2 = (1, 1.5, 'b', 'a', 'words')
dict1 = {'name': 'ted', 'email': 'secret'}
set1, set2 = set(list2), set(tuple2)

list1[0] = 5
list2.insert(3, 'b')
dict1['email'] = 'naver.com'

print('list1', list1, type(list1))
print('list2', list2, type(list2))
print('tuple1', tuple1), type(tuple1)
print('dict1', dict1, type(dict1))
print('set1', set1, type(set1))
print('set2', set2, type(set2))
print('insection', set1 & set2)

