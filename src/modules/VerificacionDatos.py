#Datos de entrada para este modulo
#ibus numero de barra
#id id del generador
#i5-> CON a cambiar
import os
import sys

sys_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSPY34'
sys.path.append(sys_path_PSSE)
sys_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\ssssPSSPY34'
sys.path.append(r'C:/Users/juan/AppData/Local/Programs/Python/Python312/Lib/site-packages')

os_path_PSSE=r'E:\PSS\PSSBIN'
os.environ['PATH'] += ';' + os_path_PSSE
os.environ['PATH'] += ';' + sys_path_PSSE

import psspy

def generadores(ibus,id,i5):
    '''
    Función que verifica los datos obtenidos del archivo"reserva.dat"
    Los parámetros de la funcion son 
    ibus
    id
    i5(CON)
    nombre
    '''

    #NOTONA devuelve el nombre extendido de 18 caracteres para el numero de barra identificado
    ierr,nombre=psspy.notona(ibus)
    if (ierr == 1):
        print('***** ERROR EN LOS DATOS DE FLUJO *****\nNO SE ENCUENTRA LA BARRA, ',ibus, ', ',nombre,'\n')
    elif(ierr == 2):
        print('***** ERROR EN LOS DATOS DE FLUJO *****\nNOMBRE DE LA BARRA ,',ibus,', ',nombre,', MENOR A 12 CARACTERES\n')

    id=str(id)
    #MACDT2 devuelve las cantidades complejas de la maquina
    ierr,cmpval = psspy.macdt2(ibus, id, "PQ")
    if(ierr==1):
        print('***** ERROR EN LOS DATOS DE FLUJO ***** \nNO SE ENCUENTRA LA BARRA , ',ibus,',', {nombre},'\n')
    elif(ierr==2):
        print('EN LA BARRA ',ibus,',', nombre,' NO EXISTEN MÁQUINAS CONECTADAS\n')
    elif(ierr==3):
        print('EN BARRA ' , ibus, nombre,' NO EXISTEN MÁQUINAS CONECTADAS\n')
    elif(ierr==4):
        print('LA BARRA', ibus, nombre,' TIENE GENERADORES FUERA DE SERVICIO\n')
    elif(ierr==5):
        print('***** ERROR EN PROGRAMA IPLAN *****\nLA BARRA ',ibus, nombre,'\nERROR EN EL STRING PQ')
    elif(ierr==6):
        print('***** ERROR EN LOS DATOS DE FLUJO *****\nPARA LA BARRA ',ibus,nombre,'\nNO HAY DATOS DE SECUENCIA\n')


    #MACDAT devuelve las cantidaes reales de la maquina-- devuelve en este caso el total de MVA base
    ierr,v = psspy.macdat(ibus,id,"MBASE")
    if(ierr==1):
        print('***** ERROR EN LOS DATOS DE FLUJO *****\nNO SE ENCUENTRA LA BARRA', ibus, nombre,'\n')
    elif(ierr==2):
        print('***** ERROR EN LOS DATOS DE FLUJO *****\nNO ENCUENTRO LA MÁQUINA, ',id, 'EN LA BARRA',ibus, nombre,'\n')
    elif(ierr==3):
        print('EN BARRA,', ibus, nombre,' NO EXISTEN MÁQUINAS CONECTADAS\n')
    elif(ierr==4):
        print('LA BARRA' ,ibus, nombre, 'TIENE GENERADORES FUERA DE SERVICIO')
    elif(ierr==5):
        print('***** ERROR EN LOS DATOS DE FLUJO *****\nLA BARRA, ',ibus, nombre,'\nLA CADENA DE CARACTERES -MBASE- ES INCORRECTA\n')
   

    #MACDAT devuelve las cantidaes reales de la maquina-- devuelve en este caso la potencia maxima de salida del generador
    ierr,v1 = psspy.macdat(ibus,id,"PMAX")
    if(ierr==1):
        print('***** ERROR EN LOS DATOS DE FLUJO *****\nNO SE ENCUENTRA LA BARRA' ,ibus, nombre,'\n')
    elif(ierr==2):
        print('NO ENCUENTRO LA MÁQUINA', id,'EN LA BARRA', ibus, nombre,'\n')
    elif(ierr==3):
        print('EN BARRA' ,ibus,nombre,'NO EXISTEN MÁQUINAS CONECTADAS\n')
    elif(ierr==4):
        print('LA BARRA',ibus ,nombre,'TIENE GENERADORES FUERA DE SERVICIO\n')
    elif(ierr==5):
        print('***** ERROR EN LOS DATOS DE FLUJO *****\nLA BARRA ',ibus, nombre,'\nLA CADENA DE CARACTERES -PMAX- ES INCORRECTA\n')  


    #MDLIND devuelve el indice del comienzo del arreglo del modelo y el status
    ierr,indice_ini = psspy.mdlind(ibus, id,"GOV","CON")
    if(ierr==1):
        print('***** ERROR EN LOS DATOS DE FLUJO O DINAMICOS *****\nNO SE ENCUENTRA LA MÁQUINA' ,id, 'EN LA BARRA' ,ibus, nombre, 'EN LA RED\n') 
        print('PERO SI SE ENCUENTRA EN LOS DATOS DINÁMICOS Y EL MODELO DE REGULADOR EXISTE\n')
    elif(ierr==2):
        print('***** ERROR EN LOS DATOS DE FLUJO O DINAMICOS *****\n')    
        print('NO SE ENCUENTRA LA MÁQUINA {id} EN LA BARRA', ibus, nombre, 'EN LA RED\n')  
        print('O NO SE ENCUENTRA EN LOS DATOS DINÁMICOS Y EL MODELO DE REGULADOR\n')
    elif(indice_ini==0):
        print('***** POSIBLE ERROR EN LOS DATOS DE FLUJO O DINAMICOS *****\n')
        print('MÁQUINA' ,id, 'EN LA BARRA', ibus, nombre,'\n')
        print('ORDEN DE CON=0\n')


    #DSRVAL devuelve los valores reales dinamicos-- en este caso devuelve los parametros reales del modelo
    ierr,rval = psspy.dsrval("CON",(indice_ini+i5))
    if(ierr==1):
        print('***** ERROR EN LOS DATOS DINAMICOS *****\n')
        print('LA BARRA ', ibus, nombre,'\n')     
        print('NOMBRE DEL ARRAY ERRONEO\n')
    elif(ierr==2):
        print('***** ERROR EN LOS DATOS DINAMICOS *****\n')    
        print('LA BARRA', ibus, nombre,'INDICE DEL ARRAY ERRONEO\n')  
        print('VERIFIQUE EL ORDEN DE ICON EN ARCHIVO reserva.DAT\n')
    return(nombre, cmpval,v,v1, indice_ini,rval)


def gensale(ibus,nombre,id):
    id=str(id)
    '''Función para verificar los datos de gensale.prn'''
    ierr,ival=psspy.busint(ibus,'TYPE')
    if(ierr==1):
        print('***** ERROR EN LOS DATOS DE GENSALE.PRN *****')
        print('NO SE ENCUENTRA LA BARRA ',ibus,' ',nombre)
        print(' ')
    #if (ival==4):

    #if (ival==1):

    ierr,cmpval=psspy.macdt2(ibus,id,'PQ')

    if(ierr==1):
        print('***** ERROR EN LOS DATOS DE GENSALE.PRN *****')  
        print('NO SE ENCUENTRA LA BARRA ',ibus ,' ',nombre)
        print(' ')

    if(ierr==2):
        print('***** ERROR EN LOS DATOS DE GENSALE.PRN *****')
        print('EN LA BARRA ',ibus,' ',nombre ,' NO EXISTEN MÁQUINAS CONECTADAS')
        print(' ')

    if(ierr==3) :
        print('***** ERROR EN LOS DATOS DE GENSALE.PRN *****')
        print('EN BARRA ',ibus,' ',nombre ,' NO EXISTEN MÁQUINAS CONECTADAS')
        print(' ')
        pge=0.0
        qge=0.0

    if(ierr==4) :
        print('***** ERROR EN LOS DATOS DE GENSALE.PRN *****')    
        print('LA BARRA ',ibus,' ',nombre ,' TIENE GENERADORES FUERA DE SERVICIO')
        print(' ')
        pge=0.0
        qge=0.0

    if(ierr==5) :
        print('***** ERROR EN PROGRAMA IPLAN *****')    
        print('***** ERROR EN LOS DATOS DE GENSALE.PRN *****')    
        print('LA BARRA ',ibus,' ',nombre)
        print('ERROR EN EL STRING PQ')
        print(' ')

    if(ierr==6) :
        print('***** ERROR EN LOS DATOS DE GENSALE.PRN *****')    
        print('PARA LA BARRA ',ibus,' ',nombre) 
        print('NO HAY DATOS DE SECUENCIA')
        print(' ')
    
    return(cmpval)

def area (iarea,nombre_area):
    ierr,cmpva_area=psspy.ardat(iarea,'GEN')
    if(ierr==1):
        print('***** ERROR EN LOS DATOS DE reserva_DEMANDAS *****')    
        print('NO SE ENCUENTRA EL AREA INDICADA COMO ',iarea ,' ',nombre_area)
        print(' ')
        print('***** ERROR EN LOS DATOS DE reserva_DEMANDAS *****')   
        print('NO SE ENCUENTRA EL AREA INDICADA COMO ',iarea ,' ',nombre_area)
        print(' ')

    if(ierr==2):
        print('***** ERROR EN LOS DATOS DE reserva_DEMANDAS *****')    
        print('EL AREA INDICADA COMO ',iarea ,' ',nombre_area,' NO POSEE SYSTEMA')
        print(' ')
        print('***** ERROR EN LOS DATOS DE reserva_DEMANDAS *****')    
        print('EL AREA INDICADA COMO ',iarea ,' ',nombre_area,' NO POSEE SYSTEMA')
        print(' ')

    if(ierr==3):
        print('***** ERROR EN LOS DATOS DE reserva_DEMANDAS *****')    
        print('ERROR EN EL STRING ')
        print(' ')
        print('***** ERROR EN LOS DATOS DE reserva_DEMANDAS *****')    
        print('ERROR EN EL STRING ')
        print(' ')

    #CALL ARDAT(iarea,'INT',PiA,QiA,ierr) revisar esto
    
    return(cmpva_area)
#Datos de salida para este modulo:
#nombre-> nombre completo del generador
#cmpval-> valores complejos de la maquina P y Q 
#v-> total de MVA
#v1-> potencia de salida maxima
#indice_ini-> el indice de comienzo del modelo
#rval-> parametros reales del modelo dinamico