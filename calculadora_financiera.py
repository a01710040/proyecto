#Calculadora Financiera

def sumar_ingresos(ingreso_total):
    ingreso2 = float(input("Introduce un ingreso (usa '0' para terminar): "))
    while ingreso2 > 0:
        ingreso_total = ingreso_total + ingreso2
        print("El total de ingresos ahora es: $", ingreso_total)
        ingreso2 = float(input("Introduce otro ingreso (usa '0' para terminar): "))
    return ingreso_total

def sumar_egresos(egreso_total):
    egreso2 = float(input("Introduce un egreso/gasto (usa '0' para terminar): "))
    while egreso2 > 0:
        egreso_total = egreso_total + egreso2
        print("El total de egresos ahora es: $", egreso_total)
        egreso2 = float(input("Introduce otro egreso (usa '0' para terminar): "))
    return egreso_total

ingreso_total = 0
egreso_total = 0
menu = 3

while menu > 0:
    menu = int(input("Has desplegado el menú, selecciona (0=Salir 1=Ingresos 2=Egresos): "))

    if menu == 1:
        ingreso_total = sumar_ingresos(ingreso_total)
    
    elif menu == 2:
        egreso_total = sumar_egresos(egreso_total)

    elif menu == 0:
        print("Has salido del programa")
    else:
        print("ERROR: Opción no válida")

print("Fin del programa, tus ingresos totales fueron de: $", ingreso_total, "y tus egresos totales fueron de: $", egreso_total, "tu balance actual es de: $", (ingreso_total - egreso_total))
