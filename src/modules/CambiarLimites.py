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


def BSASGO(difnue,nueva_pmax,rval1,rval3):         
    '''
    
    '''
    if (difnue>0.0):
        #pmaxi=rval1*rval2*rval3     
    
        if(NORMAL==1):
            limnue=nueva_pmax/(rval1*rval3)
        else:
            limnue=nueva_pmax/(rval1*rval3)
    
    return 

def RAVYA3 (difnue):
    if (DIFNUE>0.0):
        if(NORMAL==0):
         
            'push indice_ini+i5'
           
  
    return

def GAST2A(difnue,paraetros,nueva_pmax):
    if (difnue>0.0):
        c=rval22
        kf=rval20
        trate=rval8
        af2=rval2
        a=rval3
        bf2=rval4
        k6=rval5
        max=rval6
        k3=rval7
        write 2; 'REGULADOR=GAST2A'             
        if(NORMAL==1):
            limnue=(((pmaxinue2/trate)-af2)/(bf2*(a/(c+a*kf)))-k6)/k3
        else:
            limnue=(((pmaxinue/trate)-af2)/(bf2*(a/(c+a*kf)))-k6)/k3

        write 2;ibus,' ',nombre,' limite nuevo= ',limnue
        push 'ALTR'
        push '2'
        push indice_ini+i5
        push 'Y'
        push limnue
        push '0'
        push '0'
        push '0'
        endif
        endif
    return

def GAST(difnue,nueva_pmax):
    if (difnue>0.0):
        if(NORMAL==1):
            limnue=pmaxinue2/v
        else: 
            limnue=pmaxinue/v
  
        write 2;ibus,' ',nombre,' limite nuevo= ',limnue
        push 'ALTR'
        push '2'
        push indice_ini+i5
        push 'Y'
        push limnue
        push '0'
        push '0'
        push '0'
        endif
        endif
    return

def GASTWD(difnue): 
    if (difnue>0.0):
        c=rval22
        kf=rval20
        trate=rval8
        af2=rval2
        a=rval3
        bf2=rval4
        k6=rval5
        max=rval6
        k3=rval7             
        if(NORMAL==1):
            limnue=(((pmaxinue2/trate)-af2)/(bf2*(a/(c+a*kf)))-k6)/k3
        else: 
            limnue=(((pmaxinue/trate)-af2)/(bf2*(a/(c+a*kf)))-k6)/k3
        ENDIF
        write 2;ibus,' ',nombre,' limite nuevo= ',limnue
        push 'ALTR'
        push '2'
        push indice_ini+i5
        push 'Y'
        push limnue
        push '0'
        push '0'
        push '0'
        endif
        endif
    return

def HYGOV(difnue):
    if (difnue>0):
        if(NORMAL==1):
            limnue=(pmaxinue2/(v*rval22))+rval20
        else:
            limnue=(pmaxinue/(v*rval22))+rval20
    write 2;ibus,' ',nombre,' limite nuevo= ',limnue
    write 2; 'REGULADOR=HYGOV'             
    push 'ALTR'
    push '2'
    push indice_ini+i5
    push 'Y'
    push limnue
    push '0'
    push '0'
    push '0'
    endif
    endif
    return

def HYGV5P(difnue,rval1):
    if (difnue>0.0):
        if(NORMAL==1):
            limnue=pmaxinue2/rval1
        else:
            limnue=pmaxinue/rval1
        write 2;ibus,' ',nombre,' limite nuevo= ',limnue
        push 'ALTR'
        push '2'
        push indice_ini+i5
        push 'Y'
        push limnue
        push '0'
        push '0'
        push '0'
        endif
        endif
    return

def HYGV7P(difnue,rval1):
    if (difnue>0.0):
        if(NORMAL==1):
            limnue=pmaxinue2/rval1
        else:
            limnue=pmaxinue/rval1
        write 2;ibus,' ',nombre,' limite nuevo= ',limnue
        push 'ALTR'
        push '2'
        push indice_ini+i5
        push 'Y'
        push limnue
        push '0'
        push '0'
        push '0'
        endif
        endif
    return

def IEEEG1(difnue,v):
    if (difnue>0.0):
        if(NORMAL==1):
            limnue=pmaxinue2/v
        else:
            limnue=pmaxinue/v
        write 2;ibus,' ',nombre,' limite nuevo= ',limnue
        push 'ALTR'
        push '2'
        push indice_ini+i5
        push 'Y'
        push limnue
        push '0'
        push '0'
        push '0'
        endif
        endif
    return

def IEEEG3(difnue,v):
    if (difnue>0.0):
        write 2; 'REGULADOR=IEEEG3'
        if(NORMAL==1):
            limnue=pmaxinue2/v
        else:
            limnue=pmaxinue/v
        write 2;ibus,' ',nombre,' limite nuevo= ',limnue
        push 'ALTR'
        push '2'
        push indice_ini+i5
        push 'Y'
        push limnue
        push '0'
        push '0'
        push '0'
        endif
        endif
    return

def IEEEG2(difnue,v):
    if (difnue>0.0):    
        if(NORMAL==1):
            limnue=pmaxinue2/v
        else:
            limnue=pmaxinue/v
        write 2;ibus,' ',nombre,' limite nuevo= ',limnue
        push 'ALTR'
        push '2'
        push indice_ini+i5
        push 'Y'
        push limnue
        push '0'
        push '0'
        push '0'
        endif
        endif
    return

def IEESGO(difnue,v):
    if (difnue>0.0)then
        write 2; 'REGULADOR=IEESGO'
        if(NORMAL==1):
            limnue=pmaxinue2/v
        else:
            limnue=pmaxinue/v
        ENDIF
        write 2;ibus,' ',nombre,' limite nuevo= ',limnue
        push 'ALTR'
        push '2'
        push indice_ini+i5
        push 'Y'
        push limnue
        push '0'
        push '0'
        push '0'
        endif
        endif
    return

def STGV1P(difnue,rval1):
    if (difnue>0.0):
        if(NORMAL==1):
            limnue=pmaxinue2/rval1
        else:
            limnue=pmaxinue/rval1
        write 2;ibus,' ',nombre,' limite nuevo= ',limnue
        push 'ALTR'
        push '2'
        push indice_ini+i5
        push 'Y'
        push limnue
        push '0'
        push '0'
        push '0'
        endif
        endif
    return

def STGV4P(difnue,rval1):
    if (difnue>0.0):
        if(NORMAL==1):
            limnue=pmaxinue2/rval1
        else:
            limnue=pmaxinue/rval1
    write 2;ibus,' ',nombre,' limite nuevo= ',limnue
    push 'ALTR'
    push '2'
    push indice_ini+i5
    push 'Y'
    push limnue
    push '0'
    push '0'
    push '0'
    endif
   
    return

def STGV2P(difnue,rval1):
    if (difnue>0.0):
        if(NORMAL==1):
            limnue=pmaxinue2/rval1
        else:
            limnue=pmaxinue/rval1
        write 2;ibus,' ',nombre,' limite nuevo= ',limnue
        push 'ALTR'
        push '2'
        push indice_ini+i5
        push 'Y'
        push limnue
        push '0'
        push '0'
        push '0'
    return


def TGOV1(difnue,v):
    if (difnue>0.0):
        if(NORMAL==1):
            limnue=pmaxinue2/v
        else:
            limnue=pmaxinue/v
    write 2;ibus,' ',nombre,' limite nuevo= ',limnue
    push 'ALTR'
    push '2'
    push indice_ini+i5
    push 'Y'
    push limnue
    push '0'
    push '0'
    push '0'
    endif
    endif
    return

def WPIDHY(difnue,v):
    if (difnue>0.0):
        if(NORMAL==1):
            limnue=pmaxinue2/v
        else:
            limnue=pmaxinue/v
        write 2;ibus,' ',nombre,' limite nuevo= ',limnue
        push 'ALTR'
        push '2'
        push indice_ini+i5
        push 'Y'
        push limnue
        push '0'
        push '0'
        push '0'
        endif
        endif

    return

def GAST5(difnue,v,rval1):
    if (difnue>0.0):
        if(NORMAL==1):
            limnue=(pmaxinue2/v)+rval1
        else:
            limnue=(pmaxinue/v)+rval1
    write 2;ibus,' ',nombre,' limite nuevo= ',limnue
    push 'ALTR'
    push '2'
    push indice_ini+i5
    push 'Y'
    push limnue
    push '0'
    push '0'
    push '0'
    endif
    endif
    return

def SIE943(difnue):
    af1=0.
    ierr,af1=DSRVAL('CON',(indice_ini+23))
    bf1=0.
    ierr,bf1=DSRVAL('CON',(indice_ini+24))
    ramx4=0.
    ierr,rmax4=DSRVAL('CON',(indice_ini+32))
    af2=0.
    ierr,af2=DSRVAL('CON',(indice_ini+34)) 
    bf2=0. 
    ierr,bf2=DSRVAL('CON',(indice_ini+35))
    af3=0.
    ierr,af3=DSRVAL('CON',(indice_ini+37))
    bf3=0.
    ierr,bf3=DSRVAL('CON',(indice_ini+38)) 
    cf3=0. 
    ierr,cf2=DSRVAL('CON',(indice_ini+39))
    df3=0.
    ierr,df3=DSRVAL('CON',(indice_ini+40))
    tlim=0.
    ierr,tlim=DSRVAL('CON',(indice_ini+47)r)
    tamb=0.
    ierr,tamb=DSRVAL('CON',(indice_ini+60))
    ierr,rvak1=DSRVAL('CON',(indice_ini+6))
                 
    if (difnue>0.0):            
        if(NORMAL==1):
            rQg=((pmaxinue2/rval1)-bf1)/af1
            limnue=-(((rQg*cf3+df3-tlim+af3*tamb)/bf3)+bf2)/af2
        else:
            rQg=((pmaxinue/rval1)-bf1)/af1
            limnue=-(((rQg*cf3+df3-tlim+af3*tamb)/bf3)+bf2)/af2
        write 2;ibus,' ',nombre,' limite nuevo= ',limnue
        push 'ALTR'
        push '2'
        push indice_ini+i5
        push 'Y'
        push limnue
        push '0'
        push '0'
        push '0'
        endif
        endif
    return

def TUCUGO(difnue):
    if (difnue>0.0):            
        if(NORMAL==1):
            limnue=((pmaxinue2/rval1)+rval4)/rval3
        else:
            limnue=((pmaxinue/rval1)+rval4)/rval3
    write 2;ibus,' ',nombre,' limite nuevo= ',limnue
    push 'ALTR'
    push '2'
    push indice_ini+i5
    push 'Y'
    push limnue
    push '0'
    push '0'
    push '0'
    endif 
    endif 
    return

def GASV94(difnue):
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
    ierr,rval1=DSRVAL('CON',(indice_ini+50))
    ierr,AF6=DSRVAL('CON',(indice_ini+61))
    ierr,TAMB=DSRVAL('CON',(indice_ini+53))
    ierr,BF6=DSRVAL('CON',(indice_ini+62))
    ierr,AF4=DSRVAL('CON',(indice_ini+57))
    ierr,BF4=DSRVAL('CON',(indice_ini+58))
    ierr,DF6=DSRVAL('CON',(indice_ini+64))
    ierr,CF6=DSRVAL('CON',(indice_ini+63))
    ierr,AF5=DSRVAL('CON',(indice_ini+59))
    ierr,BF5=DSRVAL('CON',(indice_ini)+60))

    if (difnue>0.0):
        write 2; 'REGULADOR=GASV94'             
        RQG=0.
        if(NORMAL==1):
            RQg=((pmaxinue2/rval1)-bf5)/Bf5
            limnue=(RQg*CF6)+DF6+BF6*(AF4+BF4)+AF6*TAMB
        else;
            RQg=((pmaxinue/rval1)-bf5)/Bf5
            limnue=(RQg*CF6)+DF6+BF6*(AF4+BF4)+AF6*TAMB
        ENDIF
        write 2;ibus,' ',nombre,' limite nuevo= ',limnue
        push 'ALTR'
        push '2'
        push indice_ini+i5
        push 'Y'
        push limnue
        push '0'
        push '0'
        push '0'
    
    return


