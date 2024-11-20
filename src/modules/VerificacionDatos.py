#Datos de entrada para este modulo
#ibus numero de barra
#id id del generador
#i5-> CON a cambiar
import os
import sys

sys_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSPY34'
sys.path.append(sys_path_PSSE)

 
os_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSBIN'
os.environ['PATH'] += ';' + os_path_PSSE
os.environ['PATH'] += ';' + sys_path_PSSE


import psspy
import modules.informe as informe

def generadores(ruta, nombre_archivo,ibus,id,i5):
    '''
    Función que verifica los datos obtenidos del archivo"reserva.dat"
    Los parámetros de la funcion son 
    ibus
    id
    i5(CON)
    nombre
    '''
    ruta=ruta+'/'+nombre_archivo

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
    return(nombre, cmpval,v,v1, indice_ini,rval)


def gensale(ruta, nombre_archivo, ibus,nombre,id):
    id=str(id)
    '''Función para verificar los datos de gensale.prn'''
    ierr,ival=psspy.busint(ibus,'TYPE')
    if(ierr==1):
        error= '***** ERROR EN LOS DATOS DE GENSALE.PRN ***** NO SE ENCUENTRA LA BARRA ' + str(ibus) + ' ' + nombre
        informe.Reserva_err(ruta,nombre_archivo, error)
    #if (ival==4):

    #if (ival==1):

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
    
    return(cmpval)

def area (ruta, nombre_archivo,iarea,nombre_area):

    ierr,cmpva_area=psspy.ardat(iarea,'GEN')
    if(ierr==1):
        error='***** ERROR EN LOS DATOS DE reserva_DEMANDAS ***** NO SE ENCUENTRA EL AREA INDICADA COMO ' + str(iarea)+' '+str(nombre_area)
        informe.Reserva_err(ruta,nombre_archivo,error)    

    if(ierr==2):
        error='***** ERROR EN LOS DATOS DE reserva_DEMANDAS ***** EL AREA INDICADA COMO ' + str(iarea) + ' ' + str(nombre_area) + ' NO POSEE SYSTEMA'
        informe.Reserva_err(ruta,nombre_archivo,error)
    if(ierr==3):
        error='***** ERROR EN LOS DATOS DE reserva_DEMANDAS ***** EL AREA INDICADA COMO ' + str(iarea) + ' ' + str(nombre_area) + ' NO POSEE SYSTEMA'
        informe.Reserva_err(ruta,nombre_archivo,error)   

    #CALL ARDAT(iarea,'INT',PiA,QiA,ierr) revisar esto
    
    return(cmpva_area)

 
#Datos de salida para este modulo:
#nombre-> nombre completo del generador
#cmpval-> valores complejos de la maquina P y Q 
#v-> total de MVA
#v1-> potencia de salida maxima
#indice_ini-> el indice de comienzo del modelo
#rval-> parametros reales del modelo dinamico