import re
from bottle import Bottle, run, request, response, route, template, static_file, error
#import sys

#inFile = sys.argv[1]
#directions = open(inFile, "r")
#directions = directions.readlines()

@route('/hola')
def hola():
	return "hola"

@route('/normalizador/<direccion:path>')
def normalice(direccion):
	print(direccion)
	direccion = direccion.replace("_", " ")
	if direccion.find("#") != -1:
		direccion = direccion.replace("#", "")
	extra = re.match("(.*)?(Pasaje|Psj|Psje|Pje|Pj|Psj.|Psje.|Pje.|Pj.)\s(\d+)(.*)?", direccion)
	if extra:
		direccion = extra.group(1) + extra.group(4)
		
	av = re.match("(Av[da|.|da.|enida]?)\s(\d*)?([^\d]*)[N|N°|Numero|Num|#|Casa|Bloque]?\s?(\d+)(.*)", direccion)
	st = re.match("(CALLE|Esquina|Esq|Esq.)\s(\d*)?([^\d]*)[N|N°|Numero|Num|#|Casa|Bloque]?\s(\d+)(.*)", direccion)
	other = re.match("(\d*)?([^\d]*)[N|N°|Numero|Num|#|Casa|Bloque]?\s(\d+)(.*)", direccion)
	if av:
		name_av = ""
		if av.group(2) != "":
			name_av = av.group(2) + " "
		name_av += av.group(3).upper()
		name_av += " "
		return "AV " + name_av + av.group(4)

	elif st:
		name_st = ""
		if st.group(2) != "":
			name_st = st.group(2) + " "
		name_st += st.group(3).upper()
		name_st += " "
		return "CALLE " + name_st + st.group(4)
	else:
		if not other:
			return "ERROR EN ESTA DIRECCION  ############################"
		name_other = ""
		if other.group(1) != "":
			name_other = other.group(1) + " "
		name_other += other.group(2).upper()
		name_other += " "
		return name_other + other.group(3)


run(host='localhost', port=8080)



