#Calculadora Financiera

def pedir_ingresos():
    ingreso_total = float(input("Hola!Has iniciado la Calculadora Financiera, por favor dime cuánto dinero vas a ingresar:"))
    return ingreso_total

def sumar_ingresos(ingreso_total):
    ingreso2 = float(input("¿Tienes otro ingreso? (usa '0' en caso de no tener)"))
    while ingreso2 > 0 :
        ingreso_total = ingreso_total + ingreso2
        print("Has ingresado:$", ingreso_total)
        ingreso2 = float(input("¿Tienes otro ingreso? (usa '0' en caso de no tener)"))
    return ingreso_total


ingreso_total = pedir_ingresos()
ingreso_total = sumar_ingresos(ingreso_total)

print("Fin del programa, tus ingresos totales fueron de: $",ingreso_total)
