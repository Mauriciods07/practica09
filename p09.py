#Código de la práctica 09 para comenzar el aprendizaje en Python

x = 10     #variable de tipo entero
cadena = "Hola Mundo"    #varible de tipo cadena
print(cadena, x)

x = "Hola mundo!"
type(x)

x = y = z = 10
print(x,y,z)

#Cuando una variable tiene un valor constante, por convención, el nombre se escribe en mayúsculas.
SEGUNDOS_POR_DIA = 60 * 60 * 24
PI = 3.14

cadena1 = 'Hola '
cadena2 = "Mundo" 
print(cadena1)
print(cadena2)
concat_cadenas = cadena1 + cadena2 #Concatenación de cadenas
print(concat_cadenas)

n = 5
print("Tenemos un número {}".format(n))
print(concat_cadenas + ' ' + str(3))
print(concat_cadenas, n)

num_cadena = "Cambiando el orden:  {1}  {2}  {0} #".format(cadena1, cadena2, 3)
print(num_cadena)

print( 1 + 5 )
print( 6 * 3 )
print( 10 - 4 )
print( 100 / 50 )
print( 10 % 2 )
print( ((20 * 3) + (10 +1)) / 10 )
print( 2**2 )

False and True

print (7 < 5)  #Falso
print (7 > 5) #Verdadero
print ((11 * 3)+2 == 36 - 1)  #Verdadero
print ((11 * 3)+2 >= 36)   #Falso
print ("curso" != "CuRsO") #Verdadero

print("5 + 4 es ", 5+4)
print(5 < 4)

lista_diasDelMes=[31,28,31,30,31,30,31,31,30,31,30,31]
print (lista_diasDelMes)       #imprimir la lista completa
print (lista_diasDelMes[1])   #imprimir elemento 2
print (lista_diasDelMes[4])   #imprimir elemento 5
print (lista_diasDelMes[10])  #imprimir elemento 11

lista_numeros=[['cero', 0],['uno',1, 'UNO'], ['dos',2], ['tres', 3], ['cuatro',4], ['X',5]]
print (lista_numeros)      #imprimir lista completa
print (lista_numeros[0])    #imprime el elemento 0 de la lista
print (lista_numeros[1])    #imprime el elemento 1 de la lista
print (lista_numeros[2][0]) #imprime el primer elemento de la lista en la posicion 2
print (lista_numeros[2][1]) #imprime el segundo elemento de la lista en la posicion 2
print (lista_numeros[1][0])
print (lista_numeros[1][1])
print (lista_numeros[0][0])

lista_numeros[5][0] = "cinco"
print (lista_numeros[5])

tupla_diasDelMes=(31,28,31,30,31,30,31,31,30,31,30,31)
print (tupla_diasDelMes)       #imprimir la tupla completa
print (tupla_diasDelMes[5])    #imprimir elemento 6
print (tupla_diasDelMes[3])    #imprimir elemento 4
print (tupla_diasDelMes[1])   #imprimir elemento 2

tupla_numeros=(('cero', 0),('uno',1, 'UNO'), ('dos',2), ('tres', 3), ('cuatro',4), ('X',5))
print (tupla_numeros)        #imprimir tupla completa
print (tupla_numeros[0])     #imprime el elemento 0 de la tupla
print (tupla_numeros[1])     #imprime el elemento 1 de la tupla
print (tupla_numeros[2][0])  #imprime el primer elemento de la tupla en la posicion 2
print (tupla_numeros[2][1])  #imprime el segundo elemento de la tupla en la posicion 2
print (tupla_numeros[1][0])
print (tupla_numeros[1][1])
print (tupla_numeros[1][2])

from collections import namedtuple
planeta = namedtuple('planeta', ['nombre', 'numero'])
planeta1 = planeta('Mercurio', 1)
print(planeta1)
planeta2 = planeta('Venus', 2)
print(planeta1.nombre, planeta1.numero)  
print(planeta2[0], planeta2[1])  
print('Campos de la tupla: {}'.format(planeta1._fields))

elementos = { 'hidrogeno': 1, 'helio': 2, 'carbon': 6 }
print(elementos)
print(elementos['hidrogeno'])
print (elementos['helio'])

elementos['litio'] = 3
elementos['nitrogeno'] = 8
print (elementos)

elementos2 = {}
elementos2['H'] = {'name': 'Hydrogen', 'number': 1, 'weight': 1.00794}
elementos2['He'] = {'name': 'Helium', 'number': 2, 'weight': 4.002602}
print (elementos2)

print (elementos2['H'])
print (elementos2['H']['name'])
print (elementos2['H']['number'])
elementos2['H']['weight'] =  4.30  #Cambiando el valor de un elemento
print (elementos2['H']['weight'])

elementos2['H'].update({'gas noble':True})
print (elementos2['H'])

print (elementos2.items())
print (elementos2.keys())

def imprime_nombre(nombre):
    print("hola "+nombre)
imprime_nombre("JJ")

def cuadrado(x):
    return x**2
x = 5
print("El cuadrado de {} es {}".format(x, cuadrado(x)))

def varios(x):
    return x**2, x**3, x**4
val1, val2, val3 = varios(2)
print("{} {} {}".format(val1, val2, val3))

def cuadrado_default(x=3):
    return x**2
cuadrado_default()

val4, _, val5 = varios(2)
print("{} {}".format(val4, val5))

vg = 'Global'

def funcion_v1():
    print(vg)

funcion_v1()
#Imprime la variable global
print(vg)

def funcion_v2():
    vg = "Local"
    print(vg)

funcion_v2()  #Imprime valor local
#Imprime la variable global
print(vg)

def funcion_v3():
    print(vg)
    vg = "Local"
    print(vg)

funcion_v3()

def funcion_v4():
    global vg
    print(vg)
    vg = "Local"
    print(vg)

funcion_v4()
print(vg)

def sumar(x):
	y = 5
	return x + y
n = 4
sumar(n)