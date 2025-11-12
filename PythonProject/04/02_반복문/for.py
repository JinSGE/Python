# 1) string
str1 = 'Hello World'
print("1) string\n")
for i in str1:
    print(i)
print('*' * 50)

# 2) list
print("2) list\n")
list1 = ['a', 'b', 'c', [1, 2, 3]]
for i in list1:
    print(i)
print('*' * 50)

# 3) tuple
print("3) tuple\n")
tuple1 = ('a', 'b', 'c', [1, 2, 3])
for i in tuple1:
    print(i)
print('*' * 50)

# 4) dict
print("4) dict\n")
dict1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
for i in dict1:
    print(i)
for k,v in dict1.items():
    print(k, v)
print('*' * 50)

# 5) set
print("5) set\n")
set1 = {'a', 'b', 'c'}
for i in set1:
    print(i)
print('*' * 50)