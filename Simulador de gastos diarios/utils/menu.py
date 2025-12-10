from datetime import datetime,date
from .validaciones import *
from .css import *
from .consoleHelper import imprimidor_de_menus,espasios

def Registrar_nuevo_gasto():
    print(f"{GREEN('=============================================')}\n{TITULO(espasios('Registrar Nuevo Gasto',45))}\n{GREEN('=============================================')}")
    categoria = input(INPUT("- Categoría (ej. comida, transporte, entretenimiento, otros): "))
    while True: # Validamos el MONTO
        try:
            monto = int(input(INPUT("- Monto del gasto: ")))
            if monto == 0 :
                ERROR("No puede insertar gastos que valgan 0")
            elif monto < 0:
                ERROR("No puede insertar gastos negativos")
            else:
                break
        except ValueError:
            ERROR("***ERROR***\nDato invalido")

    print("Si no quiere poner descripcion oprima enter")
    descripcion = input(INPUT("- Descripción (opcional): "))
    if not descripcion:
        descripcion = "Not Description"
    
    print("Le gustaria usar la fecha de hoy?")
    opfecha = validarSI_NO("--> ")
    hoy = str(date.today())
    match opfecha:
        case "si": # Se guarda con la fecha de hoy
            fecha = hoy
        case "no":
            while True: # validamos el rsuario ponga bien la fecha
                fecha = input(INPUT("- Procupe usar el formato AAAA-MM-DD\n  Ingrese la fecha del gasto: "))
                if validar_fecha(fecha):
                    if datetime.strptime(fecha, "%Y-%m-%d") > datetime.strptime(hoy, "%Y-%m-%d"):
                        ERROR("Su fecha todavia no ha pasado")
                    else:
                        break
                else:
                    ERROR("***ERROR***\Fecha invalido")
    # Creamos el diccionario para poder agregarlo despues
    gasto_info = {
        "monto" : monto,
        "descripcion" : descripcion,
        "fecha" : str(fecha)
    }
    while True: # validamos si quiere guardar o no
        op = input(INPUT("Ingrese 'S' para guardar o 'C' para cancelar: ")).lower()
        if op == "s" or op == "c":
            break
        else:
            ERROR("***opcion invalid***\nIntentelo nuevamente")
    print({GREEN('=============================================')})

    return categoria.lower(),gasto_info,op # Devuelve la categoria, la infomacion del gasto, y si el usuario quiere guardarlo

# Funcion que pude el dato al usuario
def menu_final_developer(titulo,lista,max):
    imprimidor_de_menus(titulo,lista)
    return validar_opcion(1,max,"--> ")