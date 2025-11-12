# import socket
# socket.setdefaulttimeout(2)
# s = socket.socket()
# s.connect(("192.168.10.200", 21))
# ans = s.recv(1024)
# print(ans)

# b'220 (vsFTPd 2.0.5)\r\n'

import socket

socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("192.168.10.60", 21))
ans = s.recv(1024)

# https://www.exploit-db.com/
if 'vsFTPd 2.0.5' in str(ans):
    print('[+] vsFTP FTP Server is vulnerable.')
elif 'FreeFloat Ftp Server (Version 1.00)' in str(ans):
    print('[+] FreeFloat FTP Server is vulnerable.')
elif '3Com 3CDaemon FTP Server Version 2.0' in str(ans):
    print('[+] 3Com 3CDaemon FTP Server is vulnerable.')
elif 'Ability Server 2.34' in str(ans):
    print('[+] Ability FTP Server is vulnerable.')
elif 'Sami FTP Server 2.0.2' in str(ans):
    print('[+] Sami FTP Server is vulnerable.')
else:
    print('[-] FTP Server is not vulnerable.')