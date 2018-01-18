"""Modulo que consulta a Delt@ la plantilla de un CCC, a partir del NISS registrado en PAEMSA"""

#import def_calcula_dc
import munisas
import time

import datetime

contador=0
ahora=time.localtime()
fecha= datetime.date.today()
hoy= fecha.strftime("%d-%m-%Y") #he cambiado el / x -, ya que daba error al ser un caracter no permitido en nombres de fichero
inicio= time.strftime("%d %m %Y %H:%M:%S")
print inicio
nombrehoy='fichero-'+hoy+'.txt'
dir(hoy)
#abrir fichero de lectura
nombre=raw_input("Introduce el nombre del archivo con los datos a buscar (fichero.txt):" )
fichero=open(nombre)

escribir=open(nombrehoy,'a')    #abrir fichero de escritura de resultados en modo append
cabecera =" Consulta de municipio de Centros Sanitarios, realizada a la web del SAS el "+inicio+"\nDatos provenientes del archivo: "+nombre+"\n__Id Centro__Municipio_\n"
print cabecera,

escribir.write(cabecera)
##leer el num. total de lineas de lectura
#ahora tiene el problema de que salta las lineas pares, supongo que le falta intro al final o algo asi, probar con try /finally
# voy a probar a copiar todo el fichero en una lista, a ver cuanto tarda. si es poco, resulta mas facil manipular listas
fichero.seek(0)
datos=fichero.readlines()
## para Id Centro empleo la variable niss de cada centro de salud = 'empresa', en lugar de cambiar todas las veces en las que aparece 'empresa'
for empresa in datos:    #bucle desde 1 hasta total de lineas -1 (la primera es el encabezado)
    #empresa=datos[i]
    n_c=empresa.split()
    niss=n_c[0]
        #leido=fichero.readline()
        #print line
        #leido=line
        #print leido
        #nissleido=leido.split()
        #niss=nissleido[0]
    if niss=='Id Centro -5':
        #print "siguiente"
        continue
    #g=raw_input("Introduce el NISS:" )
    #t=def_calcula_dc.digitocontrol(g)
    #t=g
    #print "t es el resultado de def_calcula.digitocontrol ("+g+"); esto es t:",t
    #print "Hola1"
    #print t, str(t), type(t)
    else:
        h = munisas.municipior(niss)
            #print "Hola2"

    grabar=niss + ';' + str(h) +'\n'
    print grabar,
    escribir.writelines(str(grabar))   #grabar g, h en el archivo, salto de linea
    contador=contador+1
#escribir.writelines(str(h))
#fichero.next()# fin del bucle

finale='\n'+time.strftime("%d %m %Y %H:%M:%S")

fichero.close() #cerrar archivos
escribir.write("\nSe consultaron "+str(contador)+" establecimientos de AP.\n")
escribir.write(finale)
escribir.close()

print '\n',inicio,finale
print contador, " Centros.\n"

# imprimir fecha, hora, "fin."

#INCLUIR: UN contador de empresas.
