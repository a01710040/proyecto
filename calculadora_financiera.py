"""
Proyecto de Python: Calculadora Financiera Básica.

Este programa permite al usuario registrar transacciones de ingresos y egresos.
Calcula los totales y muestra un resumen detallado del balance final.
Los datos se manejan en memoria y se muestran al finalizar la sesión.
"""

# Bibliotecas
from datetime import datetime

# Se inicializan las listas que almacenarán los datos de las transacciones.
lista_ingresos = []
lista_egresos = []


"""
================== FUNCIONES DE TRANSACCIONES =================================
"""

def registrar_ingresos(ingreso_total_actual):
    """
    (Uso de funciones, listas, ciclos, manejo de fechas)
    Recibe: ingreso_total_actual (numérico).
    Solicita al usuario que introduzca montos de ingresos y sus descripciones,
    añadiéndolos a una lista global.
    Devuelve: El total de ingresos acumulado (numérico).
    """
    monto_ingresado = float(input("Introduce un ingreso (usa '0.0' para terminar): "))
    while monto_ingresado > 0:
        descripcion = input("Añade una descripción para este ingreso: ")
        
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        lista_ingresos.append([monto_ingresado, descripcion, fecha_actual])
        
        ingreso_total_actual = ingreso_total_actual + monto_ingresado
        print(f"El total de ingresos ahora es: ${ingreso_total_actual:.2f}")
        monto_ingresado = float(input("Introduce otro ingreso (usa '0.0' para terminar): "))
    return ingreso_total_actual


def registrar_egresos(egreso_total_actual):
    """
    (Uso de funciones, listas, ciclos, manejo de fechas)
    Recibe: egreso_total_actual (numérico).
    Solicita al usuario que introduzca montos de egresos y sus descripciones,
    añadiéndolos a una lista global.
    Devuelve: El total de egresos acumulado (numérico).
    """
    monto_egresado = float(input("Introduce un egreso/gasto (usa '0.0' para terminar): "))
    while monto_egresado > 0:
        descripcion = input("Añade una descripción para este egreso/gasto: ")

        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        lista_egresos.append([monto_egresado, descripcion, fecha_actual])

        egreso_total_actual = egreso_total_actual + monto_egresado
        print(f"El total de egresos ahora es: ${egreso_total_actual:.2f}")
        monto_egresado = float(input("Introduce otro egreso (usa '0.0' para terminar): "))
    return egreso_total_actual


"""
================== FUNCIONES AUXILIARES =======================================
"""

def mostrar_resumen_final(ingresos_totales, egresos_totales):
    """
    Función auxiliar para imprimir el resumen financiero completo.
    Muestra los detalles de ingresos, egresos y el balance final.
    """
    print("\n" + "=" * 30)
    print("       RESUMEN FINANCIERO")
    print("=" * 30)

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

    balance_actual = ingresos_totales - egresos_totales
    print("\n------------------------------")
    print(f"Ingresos Totales:   ${ingresos_totales:.2f}")
    print(f"Egresos Totales:    ${egresos_totales:.2f}")
    print(f"Balance Actual:     ${balance_actual:.2f}")
    print("------------------------------")


"""
========  PARTE PRINCIPAL DEL PROGRAMA ========================================
"""

# Se inicializan las variables para los totales.
ingreso_total = 0.0
egreso_total = 0.0
opcion_menu = -1  # Se inicia con un valor diferente de 0 para entrar al ciclo.

while opcion_menu != 0:
    print("\n--- MENÚ CALCULADORA FINANCIERA ---")
    print("1. Registrar Ingresos")
    print("2. Registrar Egresos")
    print("0. Salir y ver resumen")
    
    opcion_menu = int(input("Selecciona una opción: "))

    if opcion_menu == 1:
        ingreso_total = registrar_ingresos(ingreso_total)
    
    elif opcion_menu == 2:
        egreso_total = registrar_egresos(egreso_total)

    elif opcion_menu == 0:
        print("\nCalculando resumen final...")
    else:
        print("ERROR: Opción no válida. Por favor, intenta de nuevo.")
    
# --- Resumen Final ---
mostrar_resumen_final(ingreso_total, egreso_total)
print("\n¡Gracias por usar la calculadora! Hasta luego.")

