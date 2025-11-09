print("ingrese una serie de datos numericos para calcular su media y mediana")
print("cantidad de numeros a ingresar: ")
n=int(input("numero")) # creo un contador
lista=[] #declarar la lista vacia fuera del bucle while
suma=0
n2=n
while n>0:
    n-=1  #corta el bucle de carga de datos
   #creo variable numeros. declaro el tipo entero y se lo carga el usuario por consola
    numeros=(int(input("ingrese el numero: "))) 
    lista.append(numeros) #agrego el numero cargado a la variable lista. el vector/arreglo lista
    #calcular Media = (Suma de todos los valores) / (Número total de valores)
    print("calculo de media: ")
    suma=numeros+suma
    media=suma/n
    

print ("la lista cargada es: ",lista) #imprimo string pegado a lista. la coma concatene datos
print ("la media es: ",media)

#calcular mediana (ordenar datos)
lista.sort()
print(lista)
if n2%2==0:
    par=n2/2
    print(lista[par])
else:
    impar1=(n2/2) #posicion central
    impar2=(n2/2)+1 #posicion central +1
    impar=(lista[impar1]+lista[impar2])/2 #promedio de los dos valores tomados de la lista
    print(lista[impar])
#calcular mediana (odenar datos)
#lista.sort()
#print(lista)
#Datos impares: La mediana es el valor central único del conjunto de datos ordenado.
#Datos pares: La mediana es el promedio de los dos números centrales del conjunto de datos ordenado. 
#definir funcion par n%2 == 0
#definir funcion impar n%2 != 0