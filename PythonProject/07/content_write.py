import time
import os

content = """Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!"""

file = 'file4.txt'

with open(file, "w") as fd:
    fd.write(content)

time.sleep(5)

if os.path.exists(file):
    answer = input('진짜 파일 지울거임? (y/n)')
    if answer.lower().startswith('y'):
        print("파일 지워짐 ㅅㄱ")
        os.remove(file)
