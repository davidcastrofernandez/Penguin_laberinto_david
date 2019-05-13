#creamos un archivo nuevo
#guardamos en la carpeta del repositorio
#con la extension .py
#uso de numero aleatorios
'''
#importamos la libreria radiant
from random import randint 
aleatorio=randint(0,20)    #creamos una variante aleatorio
print(aleatorio)           #y generamos un numero aleatorio entre 0 y 20
#imprimimos el campo aleatorio
'''
#ejercicio 
#escribir una funcion sorteo() que reciba una lista de participantes
#y eleguir a uno de los participante aleatoriamente y retotno
#esa persona elegida 
#desafio: no volver a retornar una persona ya sorteado
from random import randint
listaparticipanter=["david","mauro","willy","oscar","rosa","luis"]
numeroparticipantes=len((listaparticipanter)- 1)
def sorteo(lista1):
    aleatorio=randint(0,numeroparticipantes)
    ganador=listaparticipanter[aleatorio]
    return ganador
        
print(gano)
listaganadores=[]
gano=sorteo(listaparticipanter)
listaganadores.append(gano)
print(listaganadores)



  


