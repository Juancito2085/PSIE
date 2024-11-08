import os
import sys

sys_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSPY34'
sys.path.append(sys_path_PSSE)

 
os_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSBIN'
os.environ['PATH'] += ';' + os_path_PSSE
os.environ['PATH'] += ';' + sys_path_PSSE

import psspy
import modules.informe as informe

ruta='C:/Users/jcbru/Desktop/psie'

def total():
    ierr, cmpval = psspy.systot('GEN')

    if(ierr)==2:
        error='***** ERROR EN EL SISTEMA ***** NO SE ENCUENTRAN BARRAS EN EL CASO EN ESTUDIO'
        informe.Reserva_err(ruta,error)

    if(ierr)==1:
        error='***** ERROR EN LOS DATOS DE reserva_DEMANDAS ***** ERROR EN EL STRING '
        informe.Reserva_err(ruta,error)

    p=cmpval.real
    q=cmpval.imag
 
    return(p,q)
