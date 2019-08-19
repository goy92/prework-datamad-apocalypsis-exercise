# Caso 0: Ejemplo simple

>>> armas = ['pistola','escopeta']
>>> cargadores = {
    'pistola': [10, 10], 
    'escopeta': [2, 2, 2, 2, 2]
}

>>> if "pistola" and "escopeta" in cargadores:
	balas = list(cargadores.values())
	bala = 0
	for i in balas:
		for x in i:
			bala +=x
	print(bala)

# Caso 1: Mismas armas que municiones

>>> armas = ['pistola', 'ametralladora', 'escopeta', 'fusil de francotirador']
>>> cargadores = {
    'pistola': [12, 13, 4, 5, 20, 17], 
    'ametralladora': [33, 40], 
    'escopeta': [2, 2, 2, 1], 
    'fusil de francotirador': [1, 2, 4]
}

>>> if "pistola" and "ametralladora" and "escopeta" and "fusil de francotirador" in cargadores:
	balas = list(cargadores.values())
	bala = 0
	for i in balas:
		for x in i:
			bala +=x
	print(bala)

# Caso 2: Más tipos de munición que armas

>>> armas = ['pistola', 'ametralladora', 'escopeta', 'fusil de francotirador']

>>> cargadores = {
    'pistola': [12, 13, 4, 5, 20, 17], 
    'ametralladora': [33, 40], 
    'escopeta': [2, 2, 2, 1], 
    'fusil de francotirador': [1, 2, 4], 
    'bazoka': [1, 1]
}

	
>>> del cargadores["bazoka"]
>>> if "pistola" and "ametralladora" and "escopeta" and "fusil de francotirador" in cargadores:
	balas = list(cargadores.values())
	bala = 0
	for i in balas:
		for x in i:
			bala +=x
	print(bala)
# Caso 3: Más armas que tipos de munición

>>> armas = ['pistola', 'ametralladora', 'escopeta', 'fusil de francotirador']

>>> cargadores = {
    'pistola': [12, 13, 4, 5, 20, 17], 
    'ametralladora': [33, 40], 
    'escopeta': [2, 2, 2, 1] 
}
>>> if "pistola" and "ametralladora" and "escopeta" in cargadores:
	balas = list(cargadores.values())
	bala = 0
	for i in balas:
		for x in i:
			bala +=x
