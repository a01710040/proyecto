"""
Proyecto de Python: Calculadora Financiera Básica.

Este programa permite al usuario registrar transacciones de ingresos y egresos.
Calcula los totales y muestra un resumen detallado del balance final.
Los datos se manejan en memoria y se muestran al finalizar la sesión.
"""

from datetime import datetime

# Se inicializan las listas que almacenarán los datos de las transacciones.
lista_ingresos = []
lista_egresos = []


"""
================== FUNCIONES AUXILIARES DE TRANSACCIONES ======================
"""

def obtener_fecha_actual():
    """
    Centraliza la obtención de la fecha para ser reutilizada.
    
    Devuelve:
    - str: La fecha actual formateada como "YYYY-MM-DD".
    """
    return datetime.now().strftime("%Y-%m-%d")


def procesar_transacciones(total_actual, lista_global, tipo_transaccion):
    """
    Maneja el bucle para registrar múltiples transacciones (ingresos o egresos).
    
    Recibe:
    - total_actual (float): El total acumulado antes de empezar.
    - lista_global (list): La lista (ingresos/egresos) donde se guardarán.
    - tipo_transaccion (str): El texto a mostrar (ej. "ingreso").
    
    Devuelve:
    - float: El nuevo total actualizado con las transacciones añadidas.
    """
    prompt_monto = f"Introduce un {tipo_transaccion} (usa '0.0' para terminar): "
    prompt_desc = f"Añade una descripción para este {tipo_transaccion}: "
    prompt_otro = f"Introduce otro {tipo_transaccion} (usa '0.0' para terminar): "

    monto = float(input(prompt_monto))
    
    while monto > 0:
        descripcion = input(prompt_desc)
        fecha_actual = obtener_fecha_actual()
        
        lista_global.append([monto, descripcion, fecha_actual])
        
        total_actual += monto
        print(f"El total de {tipo_transaccion}s ahora es: ${total_actual:.2f}")
        
        monto = float(input(prompt_otro))
        
    return total_actual


"""
================== FUNCIONES DE TRANSACCIONES (SIMPLIFICADAS) ================
"""

def registrar_ingresos(ingreso_total_actual):
    """
    Coordina el proceso de registrar nuevos ingresos.
    
    Recibe:
    - ingreso_total_actual (float): El total de ingresos actual.
    
    Devuelve:
    - float: El nuevo total de ingresos actualizado.
    """
    print("\n--- Registro de Ingresos ---")
    return procesar_transacciones(ingreso_total_actual, lista_ingresos, "ingreso")


def registrar_egresos(egreso_total_actual):
    """
    Coordina el proceso de registrar nuevos egresos/gastos.
    
    Recibe:
    - egreso_total_actual (float): El total de egresos actual.
    
    Devuelve:
    - float: El nuevo total de egresos actualizado.
    """
    print("\n--- Registro de Egresos ---")
    return procesar_transacciones(egreso_total_actual, lista_egresos, "egreso/gasto")


"""
================== FUNCIONES AUXILIARES DE RESUMEN ============================
"""

def imprimir_detalle_transacciones(titulo, lista_transacciones):
    """
    Imprime en consola el detalle formateado de una lista de transacciones.
    
    Recibe:
    - titulo (str): El título a imprimir (ej. "Detalle de Ingresos").
    - lista_transacciones (list): La lista (ingresos o egresos) a detallar.
    """
    print(f"\n--- {titulo} ---")
    if not lista_transacciones:
        palabra_tipo = titulo.split(' ')[-1].lower()
        print(f"No se registraron {palabra_tipo}.")
    else:
        for monto, descripcion, fecha in lista_transacciones:
            print(f"- {fecha} | ${monto:.2f} ({descripcion})")


def imprimir_balance(ingresos_totales, egresos_totales):
    """
    Calcula e imprime los totales finales y el balance.
    
    Recibe:
    - ingresos_totales (float): Total de ingresos.
    - egresos_totales (float): Total de egresos.
    """
    balance_actual = ingresos_totales - egresos_totales
    print("\n------------------------------")
    print(f"Ingresos Totales:    ${ingresos_totales:.2f}")
    print(f"Egresos Totales:     ${egresos_totales:.2f}")
    print(f"Balance Actual:      ${balance_actual:.2f}")
    print("------------------------------")


def mostrar_resumen_final(ingresos_totales, egresos_totales):
    """
    Coordina la impresión del resumen financiero completo.
    
    Recibe:
    - ingresos_totales (float): Total de ingresos.
    - egresos_totales (float): Total de egresos.
    """
    print("\n" + "=" * 30)
    print("         RESUMEN FINANCIERO")
    print("=" * 30)

    imprimir_detalle_transacciones("Detalle de Ingresos", lista_ingresos)
    imprimir_detalle_transacciones("Detalle de Egresos", lista_egresos)
    imprimir_balance(ingresos_totales, egresos_totales)


"""
================== FUNCIONES DEL MENÚ Y EJECUCIÓN =============================
"""

def mostrar_menu_principal():
    """
    Muestra el menú de opciones y captura la selección del usuario.
    
    Devuelve:
    - int: La opción numérica elegida por el usuario.
    """
    print("\n--- MENÚ CALCULADORA FINANCIERA ---")
    print("1. Registrar Ingresos")
    print("2. Registrar Egresos")
    print("0. Salir y ver resumen")
    
    opcion = int(input("Selecciona una opción: "))
    return opcion



"""
================== FUNCIONES DEL MENÚ Y EJECUCIÓN =============================
"""

ingreso_total = 0.0
egreso_total = 0.0
opcion_menu = -1 

while opcion_menu != 0:
    opcion_menu = mostrar_menu_principal()

    if opcion_menu == 1:
        ingreso_total = registrar_ingresos(ingreso_total)
    
    elif opcion_menu == 2:
        egreso_total = registrar_egresos(egreso_total)

    elif opcion_menu == 0:
        print("\nCalculando resumen final...")
    
    else: 
        print("ERROR: Opción no válida. Por favor, intenta de nuevo.")
        
mostrar_resumen_final(ingreso_total, egreso_total)
print("\n¡Gracias por usar la calculadora! Hasta luego.")
