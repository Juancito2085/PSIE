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
    '''if nombre=='BSASGO':
        BSASGO(indice_ini, P,normal,difnue,pmaxinue,pmaxinue,CON)
    if nombre=='RAVYA3':
        RAVYA3(indice_ini,rval,P,normal,difnue,pmaxinue,pmaxinue,CON)
    if nombre=='GAST2A':
        GAST2A(indice_ini,rval,P,normal,difnue,pmaxinue,pmaxinue,CON)'''
    if nombre=='HYGOV':
        print('v en la llamada', v)
        HYGOV(indice_ini, difnue, v, P,  pmaxinue, CON)
    if nombre=='TGOV1':
        print('v en la llamada', v)
        TGOV1(indice_ini, v, pmaxinue, CON)
    return
'''
def BSASGO(indice_ini, potencia,normal,difnue,pmaxinue,pmaxinue2,CON):
    if difnue>0:
        ierr,rval1=psspy.dsrval('CON',(indice_ini+15))
        ierr,rval2=psspy.dsrval('CON',(indice_ini+10))
        ierr,rval3=psspy.dsrval('CON',(indice_ini+11))
        if(normal==1):
            limnue=pmaxinue2/(rval1*rval3)
        else:
            limnue=pmaxinue/(rval1*rval3)
        psspy.change_con(indice_ini+CON,limnue)
        potencia_maxima=rval1*rval2*rval3     
        reserva=potencia_maxima-potencia
    return(reserva,potencia_maxima)

def RAVYA3(indice_ini, rval,potencia,normal,difnue,pmaxinue,pmaxinue2,CON):
    if difnue>0:
        if normal==0:
        potencia_maxima=rval
        psspy.change_con(indice_ini+CON,pmaxinue)
        reserva=potencia_maxima-potencia
    return(reserva, potencia_maxima)

def GAST2A(indice_ini, rval,potencia,normal,difnue,pmaxinue,pmaxinue2,CON):
    if (difnue>0):
        ierr,rval22=psspy.dsrval('CON',(indice_ini+14))
        ierr,rval20=psspy.dsrval('CON',(indice_ini+16))
        ierr,rval18=psspy.dsrval('CON',(indice_ini+6))   
        ierr,rval12=psspy.dsrval('CON',(indice_ini+25))         
        ierr,rval13=psspy.dsrval('CON',(indice_ini+12))   
        ierr,rval14=psspy.dsrval('CON',(indice_ini+26))
        ierr,rval5=psspy.dsrval('CON',(indice_ini+29)) 
        ierr,rval6=psspy.dsrval('CON',(indice_ini+8))           
        ierr,rval17=psspy.dsrval('CON',(indice_ini+11))

        c=rval22
        kf=rval20
        trate=rval8
        af2=rval2
        a=rval3
        bf2=rval4
        k6=rval5
        max=rval6
        k3=rval7
                
        if(normal==1):
            limnue=(((pmaxinue2/trate)-af2)/(bf2*(a/(c+a*kf)))-k6)/k3
        else:
            limnue=(((pmaxinue/trate)-af2)/(bf2*(a/(c+a*kf)))-k6)/k3
        
        psspy.change_con(indice_ini+CON,limnue)
        potencia_maxima=trate*(af2+bf2*(a/(c+a*kf))*(max*k3+k6))
        
        reserva=potencia_maxima-potencia
    
    return(reserva,potencia_maxima)

def GAST(indice_ini, rval, v, P,normal,difnue, pmaxinue, pmaxinue2,CON):
    if(difnue>0):
        if(normal==1):
            limnue=pmaxinue2/v
        else: 
            limnue=pmaxinue/v

        psspy.change_con(indice_ini+CON,limnue)

    potencia_maxima = v*rval
    reserva=potencia_maxima-P
    return (reserva,potencia_maxima)

def GASTWD(indice_ini, rval,potencia,normal,difnue,pmaxinue,pmaxinue2,CON):
    if (difnue>0):
        ierr,rval22=psspy.dsrval('CON',(indice_ini+14))
        ierr,rval20=psspy.dsrval('CON',(indice_ini+16))
        ierr,rval18=psspy.dsrval('CON',(indice_ini+6)) 
        ierr,rval2=psspy.dsrval('CON',(indice_ini+25)) 
        ierr,rval3=psspy.dsrval('CON',(indice_ini+12))
        ierr,rval4=psspy.dsrval('CON',(indice_ini+26))
        ierr,rval5=psspy.dsrval('CON',(indice_ini+29)) 
        ierr,rval6=psspy.dsrval('CON',(indice_ini+8))
        ierr,rval7=psspy.dsrval('CON',(indice_ini+11))
                 
        if normal==1):
            limnue=(((pmaxinue2/trate)-af2)/(bf2*(a/(c+a*kf)))-k6)/k3
        else:
            limnue=(((pmaxinue/trate)-af2)/(bf2*(a/(c+a*kf)))-k6)/k3
        psspy.change_con(indice_ini+CON,limnue)

        potencia_maxima=trate*(af2+bf2*(a/(c+a*kf))*(max*k3+k6))
        reserva=potencia_maxima-potencia
    return (reserva,potencia_maxima)


'''
def HYGOV(indice_ini, v, P,difnue, pmaxinue, CON):
    if difnue>0:
        ierr,rval20=psspy.dsrval('CON',(indice_ini+11))
        ierr,rval22=psspy.dsrval('CON',(indice_ini+9))
        limnue=(pmaxinue/(v*rval22))+rval20
        psspy.change_con(indice_ini+CON,limnue)
        
    return 

'''
def HYGV5P(indice_ini, rval,potencia,normal,difnue,pmaxinue,pmaxinue2,CON):
    if (difnue>0):
        ierr,rval1=psspy.dsrval('CON',(indice_ini+22))
        if(NORMAL==1):
            limnue=pmaxinue2/rval1
        else
            limnue=pmaxinue/rval1

        psspy.change_con(indice_ini+CON,limnue)
        potencia_maxima=rval1*rval
        reserva=potencia_maxima-potencia
    
    return (reserva,potencia_maxima)


def HYGV7P (indice_ini, rval,potencia,normal,difnue,pmaxinue,pmaxinue2,CON):
    if (difnue>0):
        ierr,rval1=psspy.dsrval('CON',(indice_ini+18))
        if(normal==1):
            limnue=pmaxinue2/rval1
        else:
            limnue=pmaxinue/rval1
        psspy.change_con(indice_ini+CON,limnue)
        potencia_maxima=rval1*rval
        reserva=potencia_maxima-potencia
    return (reserva,potencia_maxima)

def IEEEG1(indice_ini, rval,potencia,normal,difnue,pmaxinue,pmaxinue2,CON):
    if (difnue>0):
        if(normal==1):
            limnue=pmaxinue2/(v)
        else:
            limnue=pmaxinue/(v)
        psspy.change_con(indice_ini+CON,limnue)
        potencia_maxima=v*limnue
        reserva=potencia_maxima-potencia

    return (reserva,potencia_maxima)

def IEEEG3 (indice_ini, rval,potencia,normal,difnue,pmaxinue,pmaxinue2,CON):
    if (difnue>0.0)then
        if(normal==1):
            limnue=pmaxinue2/(v)
        else:
            limnue=pmaxinue/(v)
        psspy.change_con(indice_ini+CON,limnue)
        potencia_maxima=v*limnue
        reserva=potencia_maxima-potencia
    return (reserva,potencia_maxima)
        

def IEEEG2(indice_ini, rval,potencia,normal,difnue,pmaxinue,pmaxinue2,CON):
    if (difnue>0.0):
        IF(NORMAL==1):
            limnue=pmaxinue2/(v)
        else:
            limnue=pmaxinue/(v)
        psspy.change_con(indice_ini+CON,limnue)
        potencia_maxima=v*limnue
        reserva=potencia_maxima-potencia
    return (reserva,potencia_maxima)


def IEESGO (indice_ini, rval,potencia,normal,difnue,pmaxinue,pmaxinue2,CON):
    if (difnue>0):
        IF(NORMAL==1)THEN
            limnue=pmaxinue2/(v)
        else:
            limnue=pmaxinue/(v)
        psspy.change_con(indice_ini+CON,limnue)
        potencia_maxima=v*limnue
        reserva=potencia_maxima-potencia
    return (reserva,potencia_maxima)
  
def STGV1P(indice_ini, rval,potencia,normal,difnue,pmaxinue,pmaxinue2,CON):
    if (difnue>0):
        ierr,rval1=psspy.dsrval('CON',(indice_ini+21))
        if(normal==1):
            limnue=pmaxinue2/(rval1)
        else:
            limnue=pmaxinue/(rval1)
        psspy.change_con(indice_ini+CON,limnue)
        potencia_maxima=rval1*limnue
        reserva=potencia_maxima-potencia
    return (reserva,potencia_maxima)   

def STGV4P(indice_ini, rval,potencia,normal,difnue,pmaxinue,pmaxinue2,CON):
    if (difnue>0.0)then
        ierr,rval1=psspy.dsrval('CON',(indice_ini+21))
        if(normal==1):
            limnue=pmaxinue2/(rval1)
        else:
            limnue=pmaxinue/(rval1)
        psspy.change_con(indice_ini+CON,limnue)
        potencia_maxima=rval1*limnue
        reserva=potencia_maxima-potencia
    return (reserva,potencia_maxima)


def STGV2P (indice_ini, rval,potencia,normal,difnue,pmaxinue,pmaxinue2,CON):
    if (difnue>0.0):
            ierr,rval1=psspy.dsrval('CON',(indice_ini+18))
            ierr,rval3=psspy.dsrval('CON',(indice_ini+14))
        if(normal==1):
            limnue=pmaxinue2/(rval1)
        else:
            limnue=pmaxinue/(rval1)
        psspy.change_con(indice_ini+CON,limnue)
        potencia_maxima=rval1*limnue
        reserva=potencia_maxima-potencia
    return (reserva,potencia_maxima)

'''
def TGOV1(indice_ini, v, pmaxinue,CON):
    v_local=v
    print('V adentro',v_local)
    limnue=pmaxinue/v_local
        
    print(pmaxinue)
    print(limnue)

    psspy.change_con(indice_ini+CON,limnue)
    #agregado

    return 

'''
def WPIDHY (indice_ini, v, potencia, normal,difnue, pmaxinue, pmaxinue2,CON):
    if (difnue>0):
        if(normal==1):
            limnue=pmaxinue2(v
        else:
            limnue=pmaxinue/v
        psspy.change_con(indice_ini+CON,limnue)
        potencia_maxima=v*limnue
        reserva=potencia_maxima-potencia
    return (reserva,potencia_maxima)

def GAST5(indice_ini, v, potencia, normal,difnue, pmaxinue, pmaxinue2,CON):
    if (difnue>0):
        ierr,rval1=psspy.dsrval('CON',(indice_ini+9))
        if(NORMAL==1):
            limnue=(pmaxinue2/v)+rval1
        else:
            limnue=(pmaxinue/v)+rval1
        psspy.change_con(indice_ini+CON,limnue)
        potencia:(limnue-rval1)*v  
        reserva=potencia_maxima-potencia
    return (reserva,potencia_maxima)


def SIE943(indice_ini, v, potencia, normal,difnue, pmaxinue, pmaxinue2,CON):
    if (difnue>0.0)then
        AF1=0
        ierr,AF1=psspy.dsrval('CON',(indice_ini+23))
        BF1=0
        ierr,BF1=psspy.dsrval('CON',(indice_ini+24))
        RMAX4=0
        ierr,RMAX4=psspy.dsrval('CON',(indice_ini+32))
        AF2=0
        ierr,AF2=psspy.dsrval('CON',(indice_ini+34))            
        BF2=0 
        ierr,BF2=psspy.dsrval('CON',(indice_ini+35))
        AF3=0
        ierr,AF3psspy.dsrval('CON',(indice_ini+37)) 
        CF3=0 
        ierr,CF3=psspy.dsrval('CON',(indice_ini+39))
        DF3=0.
        ierr,DF3=psspy.dsrval('CON',(indice_ini+40))
        TLIM=0.
        ierr,TLIM=psspy.dsrval('CON',(indice_ini+47))
        TAMB=0.
        ierr,TAMB=psspy.dsrval('CON',(indice_ini+60))
        ierr,rval1=psspy.dsrval('CON',(indice_ini+6))                     
        if(nromal==1):
            rQg=((pmaxinue2/rval1)-bf1)/af1
            limnue=-(((rQg*cf3+df3-tlim+af3*tamb)/bf3)+bf2)/af2
        else:
            rQg=((pmaxinue/rval1)-bf1)/af1
            limnue=-(((rQg*cf3+df3-tlim+af3*tamb)/bf3)+bf2)/af2
        psspy.change_con(indice_ini+CON,limnue)
        rQg=(tlim-af3*tamb-bf3*((af2*rmax4+bf2)*1.0)-df3)/cf3
        #revisar esto
        potencia_maxima=rval1*rQg
        reserva=potencia_maxima-potencia
    return (reserva,potencia_maxima)

def TUCUGO(indice_ini, v, potencia, normal,difnue, pmaxinue, pmaxinue2,CON):
    if (difnue>0.0):
        ierr,rval1=psspy.dsrval('CON',(indice_ini+15))
        ierr,rval3=psspy.dsrval('CON',(indice_ini+11))
        ierr,rval4=psspy.dsrval('CON',(indice_ini+14))      
        if(normal==1):
            limnue=((pmaxinue2/rval1)+rval4)/rval3
        else:
            limnue=((pmaxinue/rval1)+rval4)/rval3
            psspy.change_con(indice_ini+CON,limnue)
        potencia_maxima=((lim*rval3)-rval4)*rval1 
        reserva=potencia_maxima-potencia
    return (reserva,potencia_maxima)

def GASV94 (indice_ini, v, potencia, normal,difnue, pmaxinue, pmaxinue2,CON):
    if (difnue>0.0)then 
        AF6=0.
        TAMB=0.0
        BF6=0.0
        AF4=0.0
        BF4=0.0
        DF6=0.0
        CF6=0.0
        AF5=0.0
        BF5=0.0
        
        ierr,rval1=psspy.dsrval('CON',(indice_ini+50))
        ierr,AF6=psspy.dsrval('CON',(indice_ini+61))   
        ierr,TAMB=psspy.dsrval('CON',(indice_ini+53))
        ierr,BF6=psspy.dsrval('CON',(indice_ini+62))
        ierr,AF4=psspy.dsrval('CON',(indice_ini+57))
        ierr,BF4=psspy.dsrval('CON',(indice_ini+58))
        ierr,DF6=psspy.dsrval('CON',(indice_ini+64))
        ierr,CF6=psspy.dsrval('CON',(indice_ini+63))
        ierr,AF5=psspy.dsrval('CON',(indice_ini+59))
        ierr,BF5=psspy.dsrval('CON',(indice_ini+60))

        if(NORMAL==1):
            RQg=((pmaxinue2/rval1)-bf5)/Bf5
            limnue=(RQg*CF6)+DF6+BF6*(AF4+BF4)+AF6*TAMB
        else:
            RQg=((pmaxinue/rval1)-bf5)/Bf5
            limnue=(RQg*CF6)+DF6+BF6*(AF4+BF4)+AF6*TAMB
        psspy.change_con(indice_ini+CON,limnue)
        potencia_maxima=buscar solucion
        reserva=potencia_maxima-potencia
    return (reserva,potencia_maxima)

'''