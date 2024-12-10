#Datos de entrada para este modulo
#ibus numero de barra
#id id del generador
#i5-> CON a cambiar

import psspy
import modules.informe as informe
import textwrap

def generadores(ruta, nombre_archivo,ibus,id,i5):
    '''
    Función que verifica los datos obtenidos del archivo"reserva.dat"

    :param ruta: ruta del archivo
    :param nombre_archivo: nombre del archivo
    :param ibus: numero de barra
    :param id: id del generador
    :param i5: CON a cambiar
    '''
    ruta = ruta+'/'+nombre_archivo
    ierr = None
    #NOTONA devuelve el nombre extendido de 18 caracteres para el numero de barra identificado
    ierr,nombre=psspy.notona(ibus)
    if (ierr == 1):
        error='***** ERROR EN LOS DATOS DE FLUJO ***** NO SE ENCUENTRA LA BARRA, '+str(ibus)+', '+nombre
        informe.Reserva_err(ruta,error)
    elif(ierr == 2):
        error='***** ERROR EN LOS DATOS DE FLUJO ***** NO SE ENCUENTRA LA BARRA, '+str(ibus)+', '+nombre
        informe.Reserva_err(ruta,error)

    id=str(id)
    #MACDT2 devuelve las cantidades complejas de la maquina
    ierr,cmpval = psspy.macdt2(ibus, id, "PQ")
    if(ierr==1):
        error='***** ERROR EN LOS DATOS DE FLUJO ***** NO SE ENCUENTRA LA BARRA, '+str(ibus)+', '+nombre
        informe.Reserva_err(ruta,error)
    elif(ierr==2):
        error='EN LA BARRA, '+str(ibus)+', '+nombre+', NO EXISTEN MÁQUINAS CONECTADAS'
        informe.Reserva_err(ruta,error)
    elif(ierr==3):
        error='EN LA BARRA, '+str(ibus)+', '+nombre+', NO EXISTEN MÁQUINAS CONECTADAS'
        informe.Reserva_err(ruta,error)
    elif(ierr==4):
        error='LA BARRA, '+str(ibus)+', '+nombre+', TIENE GENERADORES FUERA DE SERVICIO'
        informe.Reserva_err(ruta,error)
    elif(ierr==5):
        error='***** ERROR EN PROGRAMA IPLAN ***** ERROR EN LOS DATOS DE FLUJO ***** LA BARRA, '+str(ibus)+', '+nombre+'ERROR EN EL STRING PQ'
        informe.Reserva_err(ruta,error)
    elif(ierr==6):
        error='***** ERROR EN LOS DATOS DE FLUJO ***** PARA LA BARRA, '+str(ibus)+', '+nombre+' NO HAY DATOS DE SECUENCIA'
        informe.Reserva_err(ruta,error)


    #MACDAT devuelve las cantidaes reales de la maquina-- devuelve en este caso el total de MVA base
    ierr,v = psspy.macdat(ibus,id,"MBASE")
    if(ierr==1):
        error='***** ERROR EN LOS DATOS DE FLUJO ***** NO SE ENCUENTRA LA BARRA, '+str(ibus)+', '+nombre
        informe.Reserva_err(ruta,error)
    elif(ierr==2):
        error='***** ERROR EN LOS DATOS DE FLUJO ***** NO ENCUENTRO LA MÁQUINA, '+id+', EN LA BARRA, '+str(ibus)+', '+nombre
        informe.Reserva_err(ruta,error)
    elif(ierr==3):
        error='EN BARRA, '+str(ibus)+', '+nombre+', NO EXISTEN MÁQUINAS CONECTADAS'
        informe.Reserva_err(ruta,error)
    elif(ierr==4):
        error='LA BARRA, '+str(ibus)+', '+nombre+', TIENE GENERADORES FUERA DE SERVICIO'
        informe.Reserva_err(ruta,error)
    elif(ierr==5):
        error='***** ERROR EN LOS DATOS DE FLUJO ***** LA BARRA, '+str(ibus)+', '+nombre+' LA CADENA DE CARACTERES -MBASE- ES INCORRECTA'
        informe.Reserva_err(ruta,error)
   

    #MACDAT devuelve las cantidaes reales de la maquina-- devuelve en este caso la potencia maxima de salida del generador
    ierr,v1 = psspy.macdat(ibus,id,"PMAX")
    if(ierr==1):
        error='***** ERROR EN LOS DATOS DE FLUJO ***** NO SE ENCUENTRA LA BARRA, '+str(ibus)+', '+nombre
        informe.Reserva_err(ruta,error)
    elif(ierr==2):
        error=('NO ENCUENTRO LA MÁQUINA, '+id+', EN LA BARRA, '+str(ibus)+', '+nombre)
        informe.Reserva_err(ruta,error)
    elif(ierr==3):
        error='EN BARRA, '+str(ibus)+', '+nombre+', NO EXISTEN MÁQUINAS CONECTADAS'
        informe.Reserva_err(ruta,error)
    elif(ierr==4):
        error='LA BARRA, '+str(ibus)+', '+nombre+', TIENE GENERADORES FUERA DE SERVICIO'
        informe.Reserva_err(ruta,error)
    elif(ierr==5):
        error='***** ERROR EN LOS DATOS DE FLUJO ***** LA BARRA, '+str(ibus)+', '+nombre+' LA CADENA DE CARACTERES -PMAX- ES INCORRECTA'
        informe.Reserva_err(ruta,error)

    #MDLIND devuelve el indice del comienzo del arreglo del modelo y el status
    ierr,indice_ini = psspy.mdlind(ibus, id,"GOV","CON")
    if(ierr==1):
        error='***** ERROR EN LOS DATOS DE FLUJO O DINAMICOS ***** NO SE ENCUENTRA LA MÁQUINA, '+id+', EN LA BARRA, '+str(ibus)+', '+nombre+', EN LA RED'
        informe.Reserva_err(ruta,error)
        error='PERO SI SE ENCUENTRA EN LOS DATOS DINÁMICOS Y EL MODELO DE REGULADOR EXISTE'
        informe.Reserva_err(ruta,error)
    elif(ierr==2):
        error='***** ERROR EN LOS DATOS DE FLUJO O DINAMICOS ***** NO SE ENCUENTRA LA MÁQUINA {id} EN LA BARRA'+ str(ibus)+' '+str(nombre) +'EN LA RED'
        informe.Reserva_err(ruta,error)
        error='O NO SE ENCUENTRA EN LOS DATOS DINÁMICOS Y EL MODELO DE REGULADOR'
        informe.Reserva_err(ruta,error)
    elif(indice_ini==0):
        error='***** POSIBLE ERROR EN LOS DATOS DE FLUJO O DINAMICOS *****''MÁQUINA' + str(id)+ 'EN LA BARRA' +str(ibus)+' '+ str(nombre)+'ORDEN DE CON=0'
        informe.Reserva_err(ruta,error)

    #DSRVAL devuelve los valores reales dinamicos-- en este caso devuelve los parametros reales del modelo
    ierr,rval = psspy.dsrval("CON",(indice_ini+i5))
    if(ierr==1):
        error='***** ERROR EN LOS DATOS DINAMICOS ***** LA BARRA '+str(ibus) + ' '+ str(nombre)+'NOMBRE DEL ARRAY ERRONEO'
        informe.Reserva_err(ruta,error)
    elif(ierr==2):
        error='***** ERROR EN LOS DATOS DINAMICOS ***** LA BARRA '+str(ibus) + ' '+ str(nombre)+'INDICE DEL ARRAY ERRONEO VERIFIQUE EL ORDEN DE ICON EN ARCHIVO reserva.DAT'
        informe.Reserva_err(ruta,error)
    if ierr==None:
        ierr=0
    return(nombre, cmpval, v, v1, indice_ini, rval, ierr)


def gensale(ruta, nombre_archivo, ibus,nombre,id):
    '''
    Función que verifica los datos obtenidos del archivo "gensale.prn"
    
    :param ruta: ruta del archivo
    :param nombre_archivo: nombre del archivo
    :param ibus: numero de barra
    :param nombre: nombre de la barra
    :param id: id del generador
    '''
    id = str(id)
    ierr = None
    '''Función para verificar los datos de gensale.prn'''
    ierr,ival=psspy.busint(ibus,'TYPE')
    if(ierr==1):
        error= '***** ERROR EN LOS DATOS DE GENSALE.PRN ***** NO SE ENCUENTRA LA BARRA ' + str(ibus) + ' ' + nombre
        informe.Reserva_err(ruta,nombre_archivo, error)
    if (ierr==2):
        error='***** ERROR EN LOS DATOS DE GENSALE.PRN ***** ERROR EN EL STRING'
        informe.Reserva_err(ruta,nombre_archivo, error)

    ierr,cmpval=psspy.macdt2(ibus,id,'PQ')

    if(ierr==1):
        error='***** ERROR EN LOS DATOS DE GENSALE.PRN ***** NO SE ENCUENTRA LA BARRA ' + str(ibus) + ' ' + nombre
        informe.Reserva_err(ruta,nombre_archivo, error)  

    if(ierr==2):
        error='***** ERROR EN LOS DATOS DE GENSALE.PRN ***** EN LA BARRA ' + str(ibus) + ' ' + nombre + ' NO EXISTEN MÁQUINAS CONECTADAS'
        informe.Reserva_err(ruta,nombre_archivo, error)

    if(ierr==3) :
        error='***** ERROR EN LOS DATOS DE GENSALE.PRN ***** EN LA BARRA ' + str(ibus) + ' ' + nombre + ' NO EXISTEN MÁQUINAS CONECTADAS'
        informe.Reserva_err(ruta,nombre_archivo, error)
        pge=0.0
        qge=0.0

    if(ierr==4) :
        error='***** ERROR EN LOS DATOS DE GENSALE.PRN ***** LA BARRA ' + str(ibus) + ' ' + nombre + ' TIENE GENERADORES FUERA DE SERVICIO'
        informe.Reserva_err(ruta,nombre_archivo, error)    
        pge=0.0
        qge=0.0

    if(ierr==5) :
        error='***** ERROR EN PROGRAMA IPLAN ***** ERROR EN LOS DATOS DE GENSALE.PRN *****''LA BARRA '+str(ibus)+' '+str(nombre)+'ERROR EN EL STRING PQ'
        informe.Reserva_err(ruta,nombre_archivo, error)    

    if(ierr==6) :
        error='***** ERROR EN LOS DATOS DE GENSALE.PRN ***** PARA LA BARRA '+str(ibus)+' '+str(nombre)+' NO HAY DATOS DE SECUENCIA'
        informe.Reserva_err(ruta,nombre_archivo, error)
    if ierr==None:
        ierr=0
    return(cmpval, ierr)

def area (ruta, nombre_archivo,iarea,nombre_area):
    '''
    Función que verifica los datos obtenidos del archivo "reserva.dat"

    :param ruta: ruta del archivo
    :param nombre_archivo: nombre del archivo
    :param iarea: numero de area
    :param nombre_area: nombre del area
    '''
    ierr = None
    ierr,cmpva_area=psspy.ardat(iarea,'GEN')
    if(ierr==1):
        error='***** ERROR EN LOS DATOS DE reserva_DEMANDAS ***** NO SE ENCUENTRA EL AREA INDICADA COMO ' + str(iarea)+' '+str(nombre_area)
        informe.Reserva_err(ruta,nombre_archivo,error)    

    if(ierr==2):
        error='***** ERROR EN LOS DATOS DE reserva_DEMANDAS ***** EL AREA INDICADA COMO ' + str(iarea) + ' ' + str(nombre_area) + ' NO POSEE SISTEMA'
        informe.Reserva_err(ruta,nombre_archivo,error)
    if(ierr==3):
        error='***** ERROR EN LOS DATOS DE reserva_DEMANDAS ***** EL AREA INDICADA COMO ' + str(iarea) + ' ' + str(nombre_area) + ' NO POSEE SISTEMA'
        informe.Reserva_err(ruta,nombre_archivo,error)   

    #CALL ARDAT(iarea,'INT',PiA,QiA,ierr) revisar esto
    if ierr==None:
        ierr=0
    return(cmpva_area, ierr)

 
#Datos de salida para este modulo:
#nombre-> nombre completo del generador
#cmpval-> valores complejos de la maquina P y Q 
#v-> total de MVA
#v1-> potencia de salida maxima
#indice_ini-> el indice de comienzo del modelo
#rval-> parametros reales del modelo dinamico