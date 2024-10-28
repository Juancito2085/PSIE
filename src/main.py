import os
import sys
 
sys_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSPY34'
sys.path.append(sys_path_PSSE)

 
os_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSBIN'
os.environ['PATH'] += ';' + os_path_PSSE
os.environ['PATH'] += ';' + sys_path_PSSE
 
# Importación de librerias necesarias
import redirect
import datetime
import re
import tkinter
import pssexplore34
import psspy

#importacion de librerias propias
import modules.lectura as lectura 
import modules.informe as informe
import modules.VerificacionDatos as verificaciondatos
import modules.CalculoReserva as CR
import modules.generacion as generacion

_i = psspy.getdefaultint()
_f = psspy.getdefaultreal()
_s = psspy.getdefaultchar()

psspy.psseinit(1000)

CASE='savnw.sav'

psspy.case(CASE)

psspy.cong(0)
psspy.conl(0,1,1,[0,0],[ 100.0,0.0,0.0, 100.0])
psspy.conl(0,1,2,[0,0],[ 100.0,0.0,0.0, 100.0])
psspy.conl(0,1,3,[0,0],[ 100.0,0.0,0.0, 100.0])
psspy.fact()
psspy.tysl(0)

# Open snap.
psspy.rstr(r"""savnw""")
psspy.dynamicsmode(0)

# 1 - Crear el archivo de salida
ruta='C:/Users/jcbru/Desktop/psie'
informe.crear(ruta)

# 2 - Lectura de los parametros
parametros=lectura.parametros()

# 3 - Lectura de datos del archivo "reserva.dat"
bus,governor,CON,porcentaje,idg,comentario,tipo=lectura.generadores()

# 4 - Verificacion de los datos
nombre=list()
cmpval=list()
v=list()
v1=list()
indice_ini=list()
rval=list()
for i in range(0,len(bus)):
   nombre_temp, cmpval_temp,v_temp,v1_temp, indice_ini_temp,rval_temp=verificaciondatos.generadores(bus[i],idg[i],CON[i])
   nombre.append(nombre_temp)
   cmpval.append(cmpval_temp)
   v.append(v_temp)
   v1.append(v1_temp)
   indice_ini.append(indice_ini_temp)
   rval.append(rval_temp)

# 5 - Determinación de los margenes de reserva
P=list()
Q=list()
for pq in cmpval:
   P.append(pq.real)
   Q.append(pq.imag)

reserva=list()
potencia_maxima=list()
for i,gov in enumerate(governor):
   res,pmax=CR.calculo(gov,indice_ini[i],rval[i],v[i],P[i])
   reserva.append(res)
   potencia_maxima.append(pmax)

# 6 - Registro de la reserva de todos los generadores en la hoja "Pmax_Pgen.prn"
reserva_por=list()
for i in range(0,len(bus)):
   reserva_por.append((reserva[i]/P[i])*100)

informe.Pmax_Pgen(ruta,bus,nombre,idg,potencia_maxima,P,reserva,reserva_por,porcentaje,parametros[0])

# 7 - Registro de los generadores con reserva por debajo de la optima
informe.Menor_optima(ruta,bus,nombre,idg,potencia_maxima,P,reserva,reserva_por,porcentaje,parametros[0])

# 8 - Registro de los generadores con reserva mayor a la maxima
informe.Mayor_maxima(ruta,bus,nombre,idg,potencia_maxima,P,reserva,reserva_por,porcentaje,parametros[0])

# 9 - Extracción de la generación del sistema
ibus_sale,nombre_sale,id_sale=lectura.generadores_no_suman()

cmpval_sale=list()
for i in range(0,len(ibus_sale)):
   cmpval_sale.append(verificaciondatos.gensale(ibus_sale[i],nombre_sale[i],id_sale[i]))
pge=0
for pq in cmpval_sale:
   if pq is not None:
      pge+=pq.real()

# 10 - Areas a restar
iarea,nombre_area=lectura.regiones_paises_limitrofes()

for i in range(0,len(iarea)):
   cmpval_area=verificaciondatos.area(iarea[i],nombre_area[i])
pga=0
for pq in cmpval_sale:
   if pq is not None:
      pga+=pq.real()

# 11 - Generación total a restar
total_A, total_R=generacion.total()
generacion_total=total_A

# 12 - informes de todo esto
gensadi=generacion_total-pge-pga
print(gensadi)

# 13 - Sección donde recorta si el parametro[1]==1
print(parametros)
if parametros[1]==1:
   print('recorta')
   if parametros[2]==0:
      print('optima')
   else:
      print('dato')
   # 14 - Anñalisis de cada governor para cambiar los limites (2204)

   # 15 Análisis de cada governor para determinar los margenes de reserva con los limites corregidos (3329)





"""
Revisar esto porque no puede ser la potencia generada mayor que la maxima y debe estar considerado en los errores->
RESERVATOTAL=RESERVATOTAL+((pmaxi(ngen)-P(ngen))*Aux01)


RESERVATOTAL2=RESERVATOTAL2+(pmaxi(Igen)-P(Igen))

Se deteermina la nueva reserva en base al dato del archivo 
reserva_nueva=reserva_optima*gen_SADI/100
(GENSADI=(PA-TOTALRESTA) en la generacion del sadi se resta los generadores que no aportan a la generacion pgeuru=pgeuru+pge y
que generacion de que regiones se restan TOTALRESTA=TOTALRESTA+PA)

RESERVANUEVA=((RESERVAOPTIMA/100.)*(GENSADI)) se calcula la nueva reserva una vez calculada la generacion del SADI 

DIFNUE(IGEN)= RESERVANUEVA*DIFEGEN(IGEN)/RESERVATOTAL2 aca se calcula la nueva reserva para el generador en cuestion 

PMAXINUE(IGEN)=P(IGEN)+DIFNUE(IGEN) se calcula nueva potencia maxima del generador para poder cambiar los limites

PMAXINUE2(IGEN)=P(IGEN)*(1.+PORCE(IGEN)/100.) se calcula la nueva potencia maxima en base al porcentaje del generador

RESERVANUEVAX=(PMAXINUE(IGEN)-P(IGEN))+RESERVANUEVAX

totadif=totadif+DIFNUE(IGEN)

totamax=totamax+pmaxiNUE(IGEN)-P(IGEN)
"""
#Se registran los generadores que tienen PMAX<PGEN (1721)
#ERRROR EN GENERADOR, ibus, id, nombre

#Se registran en pmax_pgen.prn "DETALLES DE RESERVA DE GENERADORES" (1732)
#IBUS NOMBRE ID POT_MAX POT_GEN MAX_GEN RESERVA% PORCENTAJE DATO RESOPT 

#DIFPOT=pmax-p es la reserva que queda

#Registrar generadores con reserva por debajo de la optima (1799)

#Registrar generadores con reserva mayoor a la maxima (1831)

"""Saca informe con
el titulo del escenario
reserva hidro, termica y total
revisar el tema de la reserva util
(1850)
"""

#Extrae generacion del sistema (1880)

"""Se registra los generadores que salen
gensale, ibus, nombre, PQ, id
generacion restar
"""

#Se analizan las aeras

#Se registra Genreacion Activa Reactiva (1996)
#iarea, nombrearea

#---------
#prueba para el cambio de CON
#primero miro el CON

"""for i,gov in enumerate(governor):
      if gov=='HYGOV':
         ierr,rval20=psspy.dsrval('CON',(indice_ini[i]+11))
         ierr,rval22=psspy.dsrval('CON',(indice_ini[i]+9))
         print('los valores de CON de HYGOV  son ',rval20,', ',rval22)
         psspy.change_con(indice_ini[i]+11, 0.5)
         psspy.change_con(indice_ini[i]+9,2)
         ierr,rval20=psspy.dsrval('CON',(indice_ini[i]+11))
         ierr,rval22=psspy.dsrval('CON',(indice_ini[i]+9))
         print('los nuevos valores CON de HYGOV  son ,',rval20,', ',rval22)

#verifico que me cambio los limites

total=0
for i,gov in enumerate(governor):
   print(gov,i)
   if gov=='TGOV1':
      reserva,pot=CR.TGOV1(rval[i],v[i],P[i])
      print('la reserva es ', reserva)
      
   if gov=='HYGOV':
      reserva,pot=CR.HYGOV(indice_ini[i],rval[i],v[i],P[i])
      print('el limite es ',reserva)
   total+=reserva
print('la reserva total es ',total)"""