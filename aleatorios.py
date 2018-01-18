# -*- coding: utf-8 -*-

"""Extrae muestras aleatorias de una población.
Se debe introducir el tamaño de la población y
el número de elementos de la muestra."""
muestra=[]
grande=int(raw_input("Elementos poblacion:"))
elementos=int(raw_input("Elementos muestra:"))
import random
muestra=random.sample(xrange(grande),elementos)
muestra.sort()
print muestra
respuesta=raw_input("Grabar muestra en archivo txt? (s/n)")
if respuesta== "s":
    nombre=raw_input("Nombre:")
    nombre_fichero=nombre+'.txt'
    fichero=open(nombre_fichero,'w')
    for elemento in muestra:
        fichero.write(str(elemento))
        fichero.write('\n')

    fichero.close()
    print fichero
# problema: el 0 está incluido, tengo que pensar cómo excluirlo puesto que no hay empresas con
# nº orden cero.

