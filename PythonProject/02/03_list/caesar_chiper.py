plaintext = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

plaintextsize = len(plaintext)

ciphertext_list = []
for i in range(plaintextsize):
	# print(i)
	index = (i + 3) % plaintextsize
	# print(index)
	ciphertext_list.append(plaintext[index])
# print(ciphertext_list)
ciphertext = ''.join(ciphertext_list)

print(ciphertext)