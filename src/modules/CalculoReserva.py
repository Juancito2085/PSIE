
import os
import sys

sys_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSPY34'
sys.path.append(sys_path_PSSE)
sys_path_PSSE=r'E:\PSS\PSSPY34'


os_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSBIN'
os.environ['PATH'] += ';' + os_path_PSSE
os.environ['PATH'] += ';' + sys_path_PSSE

import psspy

def calculo(nombre,indice_ini,rval,v,potencia):
    if nombre=="BSASGO":
        reserva_maquina,potencia_maxima=BSASGO(indice_ini,potencia)
    elif nombre=="RAVYA3":
        reserva_maquina,potencia_maxima=RAVYA3(rval,potencia)
    elif nombre=="GAST2A":
        reserva_maquina,potencia_maxima=GAST2A(indice_ini,potencia)
    elif nombre=="GAST":
        reserva_maquina,potencia_maxima=GAST(v,rval,potencia)
    elif nombre=="GASTWD":
        reserva_maquina,potencia_maxima=GASTWD(indice_ini,potencia)
    elif nombre=="HYGOV":
        reserva_maquina,potencia_maxima=HYGOV(indice_ini,rval,v,potencia)
    elif nombre=="HYGV5P":
        reserva_maquina,potencia_maxima=HYGV5P(indice_ini,rval,potencia)
    elif nombre=="HYGV7P":
        reserva_maquina,potencia_maxima=HYGV7P(indice_ini,rval,potencia)
    elif nombre=="IEEEG1":
        reserva_maquina,potencia_maxima=IEEEG1(rval,v,potencia)
    elif nombre=="IEEEG3":
        reserva_maquina,potencia_maxima=IEEEG3(rval,v,potencia)
    elif nombre=="IEEEG2":
        reserva_maquina,potencia_maxima=IEEEG2(rval,v,potencia)
    elif nombre=="IEESGO":
        reserva_maquina,potencia_maxima=IEESGO(rval,v,potencia)
    elif nombre=="STGV1P":
        reserva_maquina,potencia_maxima=STGV1P(indice_ini,rval,potencia)
    elif nombre=="STGV4P":
        reserva_maquina,potencia_maxima=STGV4P(indice_ini,potencia)
    elif nombre=="STGV2P":
        reserva_maquina,potencia_maxima=STGV2P(indice_ini,potencia)
    elif nombre=="TGOV1":
        reserva_maquina,potencia_maxima=TGOV1(rval,v,potencia)
    elif nombre=="WPIDHY":
        reserva_maquina,potencia_maxima=WPIDHY(rval,v,potencia)
    elif nombre=="GAST5":
        reserva_maquina,potencia_maxima=GAST5(indice_ini,rval,v,potencia)
    elif nombre=="SIE943":
        reserva_maquina,potencia_maxima=SIE943(indice_ini,potencia)
    elif nombre=="TUCUGO":
        reserva_maquina,potencia_maxima=TUCUGO(indice_ini,potencia)
    return reserva_maquina,potencia_maxima


def BSASGO(indice_ini, potencia):
    ierr,rval1=psspy.dsrval('CON',(indice_ini+15))
    ierr,rval2=psspy.dsrval('CON',(indice_ini+10))
    ierr,rval3=psspy.dsrval('CON',(indice_ini+11))
    if (potencia>0):
        potencia_maxima=rval1*rval2*rval3     
    if potencia_maxima>=potencia:
        reserva_maquina=potencia_maxima-potencia
    return(reserva_maquina,potencia_maxima)

def RAVYA3(rval,potencia):
    if (potencia>0):        
        potencia_maxima=rval
    if (potencia_maxima>=potencia):
        reserva_maquina=potencia_maxima-potencia
    return(reserva_maquina, potencia_maxima)

def GAST2A(indice_ini,potencia):
    c=0.0
    kf=0.0
    trate=0.0
    af2=0.0
    a=0.0
    bf2=0.0
    k6=0.0
    max=0.0
    k3=0.0

    ierr,rval22=psspy.dsrval('CON',(indice_ini+14))
    ierr,rval20=psspy.dsrval('CON',(indice_ini+16))
    ierr,rval18=psspy.dsrval('CON',(indice_ini+6))   
    ierr,rval12=psspy.dsrval('CON',(indice_ini+25))         
    ierr,rval13=psspy.dsrval('CON',(indice_ini+12))   
    ierr,rval14=psspy.dsrval('CON',(indice_ini+26))
    ierr,rval5=psspy.dsrval('CON',(indice_ini+29)) 
    ierr,rval6=psspy.dsrval('CON',(indice_ini+8))           
    ierr,rval17=psspy.dsrval('CON',(indice_ini+11))

    if (potencia>0):
        c=rval22
        kf=rval20
        trate=rval8
        af2=rval2
        a=rval3
        bf2=rval4
        k6=rval5
        max=rval6
        k3=rval7
             
        potencia_maxima=trate*(af2+bf2*(a/(c+a*kf))*(max*k3+k6))
        if (potencia_maxima>=potencia):
            reserva_maquina=potencia_maxima-potencia
    return(reserva_maquina,potencia_maxima)

def GAST(v,rval,potencia):
    if (potencia>0):
        potencia_maxima=v*rval
        if (potencia_maxima>=potencia):
            reserva_maquina=potencia_maxima-potencia
    return(reserva_maquina,potencia_maxima)

def GASTWD(indice_ini,potencia):
    c=0.0
    kf=0.0
    trate=0.0
    af2=0.0
    a=0.0
    bf2=0.0
    k6=0.0
    max=0.0
    k3=0.0

    ierr,rval22=psspy.dsrval('CON',(indice_ini+14))
    ierr,rval20=psspy.dsrval('CON',(indice_ini+16))
    ierr,rval18=psspy.dsrval('CON',(indice_ini+6)) 
    ierr,rval2=psspy.dsrval('CON',(indice_ini+25)) 
    ierr,rval3=psspy.dsrval('CON',(indice_ini+12))
    ierr,rval4=psspy.dsrval('CON',(indice_ini+26))
    ierr,rval5=psspy.dsrval('CON',(indice_ini+29)) 
    ierr,rval6=psspy.dsrval('CON',(indice_ini+8))
    ierr,rval7=psspy.dsrval('CON',(indice_ini+11))

    if (potencia>0):
        c=rval22
        kf=rval20
        trate=rval8
        af2=rval2
        a=rval3
        bf2=rval4
        k6=rval5
        max=rval6
        k3=rval7            
        potencia_maxima=trate*(af2+bf2*(a/(c+a*kf))*(max*k3+k6))
        if (potencia_maxima>=potencia):
            reserva_maquina=potencia_maxima-potencia
    
    return(reserva_maquina,potencia_maxima)

def HYGOV(indice_ini,rval,V,potencia):
    if (potencia>0):
        ierr,rval20=psspy.dsrval('CON',(indice_ini+11))
        ierr,rval22=psspy.dsrval('CON',(indice_ini+9))
        potencia_maxima=((rval-rval20)*rval22)*V
        if (potencia_maxima>=potencia):
            reserva_maquina=potencia_maxima-potencia
    return(reserva_maquina,potencia_maxima)

def HYGV5P(indice_ini,rval,potencia):
    if (potencia>0):
        ierr,rval1=psspy.dsrval('CON',(indice_ini+22))
        potencia_maxima=rval*rval1
        if (potencia_maxima>=potencia):
            reserva_maquina=potencia_maxima-potencia
    return(reserva_maquina,potencia_maxima)

def HYGV7P(indice_ini,rval,potencia):
    if (potencia>0):
        ierr,rval1=psspy.dsrval('CON',(indice_ini+18))
        potencia_maxima=rval*rval1
        if (potencia_maxima>=potencia):
            reserva_maquina=potencia_maxima-potencia
    return(reserva_maquina,potencia_maxima)

def IEEEG1(rval,v,potencia):
    if (potencia>0):
        potencia_maxima=v*rval
        if (potencia_maxima>=potencia):
            reserva_maquina=potencia_maxima-potencia
    return(reserva_maquina,potencia_maxima)

def IEEEG3(rval,v,potencia):
    if (potencia>0):
        potencia_maxima=v*rval
        if (potencia_maxima>=potencia):
            reserva_maquina=potencia_maxima-potencia
    return(reserva_maquina,potencia_maxima)

def IEEEG2(rval,v,potencia):
    if (potencia>0):
        potencia_maxima=v*rval
        if (potencia_maxima>=potencia):
            reserva_maquina=potencia_maxima-potencia
    return(reserva_maquina,potencia_maxima)

def IEESGO(rval,v,potencia):
    if (potencia>0):
        potencia_maxima=v*rval
        if (potencia_maxima>=potencia):
          reserva_maquina=potencia_maxima-potencia
    return(reserva_maquina,potencia_maxima)

def STGV1P(indice_ini,rval,potencia):
    if (potencia>0):
        ierr,rval1=psspy.dsrval('CON',(indice_ini+21))
        potencia_maxima=rval*rval1
        if (potencia_maxima>=potencia):
            reserva_maquina=potencia_maxima-potencia
    return(reserva_maquina,potencia_maxima)

def STGV4P(indice_ini,potencia):
    if (potencia>0.0):
        ierr,rval1=psspy.dsrval('CON',(indice_ini+21))
        potencia_maxima=rval*rval1
        if (potencia_maxima>=potencia):
            reserva_maquina=potencia_maxima-potencia
    return(reserva_maquina,potencia_maxima)

def STGV2P(indice_ini,potencia):
    if (potencia>0):
        ierr,rval1=psspy.dsrval('CON',(indice_ini+18))
        ierr,rval3=psspy.dsrval('CON',(indice_ini+14))
        potencia_maxima=rval3*rval1
        if (potencia_maxima>=potencia):
          reserva_maquina=potencia_maxima-potencia
    return(reserva_maquina,potencia_maxima)

def TGOV1(rval,v,potencia):
    if (potencia>0):
        potencia_maxima=v*rval
        if (potencia_maxima>=potencia):
            reserva_maquina=potencia_maxima-potencia
    return(reserva_maquina,potencia_maxima)

def WPIDHY(rval,v,potencia):
    if (potencia>0):
        potenica_maxima=v*rval
        if (potenica_maxima>=potencia):
            reserva_maquina=potenica_maxima-potencia
    return(reserva_maquina,potencia_maxima)

def GAST5(indice_ini,rval,v,potencia):
    ierr,rval1=psspy.dsrval('CON',(indice_ini+9))
    if (potencia>0.0):
        potencia_maxima=(rval-rval1)*v     
        if (potencia_maxima>=potencia):
          reserva_maquina=potencia_maxima-potencia
    return(reserva_maquina,potencia_maxima)

def SIE943(indice_ini,potencia):
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
    if (potencia>0):
        rQg=(tlim-af3*tamb-bf3*((af2*rmax4+bf2)*1.0)-df3)/cf3
        ### rse toma como potencia maxima el menor de 2 calculos
        potencia_maxima1=rval1
        potencia_maxima2=rval1(ngen)*(af1*rQg+bf1)
        if potencia_maxima1>potencia_maxima2:
           potencia_maxima=potencia_maxima2
        else:
           potencia_maxima=potencia_maxima1
        if (potencia_maxima>=potencia):
           reserva_maquina=potencia_maxima-potencia
    return(reserva_maquina,potencia_maxima)

def TUCUGO(indice_ini,potencia):
    ierr,rval1=psspy.dsrval('CON',(indice_ini+15))
    ierr,rval3=psspy.dsrval('CON',(indice_ini+11))
    ierr,rval4=psspy.dsrval('CON',(indice_ini+14))
    if (potencia>0):
        potencia_maxima=((rval*rval3)-rval4)*rval1 
    if (potencia_maxima>=potencia):
        reserva_maquina=potencia_maxima-potencia
    return(reserva_maquina,potencia_maxima)

def GASV94(indice_ini,rval,potencia):
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
    
    if (potencia>0):
        RQG=(rval-AF6*TAMB-BF6*(AF4+BF4)-DF6)/CF6
        potencia_maxima1=rval1*(AF5+BF5)
        potencia_maxima2=rval1*(AF5*RQG+BF5)
        if potencia_maxima1>potencia_maxima2:
            potencia_maxima=potencia_maxima2
        else:
            potencia_maxima=potencia_maxima1
        if (potencia_maxima>=potencia):
            reserva_maquina=potencia_maxima-potencia
    return(reserva_maquina,potencia_maxima)
    