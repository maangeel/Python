Enunciado
Entrada de datos Salida. Debe respetarse el mismo formato del ejemplo
19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son 
iguales
4
5
El número 5 es mayor que el número 4
8
2
El número 8 es mayor que el número 2
13
13
Ambos números son iguales
20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados 
números entre 0 y 10
4
5
El número 5 es mayor que el número 4
8
2
El número 8 es mayor que el número 2
13
13
Uno o los dos números están fuera de los límites 
establecidos
11
1
Uno o los dos números están fuera de los límites 
establecidos
21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz 
cuadrada no de un valor negativo
1
-5
6
El valor de x1 es: 3.0
El valor de x2 es: 2.0
1
-6
13
La raíz no puede ser un valor negativo
PROGRAMACIÓN CON PYTHON
Departamento de Tecnología
22. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. 
Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
4 Has sacado un 4.0 y has suspendido
4.9 Has sacado un 4.9 y has suspendido
5 Has sacado un 5.0 y has aprobado
10.5 La nota que has introducido no está entre 0 y 10
-1 La nota que has introducido no está entre 0 y 10
23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un 
notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota 
introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.
1
3.5
5.2
8.6
7
Tu nota es un 1.0, has sacado un insuficiente
Tu nota es un 3.5, has sacado un insuficiente
Tu nota es un 5.2, has sacado un satisfactorio
Tu nota es un 8.6, has sacado un excelente
Tu nota es un 7.0, has sacado un notable
24. Corrige los errores del siguiente código y comprueba que se ejecuta correctamente
1var=float(input("Introduce el peso: "))
2var=(input("Introduce la altura: "))
var_imc==1var / 2var**2
print("Si pesas {1Var} kilos y mides {2var}, tu IMC es:", 
var_imc)
if var_imc>25
 print("Hay sobrepeso")
else:
 print("Estás dentro de los parámetros normales")
25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
1
3.5
5.2
8.6
7
Tu nota es un 1.0, has sacado un insuficiente
Tu nota es un 3.5, has sacado un insuficiente
Tu nota es un 5.2, has sacado un satisfactorio
Tu nota es un 8.6, has sacado un excelente
Tu nota es un 7.0, has sacado un notable
26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si 
está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
f
F
3
La letra es minúscula
La letra es mayúscula
La letra es mayúscula ¿?
27. Mejora el programa anterior para controlar que el valor introducido es una letra y en 
caso de introducir un número, aparezca un aviso por pantalla
f
F
3
/
La letra es minúscula
La letra es mayúscula
El valor introducido es un número
La letra es mayúscula ¿?
28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza 
elif.
f
F
3
/
La letra es minúscula
La letra es mayúscula
El valor introducido es un número
El valor introducido es un símbolo
PROGRAMACIÓN CON PYTHON
Departamento de Tecnología
29. Busca Internet qué función permite obtener la longitud de un String, realiza un programa 
que al introducir una frase devuelva la longitud
Hoy puede ser un buen día
Mi número de móvil es 112345
La longitud de la frase es 25
La longitud de la frase es 28
30. Realiza un programa que controle si la longitud de una frase introducida por teclado es
igual, menor o mayor de 11 caracteres. Utiliza elif
Buenos días
Buenosdías
Buenos días.
La frase tiene 11 caracteres
La frase tiene menos de 11 caracteres
La frase tiene 11 o más caracteres
31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. 
Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su 
índice.
madruga
Dios
dios
La palabra está en la frase y está en el índice 8
La palabra está en la frase y está en el índice 16
La palabra no está en la frase
32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para 
no distinguir entre mayúsculas y minúsculas
madruga
Dios
dios
La palabra está en la frase y está en el índice 8
La palabra está en la frase y está en el índice 16
La palabra está en la frase y está en el índice 16
33. Programa un código que permita contar el número de vocales de la siguiente frase: No 
hay mal que dure cien años
El número de a es 3 el número de e es 3 el número de i es 
1 el número de o es 2 y el número de u es 2
34. Corrige los 4 errores o añade el código que necesites para que el siguiente programa se 
ejecute correctamente
#inicializo valores a cada variable
var_numero=6734
var_suma=0
#obtengo su longitud
var_longitud=len(var_numero)
#sumo cada digito a partir del índice de cada posición
var_suma = var_numero [1] + var_numero [2]+ var_numero[3] + var_numero [4]
#utilizo una condición y el operador aritmético // para saber si el resto da 0 y ver si es par
if var_suma // 2 == 0:
 print (f"el valor de {var_suma} es impar"
