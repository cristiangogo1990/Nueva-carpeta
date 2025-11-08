print("este programa calcula el area de un triangulo cualquiera: ")
#pido cargar los datos al usuario
base=float(input("ingrese el valor de la base del triangulo: "))
altura=float(input("ingrese el valor de la altura del triangulo: "))
#infora los valores cargados al ususario
#convierte los valores |float a string|   str(variable)    print solo concatena strings
print("los valores asignados son: base: "+ str(base) +" altura "+ str(altura))
#calculo del area del triangulo
area= (base*altura)/2
#informa el valor total del area con 2 decimales
print(f"el area total del triangulo es: {area:.2f}")