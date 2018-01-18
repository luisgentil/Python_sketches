"""Genera muestras aleatorias entre dos valores
por ahora admite repeticiones"""
muestra=[]
beta=[]
#b = 1
import random
for i in range (500):
    b = random.randint(1,4408)
    #muestra = random.randint(1,100)
    #print "nuevo valor:", b
    #print muestra
    #print muestra
    muestra.append(b)
    #print muestra
    muestra.sort()
    #print muestra # , "otra vez a empezar"
print "finalmente", muestra


