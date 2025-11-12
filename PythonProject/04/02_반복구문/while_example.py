# (break)
print("1) break\n")
i = 1
while i <= 10:
	if i == 9 : break
	print(i)
	i += 1
print('*'*50)

# (continue)
print("2) continue\n")
i = 1
while i <= 10:
	i += 1
	if i%2 == 1: 	continue
	print(i, end=" ")