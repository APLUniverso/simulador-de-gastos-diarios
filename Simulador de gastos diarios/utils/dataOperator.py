from .validaciones import *
from .consoleHelper import *
from tabulate import tabulate
from datetime import datetime,date,timedelta

def filtrar_gastos(fecha_dt,fecha_inicio,fecha_fin = None):
    if fecha_fin == None:
        if fecha_inicio == fecha_dt:
            return True
    else:
        if fecha_inicio <= fecha_dt and fecha_dt <= fecha_fin:
            return True
    return False   

def tabla_developer(data, opcion, userCategoria = None, start_dt = None, end_dt = None, op_case4 = None,total_Gastos = False):
    gastos_lista = [] # esta variable va a tener la informacion de la tabla
    total = 0
    for categoria in data:
        categoria_puesta = False
        for gastos in data[categoria]: #data[categoria] lista con los pedidos
            tupla = tuple(gastos.values())
            tupla = (categoria if not categoria_puesta else "",) + tupla
            match opcion:

                case 1: # Todos los gastos
                    gastos_lista.append(tupla)
                    categoria_puesta = True

                case 2: # Por categoria
                    if userCategoria == categoria:
                        gastos_lista.append(tupla)
                        categoria_puesta = True

                case 3: # Rango de fechas
                    fecha_dt = datetime.strptime(gastos["fecha"], "%Y-%m-%d")
                    if datetime.strptime(start_dt, "%Y-%m-%d") <= fecha_dt and fecha_dt <= datetime.strptime(end_dt, "%Y-%m-%d"):
                        gastos_lista.append(tupla)
                        categoria_puesta = True

                case 4: # Generar reporte de gastos
                    hoy = datetime.strptime(str(date.today()), "%Y-%m-%d")
                    fecha_dt = datetime.strptime(gastos["fecha"], "%Y-%m-%d")
                    
                    match int(op_case4):
                        case 1: # Calcular total diario
                            if filtrar_gastos(fecha_dt,hoy,fecha_fin = None):
                                gastos_lista.append(tupla) 
                                total += gastos["monto"]
                                categoria_puesta = True
                        case 2: # Calcular total semanal
                            if filtrar_gastos(fecha_dt,(hoy - timedelta(days=6)),fecha_fin = hoy):
                                gastos_lista.append(tupla) 
                                total += gastos["monto"]
                                categoria_puesta = True
                        case 3: # Calcular total mensual
                            if hoy.month == 1:
                                fecha_inicio = (hoy.replace(day=1))
                                fecha_inicio = fecha_inicio.replace(month=12)
                                fecha_inicio = fecha_inicio.replace(year=(hoy.year-1))
                            else:
                                fecha_inicio = (hoy.replace(day=1)).replace(month=(hoy.month - 1))
                            if filtrar_gastos(fecha_dt,fecha_inicio,fecha_fin = (hoy - timedelta(days=(hoy.day)))):
                                gastos_lista.append(tupla) 
                                total += gastos["monto"]
                                categoria_puesta = True
                case 5: # Por rango de fecha y categoria opcional
                    fecha_dt = datetime.strptime(gastos["fecha"], "%Y-%m-%d")
                    if userCategoria == None:
                        if datetime.strptime(start_dt, "%Y-%m-%d") <= fecha_dt and fecha_dt <= datetime.strptime(end_dt, "%Y-%m-%d"):
                            gastos_lista.append(tupla)
                            categoria_puesta = True
                    else:
                        if userCategoria == categoria:   
                            if datetime.strptime(start_dt, "%Y-%m-%d") <= fecha_dt and fecha_dt <= datetime.strptime(end_dt, "%Y-%m-%d"):
                                gastos_lista.append(tupla)
                                categoria_puesta = True
                                # Se retorna la tabla º
    if total_Gastos == True:
        return total
    elif opcion == 5:
        return gastos_lista
    else:
        if gastos_lista == []:
            return "No hay gastos"
        else:
            return tabulate(gastos_lista, headers=["CATEGORIA","MONTO", "DESCRIPCION","FECHA"], tablefmt="fancy_grid")