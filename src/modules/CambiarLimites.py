#comienza en linea 2205

#ver que hacer con el limite nuevo en cada caso, es decir si cambiarlo en cada funcion o cambiarlo luego


import os
import sys

sys_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSPY34'
sys.path.append(sys_path_PSSE)
sys_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSPY34'
sys.path.append(r'C:/Users/juan/AppData/Local/Programs/Python/Python312/Lib/site-packages')

os_path_PSSE=r'E:\PSS\PSSBIN'
os.environ['PATH'] += ';' + os_path_PSSE
os.environ['PATH'] += ';' + sys_path_PSSE

import psspy

def cambiar_limites(nombre,indice_ini,rval, v, normal,difnue, pmaxinue, pmaxinue2,CON):
    if nombre=='HYGOV':
        HYGOV(indice_ini,normal, difnue, pmaxinue, pmaxinue2, CON)
    if nombre=='TGOV1':
        TGOV1(normal,difnue, pmaxinue, pmaxinue2,v, indice_ini,CON)
    return

def HYGOV(indice_ini,normal, difnue, pmaxinue, pmaxinue2, CON):
    ierr,rval20=psspy.dsrval('CON',(indice_ini+11))
    ierr,rval22=psspy.dsrval('CON',(indice_ini+9))
    if (difnue>0):
        if(normal==1):
            limnue=(pmaxinue2/(v*rval22))+rval20
        else:
            limnue=(pmaxinue/(v*rval22))+rval20
        psspy.change_con(indice_ini+CON,limnue)
    return

def TGOV1(normal,difnue, pmaxinue, pmaxinue2,v, indice_ini,CON):
    if (difnue>0):
        if(normal==1):
            limnue=pmaxinue2/v
        else:
            limnue=pmaxinue/v
        psspy.chage_con(indice_ini+CON,limnue)
    return
