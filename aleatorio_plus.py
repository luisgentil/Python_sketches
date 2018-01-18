# -*- coding: utf-8 -*-

"""Extrae muestras aleatorias de una población controlando: provincia, CNAE, tamaño Plantilla."""
#importaciones
import time
import datetime
import random
#función Text-plantilla
plantilla=0

def Tplantilla(plantilla):
    """Devuelve la etiqueta correspondiente a la clasificación europea del tamaño de plantilla"""
    if plantilla<10:
        T='micropyme'
    elif 10<=plantilla<50:
        T='peque'
    elif 50<=plantilla<=250:
        T='mediana'
    elif 250<=plantilla<500:
        T='grande'
    elif plantilla>=500:
        T='muygrande'
    return T

#definiciones básicas
n_muestra=int(raw_input('Cantidad de elementos que debe contener la muestra:'))

muestra=[]
tamanio=0
paemsas=0
no_muestra=[]
descartados=0
nom_provincias=('4','11','14','18','21','23','29','41')    #control-provincia
nom_plantillas=('micropyme','peque','mediana','grande','muygrande')
nom_cnaes=('01-02','05','13-14','15-16','17-18','19','20','21-22','23','24','25','26','27','28','29','30-32','31','33','34','35','36-37','40-41','45','50','51','52','55','60','61','62','63-64','65-66-67','70-71','72-73','74','75','80','85','90','91-92','93','95','99')
#nom_cnaes no incluye los siguientes: 10, 11, 12
valores_limites_provincias=(0.087*n_muestra,0.13*n_muestra,0.109*n_muestra,0.1*n_muestra,0.07*n_muestra,0.078*n_muestra,0.196*n_muestra,0.23*n_muestra)    #los coeficientes 0607, podremos leerlo de un fichero
valores_limites_plantillas=(0.49*n_muestra,0.39*n_muestra,0.10*n_muestra,0.01*n_muestra,0.01*n_muestra)          #los coeficientes 0607, prodemos leerlo de un fichero
valores_limites_cnaes=(0.07815*n_muestra,0.00678*n_muestra,0.00411*n_muestra,0.02926*n_muestra,0.00385*n_muestra,0.00095*n_muestra,0.01713*n_muestra,0.00568*n_muestra,0.00052*n_muestra,0.00529*n_muestra,0.00372*n_muestra,0.01566*n_muestra,0.01428*n_muestra,0.03383*n_muestra,0.00807*n_muestra,0.00113*n_muestra,0.00424*n_muestra,0.00034*n_muestra,0.00197*n_muestra,0.00378*n_muestra,0.02003*n_muestra,0.00590*n_muestra,0.32501*n_muestra,0.03234*n_muestra,0.05016*n_muestra,0.06254*n_muestra,0.06459*n_muestra,0.04066*n_muestra,0.00098*n_muestra,0.00061*n_muestra,0.01158*n_muestra,0.00311*n_muestra,0.01243*n_muestra,0.00206*n_muestra,0.03321*n_muestra,0.02944*n_muestra,0.01035*n_muestra,0.01453*n_muestra,0.00431*n_muestra,0.01587*n_muestra,0.01841*n_muestra,0.00314*n_muestra)

"""Cuando leamos los coeficientes, las variables se activarán así:
leer coef_provincias #leer valores de coeficientes desde un txt
#abrir archivo de lectura, copiar datos a una lista
nombre='coef_provincias.txt'              #nombre=raw_input("Introduce el nombre del archivo con los datos de los coeficientes de % de provincias (fichero.txt):" )
fichero=open(nombre)
fichero.seek(0)
coef_provincias=fichero.readlines()       #asigna todos los datos de todas las empresas a una lista llamada 'datos'
numero=0
for elemento in coef_provincias
    valores_limites_provincias[numero]=(elemento*n_muestra)
    numero=numero+1

leer coef_plantillas #leer valores de coeficientes de límites de plantillas desde un txt
numero=0
for elemento in coef_plantillas
    valores_limites_plantillas[numero]=(elemento*n_muestra)
    numero=numero+1

leer coef_cnaes #leer valores de coeficientes de límites de cnaes desde un txt
numero=0
for elemento in coef_cnaes
    valores_limites_cnaes[numero]=(elemento*n_muestra)
    numero=numero+1

"""
#leer límites de la muestra --> componer los diccionarios
PROV=zip(nom_provincias,valores_limites_provincias)
PLANT=zip(nom_plantillas,valores_limites_plantillas)
CNAE=zip(nom_cnaes,valores_limites_cnaes)
lim_provincias=dict(PROV)
lim_plantillas=dict(PLANT)
lim_cnaes=dict(CNAE)

#inicia las variables que controlan la composición de la muestra seleccionada
control_provincias=(0,0,0,0,0,0,0,0)
control_plantillas=(0,0,0,0,0)
control_cnaes=(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
CPROV=zip(nom_provincias,control_provincias)
CPLANT=zip(nom_plantillas,control_plantillas)
CCNAE=zip(nom_cnaes,control_cnaes)
C_provincias=dict(CPROV)                #C-pronvicias: control de provincias en la selección
C_plantillas=dict(CPLANT)               #C-plantillas: control de plantillas en la selección
C_cnaes=dict(CCNAE)                     #C-cnaes: control de cnaes en la selección

#abrir archivo de lectura, copiar datos a una lista
nombre='Python_pruebas2.txt'              #nombre=raw_input("Introduce el nombre del archivo con los datos a buscar (fichero.txt):" )
fichero=open(nombre)
fichero.seek(0)
datos=fichero.readlines()       #asigna todos los datos de todas las empresas a una lista llamada 'datos'

#comienza el bucle, mientras queden empresas en datos ## hasta que hayamos probado con todas las empresas ## hasta que la selección tenga el nº de elementos que debe contener la muestra
for n in datos:
    if len(muestra)==n_muestra:
      break
#while len(muestra)<n_muestra:
    #if len(datos)==1:
     #   break
#elige empresa aleatorio
    empresa=random.choice(datos)#elige un elemento (una empresa) de la lista 'datos'

#fichero.pop(nº aleatorio): lee los datos de la empresa que corresponde al nº aleatorio,
#y lo elimina de la lista que contiene los datos de todas las empresas del fichero fuente para que no pueda repetirse
    datos.pop(datos.index(empresa))          #elimina la empresa del conjunto de datos

#split a las variables de trabajo
    ficha=empresa.split(';')       #separa los datos de la empresa en elementos de una lista
    aleat=ficha[0]              #valor del nº de orden
    prov=ficha[1]               #para calcular el valor del código de provincia
    provincia=prov[0:2]         #cuando el txt trae el código de provincia como xx.00, se toma solo la parte izquierda
    if ',' in provincia:        #hay que eliminar el ',' si lo hay
        provincia=provincia[0:provincia.index(',')]
    nif=ficha[2]                #valor del NIF
    cnae=ficha[3]               #valor del CNAE en formato PAEMSA 3
    plantilla=ficha[4]          #valor de plantilla 0607
    if ',' in plantilla:        #hay que eliminar el ',' si lo hay
        plantilla=plantilla[0:plantilla.index(',')]+'.'+plantilla[plantilla.index(',')+1:]
    Textplant=Tplantilla(float(plantilla))#convierte plantilla en su valor equivalente en texto
    iit0708=ficha[5]            #valor del IIT en periodo 20072008, sirve para depurar la muestra
    #print iit0708
    historia=ficha[6]           #valor del nº de historia en PAEMSA III
    if historia=="":
        historia=0
    niss=ficha[7]               #valor de CT NISS
##como es pop no hace falta compruebar si el cif está en la selección

#comprueba todos los contadores; si alguno falla rompe el bucle y vuelve a generar aleatorio
    try:
        if len(muestra)==n_muestra:
            break
        if C_provincias[provincia]<lim_provincias[provincia]:
            if C_plantillas[Textplant]<lim_plantillas[Textplant]:
                if C_cnaes[cnae]<lim_cnaes[cnae]:               #si cumple contadores: añadir CIF a la muestra, incrementar todos los contadores en una unidad
                    muestra.append(empresa)
                    C_provincias[provincia]=C_provincias[provincia]+1
                    C_plantillas[Textplant]=C_plantillas[Textplant]+1
                    C_cnaes[cnae]=C_cnaes[cnae]+1
                    tamanio=tamanio+1
                    #print 'Seleccionada',provincia
                    if historia>0:
                        paemsas=paemsas+1

                else:
                    #print "descartado x 1",
                    no_muestra.append(empresa)
                    descartados=descartados+1
                    continue
            else:
                #print "descartado x 2",
                no_muestra.append(empresa)
                descartados=descartados+1
                continue
        else:
            #print "descartado x 3",
            no_muestra.append(empresa)
            descartados=descartados+1
            continue
    except KeyError:
        #print 'provincia inexistente:', provincia
        continue

fichero.close()
if len(muestra)<n_muestra:
    print 'No fue posible crear una muestra con ', n_muestra,'elementos.'

print "Elementos de la muestra:",tamanio,'de los que ',paemsas, 'son de PAEMSA III.'
w=raw_input('Imprimir muestra en pantalla?(s/n)')
if w=="s":
    for i in range(len(muestra)): print muestra[i],
print "Elementos de la muestra:",tamanio,'de los que ',paemsas, 'son de PAEMSA III.'
print "Descartados:",descartados

#grabar fichero con la muestra

respuesta=raw_input("Grabar MUESTRA en archivo txt? (s/n)")
if respuesta== "s":
    nombre=raw_input("Nombre:")
    nombre_fichero=nombre+'.txt'
    fichero=open(nombre_fichero,'w')
    for elemento in muestra:
        fichero.write(str(elemento))
        #fichero.write('\n')

    fichero.close()

#pregunta si quiere supervivencia
w=raw_input('Aplicar supervivencia 2007 y 2008 a la muestra?(s/n)')
if w=="s":                  #respuesta sí

#inicia variables de control, de límite de supervivencia
    supervivientes=[]
    coeficientes_supervivencia=[0.0248711568847073,0.0248711568847073,0.00851571364693824,0.00596726498642359,0.0265567233522129,0.0328531129011744,0.0136803061312838,0.011185908737744,0,0.00431632278575837,0.00685809958127643,0.00939249609096346,0.00560225003589094,0.0123998796395643,0.00767995429242042,0.0169763685978949,0.00640930811584376,0.00781474709722346,0.00618361983646425,0.0124586957180762,0.0168979892616527,0.00465989940382112,0.0664434699556959,0.0110564004540682,0.0118392407775775,0.0229253314467654,0.0376224020928265,0.0222225933312695,0.0175337846093693,0.0175337846093693,0.0189417820205821,0.0182265784227376,0.0394000895139819,0.0182241803672596,0.0159891401552582,0.00466472153590695,0.00864354842107141,0.00466472153590695,0.00694450868378101,0.0119488218489943,0.0185353959649765,0.00188986696139822,0.000]
    #no incluye los cnaes 10, 11-12, y el último corresponde a cnae 99
    coef_superv=zip(nom_cnaes,coeficientes_supervivencia)
    coef_supervivencia_cnae=dict(coef_superv)
    lim_supervivencia_cnae=C_cnaes
    for n in lim_supervivencia_cnae:
        lim_supervivencia_cnae[n]=lim_supervivencia_cnae[n]*coef_supervivencia_cnae[n]#límites de elementos a eliminar en cada rama de CNAE, en función del tamaño de la muestra de la que se parte
    CCNAE=zip(nom_cnaes,control_cnaes)
    C_superv_cnaes=dict(CCNAE)

    print len(muestra),len(supervivientes) #no sé porqué elimina elementos de la muestra, cuando debía eliminarlos de la copia
#inicia el bucle: para todos los elementos de la copia de la muestra
    for n in muestra:

        empresa=random.choice(muestra)#elige un elemento (una empresa)  aleatoria/ de la muestra
        print empresa
        #split a las variables de trabajo split el cnae, el IIT0708
        ficha=empresa.split(';')       #separa los datos de la empresa en elementos de una lista
        cnae=ficha[3]               #valor del CNAE en formato PAEMSA 3
        iit0708=ficha[5]            #valor del IIT en periodo 20072008
        print iit0708, len(muestra), len(supervivientes)
        #comparaciones:
        if iit0708=="":
            if C_superv_cnaes[cnae]<lim_supervivencia_cnae[cnae]:   # si en el CNAE se cumple control_supervivientes < límites_supervivientes
                # si se cumple, eliminar --> xlq no se añade a supervivientes (se elimina)
                C_superv_cnaes[cnae]=C_superv_cnaes[cnae]+1         # incrementa el control
            else:
                supervivientes.append(empresa) # si el control supera el limite es xq ya ha eliminado las suficientes, así que las añade.
        else:
            supervivientes.append(empresa) # si el iit0708 es <> 0, añade la empresa

#imprime resumen, imprime listado
    print "Muestra con ",len(muestra)," empresas."
    print "Supervivientes con ",len(supervivientes), "empresas."

w=raw_input('Imprimir supervivientes en pantalla?(s/n)')
if w=="s":
    for i in range(len(supervivientes)): print supervivientes[i],

#grabar fichero con los supervivientes

respuesta=raw_input("Grabar los supervivientes en archivo txt? (s/n)")
if respuesta== "s":
    nombre_fichero="sup-"+nombre+'.txt'
    fichero=open(nombre_fichero,'w')
    for elemento in supervivientes:
        fichero.write(str(elemento))
        #fichero.write('\n')
    fichero.close()

##fin


"""Mejoras pendientes:
- que permita elegir un archivo con los porcentajes que debe aplicar a la composición
OK - que pregunte si quiere grabar la muestra
- que pregunte si quiere grabar los descartes
- comprobar que los resultados son correctos, es decir, que la muestra seleccionada es de la proporción deseada.
OK - generar la muestra simulando el efecto de la supervivencia de empresas.
- comprobar que el porcentaje de reducción es, globalmente, correcto."""






