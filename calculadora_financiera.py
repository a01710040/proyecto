#Calculadora Financiera (Versión con formato de dos decimales)

lista_ingresos = []
lista_egresos = []

def sumar_ingresos(ingreso_total):
    ingreso2 = float(input("Introduce un ingreso (usa '0' para terminar): "))
    while ingreso2 > 0:
        descripcion = input("Añade una descripción para este ingreso: ")
        
        lista_ingresos.append([ingreso2, descripcion])
        
        ingreso_total = ingreso_total + ingreso2
        print(f"El total de ingresos ahora es: ${ingreso_total:.2f}")
        ingreso2 = float(input("Introduce otro ingreso (usa '0' para terminar): "))
    return ingreso_total

def sumar_egresos(egreso_total):
    egreso2 = float(input("Introduce un egreso/gasto (usa '0' para terminar): "))
    while egreso2 > 0:
        descripcion = input("Añade una descripción para este egreso/gasto: ")

        lista_egresos.append([egreso2, descripcion])

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
    for transaccion in lista_ingresos:
        monto = transaccion[0]
        descripcion = transaccion[1]
        print(f"- ${monto:.2f} ({descripcion})")

print("\n--- Detalle de Egresos ---")
if not lista_egresos:
    print("No se registraron egresos.")
else:
    for transaccion in lista_egresos:
        monto = transaccion[0]
        descripcion = transaccion[1]
        print(f"- ${monto:.2f} ({descripcion})")

print("\n------------------------------")
print(f"Ingresos Totales:   ${ingreso_total:.2f}")
print(f"Egresos Totales:    ${egreso_total:.2f}")
print(f"Balance Actual:     ${(ingreso_total - egreso_total):.2f}")
print("------------------------------")
