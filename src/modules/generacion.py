import os
import sys

sys_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSPY34'
sys.path.append(sys_path_PSSE)
sys_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\sssssPSSPY34'
sys.path.append(r'C:/Users/juan/AppData/Local/Programs/Python/Python312/Lib/site-packages')

os_path_PSSE=r'E:\PSS\PSSBIN'
os.environ['PATH'] += ';' + os_path_PSSE
os.environ['PATH'] += ';' + sys_path_PSSE

import psspy

def total():
    ierr, cmpval = psspy.systot('GEN')

    if(ierr)==2:
        print('**** ERROR EN EL SISTEMA *****')
        print('NO SE ENCUENTRAN BARRAS EN EL CASO EN ESTUDIO')
        print(' ')
    #write 2; '**** ERROR EN EL SISTEMA *****'
    #write 2; 'NO SE ENCUENTRAN BARRAS EN EL CASO EN ESTUDIO'
    #write 2; ' '

    if(ierr)==1:
        print('***** ERROR EN LOS DATOS DE reserva_DEMANDAS *****'  )  
        print('ERROR EN EL STRING ')
        print(' ')
    #write 2; '***** ERROR EN LOS DATOS DE reserva_DEMANDAS *****'    
    #write 2; 'ERROR EN EL STRING '
    #write 2; ' '

    for pq in cmpval:
        p=pq.real
        q=pq.imag
    return p,q