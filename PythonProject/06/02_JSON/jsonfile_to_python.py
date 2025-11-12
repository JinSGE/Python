# 파이썬에서 파일 읽기
import json

fd = open('seoul.json', "r")
data = json.load(fd)
fd.close()
print(data)

data["population"] = 9600000
print(data)

fd = open('busan.json', "w")
data["city"] = "busan"
data["population"] = 3249975
json.dump(data, fd)
fd.close()

print(data)