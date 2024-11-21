#comienza en linea 2205

#ver que hacer con el limite nuevo en cada caso, es decir si cambiarlo en cada funcion o cambiarlo luego


import os
import sys

sys_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSPY34'
sys.path.append(sys_path_PSSE)
sys_path_PSSE=r'E:\PSS\PSSPY34'


os_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSBIN'
os.environ['PATH'] += ';' + os_path_PSSE
os.environ['PATH'] += ';' + sys_path_PSSE

import psspy

def cambiar_limites(nombre,indice_ini,rval, v, P,difnue, pmaxinue,CON):
    if nombre=='BSASGO':
        BSASGO(indice_ini,pmaxinue,CON)
    '''if nombre=='RAVYA3':
        RAVYA3(indice_ini,rval,P,difnue,pmaxinue,pmaxinue,CON)'''
    if nombre=='GAST2A':
        GAST2A(indice_ini, pmaxinue, CON)
    if nombre=='GAST':
        GAST(indice_ini, v, pmaxinue, CON)
    if nombre=='GASTWD':
        GASTWD(indice_ini, pmaxinue, CON)
    if nombre=='HYGOV':
        HYGOV(indice_ini,v, pmaxinue, CON)
    if nombre=='HYGV5P':
        HYGV5P(indice_ini, pmaxinue, CON)
    if nombre=='HYGV7P':
        HYGV7P(indice_ini, pmaxinue, CON)
    if nombre=='IEEEG1':
        IEEEG1(indice_ini, v, pmaxinue, CON)
    if nombre=='IEEEG3':
        IEEEG3(indice_ini, v, pmaxinue, CON)
    if nombre=='IEEEG2':
        IEEEG2(indice_ini, v, pmaxinue, CON)
    if nombre=='IEESGO':
        IEESGO(indice_ini, v, pmaxinue, CON)
    if nombre=='STGV1P':
        STGV1P(indice_ini, pmaxinue, CON)
    if nombre=='STGV4P':
        STGV4P(indice_ini, pmaxinue, CON)
    if nombre=='STGV2P':
        STGV2P(indice_ini, pmaxinue, CON)
    if nombre=='TGOV1':
        TGOV1(indice_ini, v, pmaxinue, CON)
    if nombre=='WPIDHY':
        WPIDHY(indice_ini, v, pmaxinue, CON)
    if nombre=='GAST5':
        GAST5(indice_ini, v, pmaxinue, CON)
    if nombre=='SIE943':
        SIE943(indice_ini, pmaxinue, CON)
    if nombre=='TUCUGO':
        TUCUGO(indice_ini, pmaxinue, CON)
    if nombre=='GASV94':
        GASV94(indice_ini, pmaxinue, CON)
    return

def BSASGO(indice_ini, pmaxinue, CON):
    ierr,rval1=psspy.dsrval('CON',(indice_ini+15))
    ierr,rval3=psspy.dsrval('CON',(indice_ini+11))
    limnue=pmaxinue/(rval1*rval3)
    psspy.change_con(indice_ini+CON,limnue)

    return
''' hay que revisar este
def RAVYA3(indice_ini, rval,pmaxinue,CON):
        potencia_maxima=rval
        psspy.change_con(indice_ini+CON,pmaxinue)
        reserva=potencia_maxima-potencia
    return'''

def GAST2A(indice_ini, pmaxinue, CON):
    
    ierr,rval22=psspy.dsrval('CON',(indice_ini+14))
    ierr,rval20=psspy.dsrval('CON',(indice_ini+16))
    ierr,rval8=psspy.dsrval('CON',(indice_ini+6))   
    ierr,rval2=psspy.dsrval('CON',(indice_ini+25))         
    ierr,rval3=psspy.dsrval('CON',(indice_ini+12))   
    ierr,rval4=psspy.dsrval('CON',(indice_ini+26))
    ierr,rval5=psspy.dsrval('CON',(indice_ini+29)) 
    ierr,rval6=psspy.dsrval('CON',(indice_ini+8))           
    ierr,rval7=psspy.dsrval('CON',(indice_ini+11))

    c=rval22
    kf=rval20
    trate=rval8
    af2=rval2
    a=rval3
    bf2=rval4
    k6=rval5
    max=rval6
    k3=rval7
                
    limnue=(((pmaxinue/trate)-af2)/(bf2*(a/(c+a*kf)))-k6)/k3
        
    psspy.change_con(indice_ini+CON,limnue)
        
    return

def GAST(indice_ini, v, pmaxinue, CON):
    limnue=pmaxinue/v

    psspy.change_con(indice_ini+CON,limnue)

    return 

def GASTWD(indice_ini, pmaxinue, CON):
    ierr,rval22=psspy.dsrval('CON',(indice_ini+14))
    ierr,rval20=psspy.dsrval('CON',(indice_ini+16))
    ierr,rval8=psspy.dsrval('CON',(indice_ini+6)) 
    ierr,rval2=psspy.dsrval('CON',(indice_ini+25)) 
    ierr,rval3=psspy.dsrval('CON',(indice_ini+12))
    ierr,rval4=psspy.dsrval('CON',(indice_ini+26))
    ierr,rval5=psspy.dsrval('CON',(indice_ini+29)) 
    ierr,rval6=psspy.dsrval('CON',(indice_ini+8))
    ierr,rval7=psspy.dsrval('CON',(indice_ini+11))
    c=rval22
    kf=rval20
    trate=rval8
    af2=rval2
    a=rval3
    bf2=rval4
    k6=rval5
    max=rval6
    k3=rval7          
    limnue=(((pmaxinue/trate)-af2)/(bf2*(a/(c+a*kf)))-k6)/k3
    psspy.change_con(indice_ini+CON,limnue)

    return 

def HYGOV(indice_ini, v, pmaxinue, CON):
    ierr,rval20=psspy.dsrval('CON',(indice_ini+11))
    ierr,rval22=psspy.dsrval('CON',(indice_ini+9))
    limnue=(pmaxinue/(v*rval22))+rval20
    psspy.change_con(indice_ini+CON,limnue)

    return 

def HYGV5P(indice_ini, pmaxinue, CON):
    ierr,rval1=psspy.dsrval('CON',(indice_ini+22))
    limnue=pmaxinue/rval1
    psspy.change_con(indice_ini+CON,limnue)
    
    return 

def HYGV7P (indice_ini, pmaxinue, CON):
    ierr,rval1=psspy.dsrval('CON',(indice_ini+18))
    limnue=pmaxinue/rval1
    psspy.change_con(indice_ini+CON,limnue)

    return 

def IEEEG1(indice_ini, v, pmaxinue, CON):
    limnue=pmaxinue/v
    psspy.change_con(indice_ini+CON,limnue)

    return 

def IEEEG3 (indice_ini, v, pmaxinue, CON):
    limnue=pmaxinue/v
    psspy.change_con(indice_ini+CON,limnue)

    return 
        
def IEEEG2(indice_ini, v, pmaxinue, CON):
    limnue=pmaxinue/v
    psspy.change_con(indice_ini+CON,limnue)

    return 

def IEESGO (indice_ini, v, pmaxinue, CON):
    limnue=pmaxinue/v
    psspy.change_con(indice_ini+CON,limnue)

    return 
  
def STGV1P(indice_ini, pmaxinue, CON):
    ierr, rval1=psspy.dsrval('CON',(indice_ini+21))
    limnue=pmaxinue/rval1
    psspy.change_con(indice_ini+CON,limnue)
 
    return  

def STGV4P(indice_ini, pmaxinue, CON):
    ierr,rval1=psspy.dsrval('CON',(indice_ini+21))
    limnue=pmaxinue/(rval1)
    psspy.change_con(indice_ini+CON,limnue)

    return 

def STGV2P (indice_ini, pmaxinue, CON):
    ierr,rval1=psspy.dsrval('CON',(indice_ini+18))
    limnue=pmaxinue/rval1
    psspy.change_con(indice_ini+CON,limnue)

    return 

def TGOV1(indice_ini, v, pmaxinue, CON):
    limnue=pmaxinue/v
    psspy.change_con(indice_ini+CON,limnue)

    return 

def WPIDHY (indice_ini, v, pmaxinue, CON):
    limnue=pmaxinue/v
    psspy.change_con(indice_ini+CON,limnue)

    return 

def GAST5(indice_ini, v, pmaxinue, CON):
    ierr,rval1=psspy.dsrval('CON',(indice_ini+9))
    limnue=(pmaxinue/v)+rval1
    psspy.change_con(indice_ini+CON,limnue)

    return 

def SIE943(indice_ini, pmaxinue, CON):
    ierr,af1=psspy.dsrval('CON',(indice_ini+23))
    ierr,bf1=psspy.dsrval('CON',(indice_ini+24))
    ierr,af2=psspy.dsrval('CON',(indice_ini+34))            
    ierr,bf2=psspy.dsrval('CON',(indice_ini+35))
    ierr,af3=psspy.dsrval('CON',(indice_ini+37)) 
    ierr,bf3=psspy.dsrval('CON',(indice_ini+38))
    ierr,cf3=psspy.dsrval('CON',(indice_ini+39))
    ierr,df3=psspy.dsrval('CON',(indice_ini+40))
    ierr,tlim=psspy.dsrval('CON',(indice_ini+47))
    ierr,tamb=psspy.dsrval('CON',(indice_ini+60))
    ierr,rval1=psspy.dsrval('CON',(indice_ini+6))                     
    rQg=((pmaxinue/rval1)-bf1)/af1
    limnue=-(((rQg*cf3+df3-tlim+af3*tamb)/bf3)+bf2)/af2
    psspy.change_con(indice_ini+CON,limnue)

    return 

def TUCUGO(indice_ini, pmaxinue, CON):
    ierr,rval3=psspy.dsrval('CON',(indice_ini+11))
    ierr,rval4=psspy.dsrval('CON',(indice_ini+14))      
    limnue=((pmaxinue/rval1)+rval4)/rval3
    psspy.change_con(indice_ini+CON,limnue)

    return 

def GASV94 (indice_ini, pmaxinue, CON):
    ierr,rval1=psspy.dsrval('CON',(indice_ini+50))
    ierr,af6=psspy.dsrval('CON',(indice_ini+61))   
    ierr,tamb=psspy.dsrval('CON',(indice_ini+53))
    ierr,bf6=psspy.dsrval('CON',(indice_ini+62))
    ierr,af4=psspy.dsrval('CON',(indice_ini+57))
    ierr,bf4=psspy.dsrval('CON',(indice_ini+58))
    ierr,df6=psspy.dsrval('CON',(indice_ini+64))
    ierr,cf6=psspy.dsrval('CON',(indice_ini+63))
    ierr,bf5=psspy.dsrval('CON',(indice_ini+60))

    RQg=((pmaxinue/rval1)-bf5)/bf5
    limnue=(RQg*cf6)+df6+bf6*(af4+bf4)+af6*tamb
    psspy.change_con(indice_ini+CON,limnue)

    return 


