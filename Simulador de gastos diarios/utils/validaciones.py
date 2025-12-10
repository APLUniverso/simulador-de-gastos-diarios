from datetime import datetime
from .css import *

def validarSI_NO(text):
	while True:
		concluir_orden = input(INPUT(f"{text}(si/no): ")).lower()
		if concluir_orden == "si" or concluir_orden == "no":
			return concluir_orden
		else:
			ERROR("Opcion invalida")

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validar_opcion(min,max,mensaje):
    numeros = []
    for i in range(min,max+1):
        numeros.append(str(i))
    while True:
        op = input(INPUT(mensaje))
        if op not in numeros:
            ERROR("opcion invalida")
        else:
            return op