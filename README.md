# TC1028 Proyecto: Calculadora Financiera

## Contexto
Las habilidades financieras son super necesarias para el día a día. Saber cómo anotar tus ingresos, tus gastos y sacar un balance de todo ello hace que nuestra relación con el dinero sea más sencilla. Eso es lo que se proponen en este proyecto. Mediante el uso de Python reforzar las habilidades de contabilidad personal usando funciones, listas, bucles, condicionales y fechas como herramientas.

Este programa es una herramienta sencilla que no guarda en un archivo (es decir, toda la información se pierde al cerrar la aplicación) pero que permite llevar un control durante la sesión de toda tu actividad económica y posteriormente obtener un balance de tus cuentas. Por lo menos, su fin es que el usuario aprenda a organizar la información, procesarla y presentar resultados a éste de una manera clara y sencilla.

Se trata de un programa que funciona desde la consola, escrito en Python 3, que permite al usuario registrar ingresos y gastos, con su correspondiente descripción, y también fecha, que calcula el total de ingresos, total de gastos y saldo y que a su vez pone a disposición del usuario la consulta de cualquier resumen. Actualmente no guarda la información en un fichero (cada vez que se arranque la aplicación, esta empezará de nuevo sin información) aunque sí mantiene la información en memoria durante la ejecución.

Finalmente, el programa nos muestra un resumen de todos los ingresos y gastos que hemos introducido, así como el balance final que representa la diferencia de ambos.


## Instrucciones
Descargar el archivo y correc en terminal con:

```markdown
python calculadora_financiera.py
```
o abrir en Thonny y dar boton de play. 

Seguir las instrucciones en pantalla para registrar movimientos o consultar el resumen final. El programa no utiliza bibliotecas externas, solo módulos estándar de Python 3.

## Referencias API Python

"datetime" (https://docs.python.org/3/library/datetime.html): se usa para obtener la fecha actual de cada gasto.
