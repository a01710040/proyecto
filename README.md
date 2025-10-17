# TC1028 Proyecto: Calculadora Financiera

## Contexto
El proyecto se basa en un gestor de gastos personales.
Consta en un sistema en el cual puedes agregar tus ingresos, registrar tus gastos y consultar tu balance, además de contar con un historial de tus movimientos. 

Considero que es interesante porque, uno de los grandes problemas en la sociedad es la falta de conciencia a la hora del manejo de los gastos. Asimismo, pienso es una muy buena manera de iniciar con los códigos, ya que pide mucha interacción con el usuario.
Al momento de ejecutar el programa, se despliega un menú con una lista de opciones:
1. Agregar ingreso (se pedirá una cantidad númerica)
2. Agregar gasto (se pedirá la cantidad númerica y concepto del gasto)
3. Mostrar balance (suma todos los ingresos y resta todos los gastos)
4. Ver historial (despliega los movimientos registrados junto con su concepto)
5. Salir (saldrá del programa)

Para el codigo puedo usar ciclos while, para hacer que los números que ingrese el usuario se vayan sumando, y cuando elija salir arrojarle su total. También lo puedo usar para volver a desplegar el menú de opciones hasta que también elija salir. Puedo usar ciclos for, a la hora de que el usuario me pida ver el historial y con un ciclo for le puedo arrojar sus gastos con el concepto de cada uno.

## Instrucciones
Descargar el archivo y correc en terminal con:

```markdown
python calculadora_financiera.py
```
o abrir en Thonny y dar boton de play. 

Seguir las instrucciones en pantalla para registrar movimientos o consultar el resumen final. El programa no utiliza bibliotecas externas, solo módulos estándar de Python 3.
