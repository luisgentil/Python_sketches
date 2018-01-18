def digitocontrol(x_niss):
    """CALCULA CCC
      Calcula los digitos de control de cada CCC, para luego hacer la consulta
        a Delt@ de la plantilla de la empresa.
        Partimos del valor de Em NISS en PAEMSA formateado a 8 o 9 digitos,
        y desde ahi calculamos los digitos de control. """
    """ elaboraddo en enero 2010 para PAEMSA IV"""

#    if __name__=="__main__":
#        em_niss = raw_input("Introduce el NISS:" )
#    print x_niss
    em_niss=str(x_niss)
    largo = len(em_niss)
    caracter = 0

    if largo <8:
        ccc= "niss demasiado corto"
        if __name__=="__main__":
            return ccc
        pass
    if largo == 8: #en estos casos, la provincia tiene un digito, hay que leer el segundo caracter=caracter 1
        leer=1

    if largo==9: # en estos casos, la provincia tiene dos digitos, hay que leer el tercer caracter == caracter 2
        leer=2

    if largo>9:
        ccc="niss demasiado largo"
        if __name__=="__main__":
            return ccc
        exit ()

    caracter=em_niss[leer]

    if caracter=="0":
            niss=em_niss[0:leer]+em_niss[leer+1:] #no entiendo porque, esto ha dejado de funcionar
    else:
            niss=em_niss

    # ahora calculamos el DC a partir de niss
    idc=(int(niss)% 97)
    dc= '%02d' % idc
    cc=int(str(em_niss) + dc) # el ccc es la suma de em_niss y el DC
    ccc='%011d'% cc
    if __name__=="__main__":
        #print "largo:", largo, "leer:", leer, "caracter:", caracter, "niss:",niss, "em_niss:", em_niss
        #print "DC: ", dc, "\vCCC:", ccc, "\v"  len(ccc), "\nFin."
        print "CCC:",ccc
        exit ()
    return ccc
