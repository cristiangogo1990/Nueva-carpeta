print("INGRESE UNA SERIE DE DATOS NUMERICOS PARA CALCULAR SU MEDIA Y SU MEDIANA: ")
print("CANTIDAD DE NUMEROS A INGRESAR: ")
n=int(input("NUMERO: ")) # creo un contador
lista=[] #declarar la lista vacia fuera del bucle while
suma=0
n2=n
pos=1
while n>0:
    
   #creo variable numeros. declaro el tipo entero y se lo carga el usuario por consola
    print("INGRESE UN NUMERO PARA LA POSICION: ",pos)
    numeros=(int(input("")))
    lista.append(numeros) #agrego el numero cargado a la variable lista. el vector/arreglo lista
    #calcular Media = (Suma de todos los valores) / (Número total de valores)

    suma=numeros+suma
    pos=pos+1
    n-=1  #corta el bucle de carga de datos
print ("LA LISTA CARGADA ES: ",lista) #imprimo string pegado a lista. la coma concatene datos    

print("CALCULANDO LA MEDIA: ")
media=suma/n2  #sacar la media del bucle

print ("MEDIA = ",media)

#calcular mediana (ordenar datos)
print("CALCULANDO MEDIANA: ")
lista.sort()
print("DATOS ORDENADOS DE MENOR A MAYOR: ",lista)
if n2%2!=0:
    impar=n2//2
    print("MEDIANA = ", lista[impar])
else:
    par1=(n2//2) #posicion central
    par2=(n2//2)-1 #posicion central +1
    par=(lista[par1]+lista[par2])/2 #promedio de los dos valores tomados de la lista
    print("MEDIANA = ", par)
#calcular mediana (odenar datos)
#lista.sort()
#print(lista)
#Datos impares: La mediana es el valor central único del conjunto de datos ordenado.
#Datos pares: La mediana es el promedio de los dos números centrales del conjunto de datos ordenado. 
#definir funcion par n%2 == 0
#definir funcion impar n%2 != 0