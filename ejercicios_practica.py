#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica con números

    numero_1 = 3.56
    numero_2 = 11.33

    suma = numero_1+numero_2
    print("La suma entre",numero_1,"y",numero_2,"es",suma)

    resta = numero_1-numero_2
    print("La resta entre",numero_1,"y",numero_2,"es",resta)

    Multiplicación = numero_1*numero_2
    print("La multiplicacion entre",numero_1,"y",numero_2,"es",Multiplicación)

    division = numero_1/numero_2
    print("La division entre",numero_1,"y",numero_2,"es",division)

    Potencia = numero_1**numero_2
    print("El numero",numero_1,"elevado a la",numero_2,"es",Potencia)



def ej2():
    # Ejercicios de práctica numérica y cadenas
    
    print("Ingrese su nombre completo: ")
    nombre_completo = str(input())

    print("Ingrese su DNI: ")
    dni = int(input())

    print("Ingrese su edad: ")
    edad = int(input())

    print("Ingrese su altura: ")
    altura = float(input())

    print("Nombre completo:",nombre_completo,",","DNI:",dni)
    print("Nombre completo:",nombre_completo,",","Edad:",edad,",","Altura:",altura)

def ej3():
    # Ejercicios de práctica con cadenas
    
    print("Nombre completo del padre:")
    nombre_padre = str(input())
    a,b = nombre_padre.split(" ")
    
    print("Nombre completo de la madre:")
    nombre_madre = str(input())
    c,d = nombre_madre.split(" ")
    
    print("Nombre hija/o:")
    nombre_hijo = str(input())


    print(nombre_hijo,b,d)   

def ej4():
    # Ejercicios de práctica con cadenas

    print("Nombre completo de la primera persona: ")
    persona1 = str(input())

    print("Nombre completo de la segunda persona")
    persona2 = str(input())

    c,d = persona2.split(" ")

    parientes = d in persona1
    print(persona2,"es pariente de",persona1,"?",parientes)

def ej5():
    # Ejercicios de práctica con cadenas
       
    print("Escriba su nombre completo: ")
    nombre_completo = str.lower(input())
    print(nombre_completo)
    
    print("Escriba su nombre completo: ")
    nombre_completo = str.upper(input())
    print(nombre_completo)

    print("Escriba su nombre completo: ")
    nombre_completo = str(input()) 
    x = nombre_completo.capitalize()  
    print(x)

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
