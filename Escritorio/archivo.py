#!/usr/bin/env python
# coding: utf-8

# edad=int(input("Cuantos años tienes  "))
# if edad >=18:
#     print ("Eres mayor de edad")

# In[ ]:


x=5
y=6
if x>y:
    print(" El numero", x , "es el mayor")
if x<y:
    print("El numero", y , " es el mayor")


# In[7]:


print("Ingresa dos numeros que la suma sea igual a 10")
n1=int (input("Primer numero  "))
n2=int (input("segundo numero  "))
if n1+n2 ==10:
   print("Has acertado")
else:
   print("No has acertado")


# In[26]:


n1=int (input ("Dime un numero  "))
n2=int(input("Dime otro numero  "))
if n1>n2:
    print("El numero", n1  ,"es mayor")
else:
    if n1<n2:
        print("El numero", n2  , "es mayor"  )
    else:
        print("Son iguales")
    


# In[28]:


edad_mia=int (input("Dime tu edad  "))
edad_amigo=int (input("Dime la edad de tu amigo  "))
if edad_mia==edad_amigo:
    print("Las edades son iguales")
elif edad_mia>edad_amigo:
    print(" yo tengo mas edad")
else:
    print(" Mi amigo tiene mas edad")


# In[ ]:


print ("REFRESCOS")
print("ELIGE DEL NUMERO 1 AL 4")
eleccion=int (input("Introduce el numero  "))
if eleccion==1:
    print("Haz elegido el refresco 1")
elif eleccion==2:
    print("Haz elegido el refresco 2")
elif eleccion==3:
    print("Haz elegido el refresco 3")
elif eleccion==4:
    print("Haz elegido el refresco 4")
else:
    print("No existe ese producto")
    
    
    
    
   
    


# In[ ]:




edad=int (input("Dime la edad de la persona  "))

if edad >= 25:
    print("Es un adulto")
elif edad >= 70:
    print("Es un anciano")
elif edad >=14:
    print("Es un joven")
else:
    print("Es un niño")


# ## Programa que simula  la entrada a un parque diversiones
# Pide la edad y el peso de la persona, tiene que ser mayor de 12 años y pesar arriba de los 45 kilos.
# 

# In[ ]:


edad= int (input("Ingrese la edad  "))
peso=float(input("Ingrese el peso  en kilos "))
if edad > 12 and peso> 45:
    print("Puede pasar a la atraccion")
else:
    print("No puede pasar a la atraccion")


# In[4]:


num=int (input("Ingrese un numero:  "))
if num %2==0:
    print("El numero", num , "es par")
else:
    print("El numero", num , "es impar")


# PROGRAMA QUE COMPRUEBA SI ES MULTIPLO DE 3, 5 O DE LOS  DOS NUMEROS.
# 

# In[2]:


num=int (input("Ingresa un numero entero  "))
if num %3==0 and num %5==0:
    print("Es multiplo de  3 y de 5")
elif num %3==0:
    print("Es multiplo de 3")
elif num %5==0:
    print("Es multiplo de 5")
else: 
    print  ("No es multiplo de 3 ni de 5")


# Programa dados 3 numeros  encuentra el mayor de los tres 

# In[3]:


num1=int (input("Dime un numero:   "))
num2=int (input("Dime un segundo numero: "))
num3=int (input("Dime un tercer numero:  "))
if (num1>num3) and (num1>num3):
    print("El numero ", num1 , "es mayor" )
elif (num2>num3):
    print ("El numero", num2 , "es mayor")
else:
    print("El numero", num3 , "es mayor")


# Programa que pide un numero del 0 al 100.
# Y dice si es correcto.
# 

# In[7]:


num=int (input("Ingrese un numero del 0 al 100:   "))
if num>=0 and num<=100:
    print("El numero es correcto")
else:
    print("El numero no es correcto")


# Programa que muestre los numeros del 1 al 10 en pantalla
# 

# In[1]:


n=0
while n<=10:
    print(n)
    n=n+1


# Programa que muestre del 20 al 0.

# In[8]:


n=20
while n>0:
    print(n)
    n=n-1
print("Fin del programa.")    


# Programa que pregunta al usuario
# Si quiere seguir jugando s/n?
# 

# In[ ]:


print("Vamos a jugar")
jugando="s"

while jugando =="s":
    print("seguimos jugando")
    jugando= input("Quieres seguir jugando  (s/n)?")
    
    
print ("Fin del programa")    


# Programa que pide un contador que este entre el 10 y el 20 Si es correcto que pida el rango y te pida otro, hasta que se acabe el rango y fin del programa.

# In[3]:


n=int (input("Dime un numero entre 10 y 20:  "))
while n>=10 and n<=20:
    print("Correcto estas en el rango")
    n=int (input("Dime otro numero:  "))
    
print("Te has salido del rango")    


# Programa que te pida que adivines un numero del 1 al 10 y te pida numeros constantes hasta que lo adivines.
# Añade un contador que te diga los intentos  que has necesitado.
# 

# In[4]:


intento=int (input("Dime un numero del 1 al 10:  "))
numero="5"
veces=1
while intento != numero:
    intento=  input("No es correcto.Intentalo otra vez: ")
    veces=veces+ 1
else:
    print("Has acertado.Has necesitado", veces ,"veces.")


# In[2]:


cuenta_regresiva=int (input("Ingrese un numero: "))
while cuenta_regresiva>0:
    print(cuenta_regresiva)
    cuenta_regresiva=cuenta_regresiva-1
    
    
    
    
    


# In[1]:


cuenta_regresiva=int (input("Ingrese un numero: "))
while cuenta_regresiva>0:
    print(cuenta_regresiva)
    cuenta_regresiva=cuenta_regresiva-1


# Programa que pide la contraseña y no deja ingresar si no colocas la contraseña correcta.

# In[ ]:


print("Bienvenido al sistema")
contrasenia=1234
intento= input("Introduce la contraseña: ")
while intento!=contrasenia:
    print("La contrasenia no es correcta")
    intento= input("Intentalo otra vez:   ")
    
    
    print("Contraseña correcta")
    print("Estas dentro del sistema")


# In[ ]:


print("Bienvenido al sistema")
contrasenia=1234
intento= input("Introduce la contraseña: ")
while intento!=contrasenia:
    print("La contrasenia no es correcta")
    intento= input("Intentalo otra vez:   ")
    print("Contraseña correcta")
    print("Estas dentro del sistema")
    
   


# In[ ]:


print("Bienvenido al sistema")
contrasenia=1234
intento= input("Introduce la contraseña: ")
while intento!=contrasenia:
    print("La contrasenia no es correcta")
    intento= input("Intentalo otra vez:   ")
    
else:    
    print("Contraseña correcta")
    print("Estas dentro del sistema")


# In[ ]:


print("Bienvenido al sistema")
contrasenia=123
intento=input("Introduce la contraseña: ")
while intento != contrasenia:
print("La contraseña no es correcta")
 intento=input("Intentalo otra vez: ")
         
       


# In[ ]:


n=int (input("Ingrese un numero entre 1 y 10:  "))
while n>1 or n<10:
    print("El numero tiene que ser entre 1 y 10")
    n= input("Ingresa un numero entre 1 y 10:  ")
    


# In[ ]:


i=0
while i<5:
    print("Esto se imprimira cinco veces")
    i=i+1


# In[1]:


i=0
while i<5:
    print("Se imprime 5 veces.")
    i=i+1


# Programa que suma los numeros pares que hay entre el 1 y el 20
# 

# In[10]:




n=2
suma=0
while n <= 20:
    suma+= n
    n+=2
    
    print("El resultado es:", suma)


# Programa que ´pide un numero de inicio y uno de final al usuario  y que suma todos los multiplos de 3 que hay entre ellos.

# In[16]:


inicio: int (input("Ingrese un numero de inicio:  "))
final:int (input("Ingrese un numero final:  "))
while inicio<=final:     
    if inicio %3==0:
        suma=inicio+1
        inicio=n+1
    print("El resultado es:", suma)        
        


# In[ ]:




