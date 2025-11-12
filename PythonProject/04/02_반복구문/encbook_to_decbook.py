# encbook 가지고 decbook 만든다.
# encbook : 암호화할 때 사용하는 SYMBOLS
# decbook : 복호화할 때 사용하는 SYMBOLS

message = 'apple'

encbook = {'a': '#', 'p': 's', 'l': '?', 'e': 'k'}
decbook = {}

for k in encbook:
    v = encbook[k]
    decbook[v] = k

print('encbook :', encbook)
print('decbook :', decbook)