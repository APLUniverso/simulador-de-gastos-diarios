import os
from .jsonFIleHandler import *
from .validaciones import *
from .css import *

def imprmir_mini_menu(lista): # crea mini menus con una lista
    dict_cosas = {}
    i = 0
    for cosa in lista:
        i += 1
        dict_cosas[i] = cosa
        print(f"{i}.   {cosa}")
    cosa_num = int(validar_opcion(1,i,"Eliga una: "))
    return dict_cosas[cosa_num]

def Limpiar_Pantalla():
	os.system("cls" if os.name == "nt" else "clear")

def imprimir_tabla(tabla,ruta=None): # Imprime la tabla y la guarda si el usuario quiere
    Limpiar_Pantalla()
    print(tabla)
    if tabla != "No hay gastos": # Validamos que en tabla si alla una tabla
        op = validarSI_NO("Desea guardar la tabla")
        if op == "si":
            print("Ingrese una breve descripcion de la tabla")
            descripcion_tabla = input("--> ")
            tablas = readFile(ruta)
            tablas[descripcion_tabla] = tabla
            saveFile(ruta,tablas)
    input(INPUT("Presione enter para continuar..."))

def espasios(text,caracteres): # Coloca los espasios a ambos lados para que quede centrado
    espasio = " "*int((caracteres - len(text))/2)
    return f"{espasio}{text}{espasio}"

def imprimidor_de_menus(titulo,opciones): # Imprime los menus
    print(f"{GREEN('=============================================')}\n{TITULO(espasios(titulo,45))}\n{GREEN('=============================================')}")
    print("Seleccione una opción:\n")
    for i in range(len(opciones)):
        print(f"{i+1}.   {opciones[i]}")
    print(GREEN("============================================="))