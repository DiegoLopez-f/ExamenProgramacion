trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

import random
import math
numeros_para_calculos=[]
diccionario_trabajadores_con_sueldo={}
trabajadores_sueldo_menor_800000={}
trabajadores_sueldo_800000_a_2000000={}
trabajadores_sueldo_mayor_2000000={}
opcion_menu = 0
archivo_reporte_csv=0

def asignar_sueldos_random():
    for cada_trabajador in trabajadores:
        valor_random = random.randint(300000, 2500000)
        numeros_para_calculos.append(valor_random)
        diccionario_trabajadores_con_sueldo[cada_trabajador]=valor_random
    print("\nSe han generado los sueldos de manera exitosa")
    return diccionario_trabajadores_con_sueldo

def clasificar_sueldos():
    for trabajador, sueldo in diccionario_trabajadores_con_sueldo.items():
        if sueldo < 800000:
            trabajadores_sueldo_menor_800000[trabajador]=sueldo
        elif sueldo >= 800000 and sueldo <=2000000:
            trabajadores_sueldo_800000_a_2000000[trabajador]=sueldo
        elif sueldo >2000000:
            trabajadores_sueldo_mayor_2000000[trabajador]=sueldo
    print(f"\nSueldos menores a $800.000 TOTAL: {len(trabajadores_sueldo_menor_800000)}")
    print(f"{"\nNombre empleado:":20}{"Sueldo":>22}\n")
    for trabajador_clasificado, sueldo_clasificado in trabajadores_sueldo_menor_800000.items():
        print(f"{trabajador_clasificado:22}{'$:'+str(sueldo_clasificado):>22}")
    print(f"\nSueldos entre $800.000 y $2.000.000 TOTAL: {len(trabajadores_sueldo_800000_a_2000000)}")
    print(f"{"\nNombre empleado:":20}{"Sueldo":>22}\n")
    for trabajador_clasificado, sueldo_clasificado in trabajadores_sueldo_800000_a_2000000.items():
        print(f"{trabajador_clasificado:22}{'$:'+str(sueldo_clasificado):>22}")
    print(f"\nSueldos mayores a $2.000.000 TOTAL: {len(trabajadores_sueldo_mayor_2000000)}")
    print(f"{"\nNombre empleado:":20}{"Sueldo":>22}\n")
    for trabajador_clasificado, sueldo_clasificado in trabajadores_sueldo_mayor_2000000.items():
        print(f"{trabajador_clasificado:22}{'$:'+str(sueldo_clasificado):>22}")
    print(f"TOTAL SUELDOS: ${sum(numeros_para_calculos)}")

def ver_estadisticas():
    for trabajador, sueldo in diccionario_trabajadores_con_sueldo.items():
        if sueldo == max(diccionario_trabajadores_con_sueldo.values()):
            print(f"El trabajador con el sueldo más alto es: {trabajador}, con un sueldo de: ${sueldo}.")
        elif sueldo == min(diccionario_trabajadores_con_sueldo.values()):
            print(f"El trabajador con el sueldo más bajo es: {trabajador}, con un sueldo de: {sueldo}.")
    print(f"El promedio de sueldos es: ${sum(numeros_para_calculos)/len(numeros_para_calculos)}")
    print(f"La media geométrica es: {math.prod(numeros_para_calculos)**(1/len(numeros_para_calculos))}")

def reporte_de_sueldos():
    print("Nombre empleado\t\t\t\tSueldo Base\t\t\tDescuento Salud\t\t\tDescuento AFP\t\t\tSueldo Líquido")
    for trabajador, sueldo_bruto in diccionario_trabajadores_con_sueldo.items():
        descuento_salud = (sueldo_bruto*0.07)
        descuento_afp = (sueldo_bruto*0.12)
        sueldo_liquido = sueldo_bruto-descuento_afp-descuento_salud
        print(f"{trabajador:15}{"$"+str(sueldo_bruto):>34}{"$"+str(descuento_salud):>40}{"$"+str(descuento_afp):>30}{"$"+str(sueldo_liquido):>32}")

print("\nBienvenido al sistema de asignación de sueldos")
while opcion_menu != 5:
    try:
        print("\nMenú:\n\n1) Asignar sueldos\n2) Clasificar sueldos\n3) Ver estadísticas\n4) Reporte de sueldos\n5) Salir")
        opcion_menu=int(input("Ingrese la opción de su preferencia: "))
        while opcion_menu <1 or opcion_menu >5:
            opcion_menu = int(input("Ha seleccionado una opción no disponible. Por favor intente nuevamente: "))
        match opcion_menu:
            case 1: 
                print("Ha seleccionado generar sueldos de forma aleatoria")
                asignar_sueldos_random()
            case 2:
                print("Ha seleccionado clasificar sueldos")
                clasificar_sueldos()
            case 3:
                print("Ha seleccionado ver estadísticas")
                if sum(numeros_para_calculos)==0:
                    print("No es posible calcular las estadísticas sin haber generado las notas, por lo que volveremos al inicio")
                    continue
                ver_estadisticas()
            case 4:
                print("Ha seleccionado generar reporte de sueldos")
                reporte_de_sueldos()
            case 5:
                print("Finalizando el programa...\nDesarrollado por Diego López Fuentes\nRUT 19.433.406-0")
                break
    except:
        print("Ha ocurrido un problema. Volviendo al inicio")
