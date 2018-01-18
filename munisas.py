# -*- coding: utf-8 -*-

def municipior(x):
    """Consulta a SAS el municipio de un centro sanitario, a partir del IdCodigo.
    Responde -1 si no existe el dato en SAS """

    import sys
    sys.path.append('E:\\Documents')
    #import def_calcula_dc
    import urllib

    #print "estamos al comienzo de muestreador", "esto es x:",x
    #if __name__=="__main__":
    #    c=raw_input("Introduce el Id Centro:")
    try:
        #ww=def_calcula_dc.digitocontrol(x) #el problema esta aqui, cuando paso un niss de +9 o -8 digitos se corta la ejecucion.
        #print "x, ww, tupli, tuplii:", x, ww, tupli, tuplii

        delta="http://www.sas.junta-andalucia.es/centros/Detalle.asp?IdCentro="
        f = delta + str(x)
        #print f
        new = urllib.urlopen(f).read()

        dos=new.split(">Municipio</td><td class=\"cr\">")
        #print dos
        tres = dos[1]
        cuatro =tres.split("<")
        municipio = cuatro[0]
        #print municipio

        #print "##########"
        #print tuplii2[1]## seguro que se puede simplificar, es posible emplear splitlines() que separa las lineas
        # incluso split(), que separa en trozos segun los espacios. Hecho eso, buscar la posicion de empr_plantilla,
        # el siguiente value=" sera el anterior al valor real de la plantilla.
        #tuplii3=tuplii2[1]
        #cantidad=""
        #posicion=0
        #print tuplii3
        """for posicion in range(5):
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
        return cifra"""
    except IndexError:
        municipio="no encontrado!"
    return str(municipio)
"""gestion de errores: prever la respuesta para los siguientes errores
    errores del calculo de DC
    exceptions.IndexError: list index out of range
    NameError: name 'hiju' is not defined


"""





