#Calculadora Financiera

def pedir_ingresos():
    ingreso_total = float(input("Hola! Has iniciado la sección de ingresos, por favor dime cuánto dinero vas a ingresar: "))
    return ingreso_total

def sumar_ingresos(ingreso_total):
    ingreso2 = float(input("¿Tienes otro ingreso? (usa '0' en caso de no tener): "))
    while ingreso2 > 0:
        ingreso_total = ingreso_total + ingreso2
        print("Has ingresado: $", ingreso_total)
        ingreso2 = float(input("¿Tienes otro ingreso? (usa '0' en caso de no tener): "))
    return ingreso_total

def pedir_egresos():
    egreso_total = float(input("Hola! Has iniciado la sección de egresos, por favor dime cuánto dinero has gastado: "))
    return egreso_total

def sumar_egresos(egreso_total):
    egreso2 = float(input("¿Tienes otro egreso? (usa '0' en caso de no tener): "))
    while egreso2 > 0:
        egreso_total = egreso_total + egreso2
        print("Has gastado: $", egreso_total)
        egreso2 = float(input("¿Tienes otro egreso? (usa '0' en caso de no tener): "))
    return egreso_total

ingreso_total = 0
egreso_total = 0
menu = 3

while menu > 0:
    menu = int(input("Has desplegado el menú, selecciona el número de opción que desees (0=Salir 1=Ingresos 2=Egresos) :"))

    if menu == 1:
        ingreso_total = pedir_ingresos()
        ingreso_total = sumar_ingresos(ingreso_total)
    elif menu == 2:
        egreso_total = pedir_egresos()
        egreso_total = sumar_egresos(egreso_total)
    elif menu== 0 :
        print("Has salido del programa")
    else:
        print("ERROR: Opción no válida")

if egreso_total > ingreso_total:
    print("ERROR, has gastado más de los que has ingresado")
else:
    print("Fin del programa, tus ingresos totales fueron de: $", ingreso_total, "y tus egresos totales fueron de: $", egreso_total, "tu balance actual es de: $", (ingreso_total - egreso_total))
