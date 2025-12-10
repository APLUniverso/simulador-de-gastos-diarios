from utils.menu import *
from utils.jsonFIleHandler import *
from utils.consoleHelper import *
from utils.dataOperator import *
from utils.css import *
from datetime import datetime,date

# Ruta de la base de datos donde estan los gastos
GASTOS_DATABASE_PATH = "./dataBase/gastos.json"
TABLES_DATABASE_PATH = "./dataBase/tables.json"
REPORTE_DETALLADO = "./reports/Reporte_detallado_de_gastos.json"

while True:
    Limpiar_Pantalla()
    print(" BIENVENIDO AL APLICATIVO DE GASTOS DIARIOS")
    while True:
        try:
            op = int(menu_final_developer("Simulador de Gasto Diario",["Registrar nuevo gasto","Listar gastos","Calcular total de gastos","Generar reporte de gastos","Revisar historial de tablas","Reporte detallado de gastos","Salir"],7))
            break
        except ValueError:
            ERROR("opcion invalida")
    match op:
        case 1:
            Limpiar_Pantalla()
            categoria,gasto_info,op = Registrar_nuevo_gasto()
            match op:
                case "c":
                    print("Se cancelo el gasto")
                case "s":
                    gastosData = readFile(GASTOS_DATABASE_PATH)
                    if foundCategoria(gastosData,categoria):
                        gastosData[categoria].append(gasto_info)
                    else:
                        gastosData[categoria] = [gasto_info]
                    saveFile(GASTOS_DATABASE_PATH,gastosData)
        case 5: # Revisar historial de tablas
            tablas = readFile(TABLES_DATABASE_PATH)
            if tablas == {}:
                input(INPUT("Sin tablas registradas\nPresione enter para continuar..."))
            else:
                while True:
                    Limpiar_Pantalla()
                    op = menu_final_developer("Historial De Tablas",["Ver tabla","Eliminar Tabla","Regresar al menú principal"],3)

                    match int(op):
                        case 1: # Ver tabla
                            print(tablas[imprmir_mini_menu(tablas)])
                            input(INPUT("Presione enter para continuar..."))
                        case 2: # Eliminar tabla
                            print("Tabla que va a ser eliminada:")
                            print(tablas.pop(imprmir_mini_menu(tablas)))
                            input(INPUT("Tabla eliminada con exito\nPresione enter para continuar..."))
                            saveFile(TABLES_DATABASE_PATH,tablas)
                        case 3: # Regresar al menú principal
                            break
        case 7: # Salir
            break

    gastosData = readFile(GASTOS_DATABASE_PATH)
    if gastosData == {}:
        input(INPUT("No hay gastos registrados actualmete\nPresione enter para continuar..."))
    else:
        match op:
            case 2: # Listar gastos
                while True:
                    Limpiar_Pantalla()
                    op = menu_final_developer("Listar Gastos",["Ver todos los gastos","Filtrar por categoría","Filtrar por rango de fechas","Regresar al menú principal"],4)
                    match int(op):
                        case 1: # Ver todos los gastos
                            imprimir_tabla(tabla_developer(gastosData,1),TABLES_DATABASE_PATH)
                        case 2: # Filtrar por categoría
                            categoria = imprmir_mini_menu(gastosData)
                            imprimir_tabla(tabla_developer(gastosData,2,userCategoria=categoria),TABLES_DATABASE_PATH)
                        case 3: # Filtrar por rango de fechas
                            hoy = datetime.strptime(str(date.today()), "%Y-%m-%d")
                            print("Formato AAAA-MM-DD")
                            while True:
                                start_dt = input(INPUT("Coloque la fecha de inicio: "))
                                if validar_fecha(start_dt):
                                    if start_dt > hoy:
                                        ERROR("La fecha todavia no ha pasado")
                                    else:
                                        break
                                else:
                                    ERROR("La fecha de inicio esta mal")
                            while True:
                                end_dt = input(INPUT("Coloque la fecha de fin: "))
                                if validar_fecha(end_dt):
                                    if datetime.strptime(start_dt, "%Y-%m-%d") > datetime.strptime(end_dt, "%Y-%m-%d"):
                                        ERROR("la fecha de fin no puede ser menor")
                                    else:
                                        if end_dt > hoy:
                                            ERROR("La fecha todavia no ha pasado")
                                        else:
                                            break
                                else:
                                    ERROR("La fecha de fin esta mal")
                            imprimir_tabla(tabla_developer(gastosData,3,start_dt=start_dt,end_dt=end_dt),TABLES_DATABASE_PATH)
                        case 4: # Regresar al menú principal
                            break
            case 3: # Calcular total de gastos
                gastosData = readFile(GASTOS_DATABASE_PATH)
                hoy = datetime.strptime(str(date.today()), "%Y-%m-%d")
                while True:
                    Limpiar_Pantalla()
                    op = menu_final_developer("Calcular Total de Gastos",["Calcular total diario","Calcular total semanal","Calcular total mensual","Regresar al menú principal"],4)
                    if int(op) == 4:
                        break
                    else:
                        print(f"El total es: {colorear('YELLOW',str(tabla_developer(gastosData,4,op_case4=op,total_Gastos=True)))}")
                        input(INPUT("Presione enter para continuar..."))
            case 4: # Generar reporte de gastos
                gastosData = readFile(GASTOS_DATABASE_PATH)
                while True:
                    Limpiar_Pantalla()
                    op = menu_final_developer("Generar Reporte de Gastos",["Reporte diario","Reporte semanal","Reporte mensual","Regresar al menú principal"],4)
                    if int(op) == 4:
                        break
                    else:
                        imprimir_tabla(tabla_developer(gastosData,4,op_case4=op),TABLES_DATABASE_PATH)
            case 6: # Reporte detallado de gastos
                gastosData = readFile(GASTOS_DATABASE_PATH)
                hoy = datetime.strptime(str(date.today()), "%Y-%m-%d")
                print("Formato AAAA-MM-DD")
                while True:
                    start_dt = input(INPUT("Coloque la fecha de inicio: "))
                    
                    if validar_fecha(start_dt):
                        if datetime.strptime(start_dt, "%Y-%m-%d") > hoy:
                            ERROR("La fecha todavia no ha pasado")
                        else:
                            
                            break
                    else:
                        ERROR("La fecha de inicio esta mal")
                while True:
                    end_dt = input(INPUT("Coloque la fecha de fin: "))
                    if validar_fecha(end_dt):
                        if datetime.strptime(start_dt, "%Y-%m-%d") > datetime.strptime(end_dt, "%Y-%m-%d"):
                            ERROR("la fecha de fin no puede ser menor")
                        else:
                            if datetime.strptime(end_dt, "%Y-%m-%d") > hoy:
                                ERROR("La fecha todavia no ha pasado")
                            else:
                                break
                    else:
                        ERROR("La fecha de fin esta mal")

                if validarSI_NO("Desea filtrar por categoria") == "si":
                    userCategoria = imprmir_mini_menu(gastosData)
                    gastos_filtrados = tabla_developer(gastosData,5,userCategoria=userCategoria,start_dt=start_dt,end_dt=end_dt)
                    saveFile(REPORTE_DETALLADO,gastos_filtrados)
                    print(gastos_filtrados)
                    input("tecla para continuar....")
                else:
                    gastos_filtrados = tabla_developer(gastosData,5,start_dt=start_dt,end_dt=end_dt)
                    print(gastos_filtrados)
                    saveFile(REPORTE_DETALLADO,gastos_filtrados)
                    input("tecla para continuar....")

                
                    
                    