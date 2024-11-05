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

def cambiar_limites(nombre,indice_ini,rval, v, P, normal,difnue, pmaxinue, pmaxinue2,CON):
    if nombre=='BSASGO':
        BSASGO(indice_ini, P,normal,difnue,pmaxinue,pmaxinue2,CON)
    if nombre=='RAVYA3':
        RAVYA3(indice_inirval,P,normal,difnue,pmaxinue,pmaxinue2,CON)
    if nombre=='HYGOV':
        HYGOV(indice_ini,normal, difnue, v, P,  pmaxinue, pmaxinue2, CON)
    if nombre=='TGOV1':
        TGOV1(normal,difnue, v, P, pmaxinue, pmaxinue2, indice_ini,CON)
    return

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
'''
def RAVYA3(indice_ini, rval,potencia,normal,difnue,pmaxinue,pmaxinue2,CON):
    if difnue>0:
        if normal==0:
        potencia_maxima=rval
        psspy.change_con(indice_ini+CON,pmaxinue)
        reserva=potencia_maxima-potencia
    return(reserva, potencia_maxima)
'''

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
'''
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
def HYGOV(indice_ini, v, P, normal,difnue, pmaxinue, pmaxinue2,CON):
    if difnue>0:
        ierr,rval20=psspy.dsrval('CON',(indice_ini+11))
        ierr,rval22=psspy.dsrval('CON',(indice_ini+9))
        if(normal==1):
            limnue=(pmaxinue2/(v*rval22))+rval20
        else:
            limnue=(pmaxinue/(v*rval22))+rval20
        psspy.change_con(indice_ini+CON,limnue)
        #agregado
        potencia_maxima=((limnue-rval20)*rval22)*v
        reserva=potencia_maxima-P
        print(reserva)
        print(potencia_maxima)
        print(P)
    return (reserva,potencia_maxima)

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
        

/*
----- IEEEG2 --------------------------------------------
*/

if (nombre1(NGEN)=='IEEEG2')then
 if (difnue>0.0)then
  write 2; 'REGULADOR=IEEEG2'
  IF(NORMAL==1)THEN
  limnue=pmaxinue2/(v)
  ELSE
  limnue=pmaxinue/(v)
  ENDIF
  write 2;ibus,' ',nombre,' limite nuevo= ',limnue
  push 'ALTR'
  push '2'
  push is+i5
  push 'Y'
  push limnue
  push '0'
  push '0'
  push '0'
 endif
endif

/*
----- IEESGO --------------------------------------------
*/

if (nombre1(NGEN)=='IEESGO')then
 if (difnue>0.0)then
  write 2; 'REGULADOR=IEESGO'
  IF(NORMAL==1)THEN
  limnue=pmaxinue2/(v)
  ELSE
  limnue=pmaxinue/(v)
  ENDIF
  write 2;ibus,' ',nombre,' limite nuevo= ',limnue
  push 'ALTR'
  push '2'
  push is+i5
  push 'Y'
  push limnue
  push '0'
  push '0'
  push '0'
 endif
endif

/*
----- STGV1P --------------------------------------------
*/


if (nombre1(NGEN)=='STGV1P')then
 if (difnue>0.0)then
  write 2; 'REGULADOR=STGV1P'
  IF(NORMAL==1)THEN
  limnue=pmaxinue2/(rval1)
  ELSE
  limnue=pmaxinue/(rval1)
  ENDIF
  write 2;ibus,' ',nombre,' limite nuevo= ',limnue
  push 'ALTR'
  push '2'
  push is+i5
  push 'Y'
  push limnue
  push '0'
  push '0'
  push '0'
 endif
endif

/*
----- STGV4P --------------------------------------------
*/

if (nombre1(NGEN)=='STGV4P')then
 if (difnue>0.0)then
  write 2; 'REGULADOR=STGV4P'
  IF(NORMAL==1)THEN
  limnue=pmaxinue2/(rval1)
  ELSE
  limnue=pmaxinue/(rval1)
  ENDIF
  write 2;ibus,' ',nombre,' limite nuevo= ',limnue
  push 'ALTR'
  push '2'
  push is+i5
  push 'Y'
  push limnue
  push '0'
  push '0'
  push '0'
 endif
endif


/*
----- STGV2P --------------------------------------------
*/

if (nombre1(NGEN)=='STGV2P')then
 if (difnue>0.0)then
  write 2; 'REGULADOR=STGV2P'
  IF(NORMAL==1)THEN
  limnue=pmaxinue2/(rval1)
  ELSE
  limnue=pmaxinue/(rval1)
  ENDIF
  write 2;ibus,' ',nombre,' limite nuevo= ',limnue
  push 'ALTR'
  push '2'
  push is+i5
  push 'Y'
  push limnue
  push '0'
  push '0'
  push '0'
 endif
endif

'''
def TGOV1(indice_ini, v, P,normal,difnue, pmaxinue, pmaxinue2,CON):
    if difnue>0:
        if(normal==1):
            limnue=pmaxinue2/v
        else:
            limnue=pmaxinue/v
        psspy.change_con(indice_ini+CON,limnue)
        #agregado
        potencia_maxima=v*limnue
        reserva=potencia_maxima-P
        print(reserva)
        print(potencia_maxima)
        print(P)
    return (reserva,potencia_maxima)

'''
if (nombre1(NGEN)=='WPIDHY')then
 if (difnue>0.0)then
  write 2; 'REGULADOR=WPIDHY'
  IF(NORMAL==1)THEN
  limnue=pmaxinue2/(v)
  ELSE
  limnue=pmaxinue/(v)
  ENDIF
  write 2;ibus,' ',nombre,' limite nuevo= ',limnue
  push 'ALTR'
  push '2'
  push is+i5
  push 'Y'
  push limnue
  push '0'
  push '0'
  push '0'
 endif
endif

/*
----- GAST5 --------------------------------------------
*/

if (nombre1(NGEN)=='GAST5')then
 if (difnue>0.0)then
  write 2; 'REGULADOR=GAST5'
  IF(NORMAL==1)THEN
  limnue=(pmaxinue2/v)+rval1
  ELSE
  limnue=(pmaxinue/v)+rval1
  ENDIF
  write 2;ibus,' ',nombre,' limite nuevo= ',limnue
  push 'ALTR'
  push '2'
  push is+i5
  push 'Y'
  push limnue
  push '0'
  push '0'
  push '0'
 endif
endif

/*
----- SIE943 --------------------------------------------
*/

if (nombre1(NGEN)=='SIE943')then
 AF1=0.
 CALL DSRVAL('CON',(is+23),af1,ierr)
 BF1=0.
 CALL DSRVAL('CON',(is+24),bf1,ierr)
 RMAX4=0.
 CALL DSRVAL('CON',(is+32),rmax4,ierr)
 AF2=0.
 CALL DSRVAL('CON',(is+34),af2,ierr) 
 BF2=0. 
 CALL DSRVAL('CON',(is+35),bf2,ierr)
 AF3=0.
 CALL DSRVAL('CON',(is+37),af3,ierr)
 BF3=0.
 CALL DSRVAL('CON',(is+38),bf3,ierr) 
 CF3=0. 
 CALL DSRVAL('CON',(is+39),cf3,ierr)
 DF3=0.
 CALL DSRVAL('CON',(is+40),df3,ierr)
 TLIM=0.
 CALL DSRVAL('CON',(is+47),tlim,ierr)
 TAMB=0.
 CALL DSRVAL('CON',(is+60),tamb,ierr)
 CALL DSRVAL('CON',(is+6),rval1,ierr)
 write 2; 'Valor de TRATE= ',rval1             
 if (difnue>0.0)then
  write 2; 'REGULADOR=SIE943'             
  IF(NORMAL==1)THEN
   rQg=((pmaxinue2/rval1)-bf1)/af1
   limnue=-(((rQg*cf3+df3-tlim+af3*tamb)/bf3)+bf2)/af2
  ELSE
   rQg=((pmaxinue/rval1)-bf1)/af1
   limnue=-(((rQg*cf3+df3-tlim+af3*tamb)/bf3)+bf2)/af2
  ENDIF
  write 2;ibus,' ',nombre,' limite nuevo= ',limnue
  push 'ALTR'
  push '2'
  push is+i5
  push 'Y'
  push limnue
  push '0'
  push '0'
  push '0'
 endif
endif

/*
----- TUCUGO --------------------------------------------
*/

if (nombre1(NGEN)=='TUCUGO')then
 if (difnue>0.0)then
  write 2; 'REGULADOR=TUCUGO'             
  IF(NORMAL==1)THEN
  limnue=((pmaxinue2/rval1)+rval4)/rval3
  ELSE
  limnue=((pmaxinue/rval1)+rval4)/rval3
  ENDIF
  write 2;ibus,' ',nombre,' limite nuevo= ',limnue
  push 'ALTR'
  push '2'
  push is+i5
  push 'Y'
  push limnue
  push '0'
  push '0'
  push '0'
 endif 
endif 

/*
----- GASV94 --------------------------------------------
*/

if (nombre1(NGEN)=='GASV94')then
 AF6=0.
 TAMB=0.0
 BF6=0.0
 AF4=0.0
 BF4=0.0
 DF6=0.0
 CF6=0.0
 AF5=0.0
 BF5=0.0
 write 2; 'REGULADOR=GASV94'             
 CALL DSRVAL('CON',(is+50),rval1,ierr)
 CALL DSRVAL('CON',(is+61),AF6,ierr)
 CALL DSRVAL('CON',(is+53),TAMB,ierr)
 CALL DSRVAL('CON',(is+62),BF6,ierr)
 CALL DSRVAL('CON',(is+57),AF4,ierr)
 CALL DSRVAL('CON',(is+58),BF4,ierr)
 CALL DSRVAL('CON',(is+64),DF6,ierr)
 CALL DSRVAL('CON',(is+63),CF6,ierr)
 CALL DSRVAL('CON',(is+59),AF5,ierr)
 CALL DSRVAL('CON',(is+60),BF5,ierr)

 if (difnue>0.0)then
  write 2; 'REGULADOR=GASV94'             
  RQG=0.
  IF(NORMAL==1)THEN
   RQg=((pmaxinue2/rval1)-bf5)/Bf5
   limnue=(RQg*CF6)+DF6+BF6*(AF4+BF4)+AF6*TAMB
  ELSE
   RQg=((pmaxinue/rval1)-bf5)/Bf5
   limnue=(RQg*CF6)+DF6+BF6*(AF4+BF4)+AF6*TAMB
  ENDIF
  write 2;ibus,' ',nombre,' limite nuevo= ',limnue
  push 'ALTR'
  push '2'
  push is+i5
  push 'Y'
  push limnue
  push '0'
  push '0'
  push '0'

'''