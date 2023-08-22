#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("Si lo imaginas, lo puedes crear")


# In[2]:


#IF
password = "ACB1230"
if password == "ACB123":
    print("la clave es correcta")


# In[6]:


#IF-ELSE
password = "ACB1230"
if password == "ACB123":
    print("la clave es correcta")
else:
    print("la clave es incorrecta")


# In[11]:


#IF-ELSE-IF
password = "rOot"
usuario = "admIn"
if usuario == "admin" and password == "root":
    print("Usario correcto |  Contraseña correcta")
    
elif usuario == "admin" and password != "root":
    print ("Usuario correcto | contraseña incorrecta")
    
elif usuario != "admin" and password == "root":
    print ("Usuario incorrecto | contraseña correcta")
    
elif usuario != "admin" and password != "root":
    print ("Usuario incorrecto | contraseña incorrecta -REVISAR TU CUNTA Y CONTRASEÑA-")


# In[13]:


#IF-ELSE-IF
password = "rOot"
usuario = "admIn"
if usuario == "admin" and password == "root":
    print("Usario correcto |  Contraseña correcta")
    
elif usuario == "admin" and password != "root":
    print ("Usuario correcto | contraseña incorrecta")
    
elif usuario != "admin" and password == "root":
    print ("Usuario incorrecto | contraseña correcta")
    
else:
    if usuario != "admin" and password != "root":
        print ("Usuario incorrecto | contraseña incorrecta -REVISAR TU CUNTA Y CONTRASEÑA-")
    


# In[18]:


#CICLO WHILE
multiplicando = 11
multiplicador = 1
producto = 0
    
while multiplicador <= 10:
    
    producto = multiplicando * multiplicador
    print(f"{multiplicando} x {multiplicador} = {producto}")
    multiplicador = multiplicador +1


# In[20]:


#BUCLE FOR IN
nombres = ['Juan', 'Antonio', 'Pedro', 'Herminio']

for nombre in nombres:
     print(nombre)


# In[23]:


#BUCLE FO-IN-RANGE

base = int (input('> Introduce el numero a elevar: '))

for exponente in range(0,10):
    potencia = base ** exponente
    print(f"{base} elevado a {exponente} es {potencia}")


# In[ ]:




