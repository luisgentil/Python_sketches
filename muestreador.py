def muestreator(x):
    """Consulta a Delt@ de la plantilla de un CCC.
    Responde -1 si no existe el dato en Delt@ """

    import sys
    sys.path.append('E:\\Documents')
    import def_calcula_dc
    import urllib

    #cc=0
    tupli=[]
    tuplii=[]

    #print "estamos al comienzo de muestreador", "esto es x:",x
    #if __name__=="__main__":
        #c=raw_input("Introduce el Niss (sin DC):")
    try:
        ww=def_calcula_dc.digitocontrol(x) #el problema esta aqui, cuando paso un niss de +9 o -8 digitos se corta la ejecucion.
        #print "x, ww, tupli, tuplii:", x, ww, tupli, tuplii

        delta="http://www.delta.mtas.es/Delta2Web/common/BuscarCCC.jsp?tipoDoc=pat&valorCCC="
        f= delta + str(ww)
        new = urllib.urlopen(f).read()

        tupli=new.split("empr_plantilla")
                #print tupli
        tuplii=tupli[1]
        tuplii2=tuplii.split("value=\"")
        #print "##########"
        #print tuplii2[1]## seguro que se puede simplificar, es posible emplear splitlines() que separa las lineas
        # incluso split(), que separa en trozos segun los espacios. Hecho eso, buscar la posicion de empr_plantilla,
        # el siguiente value=" sera el anterior al valor real de la plantilla.
        tuplii3=tuplii2[1]
        cantidad=""
        posicion=0
        #print tuplii3
        for posicion in range(5):
            a=tuplii3[posicion]
            #print a
            #raw_input()
            if a=="\"":
                break
            else:
                cantidad=cantidad+a
             #   print a, cantidad
            #raw_input()
        cifra=int(cantidad)
        return cifra
    except IndexError:
        cifra=-1
        return cifra
"""gestion de errores: prever la respuesta para los siguientes errores
    errores del calculo de DC
    exceptions.IndexError: list index out of range
    NameError: name 'hiju' is not defined


"""





