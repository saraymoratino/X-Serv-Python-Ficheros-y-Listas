#!/usr/bin/python3

for i in list(range(1,11)):
	print ('\n' + "Tabla del " + str(i))
	for j in list(range(1,11)):
		resultado = i * j
		print (str(i) + "*" + str(j) + " = " + str(resultado))

