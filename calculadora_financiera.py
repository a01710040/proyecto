#Calculadora Financiera

from datetime import datetime

lista_ingresos = []
lista_egresos = []

def sumar_ingresos(ingreso_total):
    ingreso2 = float(input("Introduce un ingreso (usa '0' para terminar): "))
    while ingreso2 > 0:
        descripcion = input("Añade una descripción para este ingreso: ")
        
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        lista_ingresos.append([ingreso2, descripcion, fecha_actual])
        
        ingreso_total = ingreso_total + ingreso2
        print(f"El total de ingresos ahora es: ${ingreso_total:.2f}")
        ingreso2 = float(input("Introduce otro ingreso (usa '0' para terminar): "))
    return ingreso_total

def sumar_egresos(egreso_total):
    egreso2 = float(input("Introduce un egreso/gasto (usa '0' para terminar): "))
    while egreso2 > 0:
        descripcion = input("Añade una descripción para este egreso/gasto: ")

        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        lista_egresos.append([egreso2, descripcion, fecha_actual])

        egreso_total = egreso_total + egreso2
        print(f"El total de egresos ahora es: ${egreso_total:.2f}")
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

print("\n" + "="*30)
print("      RESUMEN FINANCIERO")
print("="*30)

print("\n--- Detalle de Ingresos ---")
if not lista_ingresos:
    print("No se registraron ingresos.")
else:
    for monto, descripcion, fecha in lista_ingresos:
        print(f"- {fecha} | ${monto:.2f} ({descripcion})")

print("\n--- Detalle de Egresos ---")
if not lista_egresos:
    print("No se registraron egresos.")
else:
    for monto, descripcion, fecha in lista_egresos:
        print(f"- {fecha} | ${monto:.2f} ({descripcion})")

print("\n------------------------------")
print(f"Ingresos Totales:   ${ingreso_total:.2f}")
print(f"Egresos Totales:    ${egreso_total:.2f}")
print(f"Balance Actual:     ${(ingreso_total - egreso_total):.2f}")
print("------------------------------")
