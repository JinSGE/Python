import diablo2

jane = diablo2.Amazon()        	# jane 여전사 탄생
mary = diablo2.Amazon()       	# mary 여전사 탄생

print(f"jane strength =" + '',jane.strength)          	# jane 여전사의 강도
print(f"jane attack type" + '',jane.attack())

eve = diablo2.Amazon()         	# eve 여전사 탄생
eve.exercise()                	# eve 훈련시키기
print(f"jab damage =" + '',eve.strength)			# eve 강도

jse = diablo2.Amazon()
print(jse.energy)
print(jse.attack())
jse.exercise()
print(jse.strength)