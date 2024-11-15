import os
import sys
#ruta para notebook
os_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSPY34'
#ruta para pc de escritorio
sys_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSPY34'
sys.path.append(sys_path_PSSE)

#ruta para notebook
os_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSBIN'
#ruta para pc de escritorio
os_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSBIN'
os.environ['PATH'] += '' + os_path_PSSE
os.environ['PATH'] += '' + sys_path_PSSE
 
# Importación de librerias necesarias
#import redirect
import datetime
import re
import tkinter as tk
from tkinter import filedialog, messagebox
import pssexplore34
import psspy

#importacion de librerias propias
import modules.lectura as lectura 
import modules.informe as informe
import modules.VerificacionDatos as verificaciondatos
import modules.CalculoReserva as CR
import modules.generacion as generacion
import modules.CambiarLimites as CL

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
print(tipo)
# 4 - Verificacion de los datos
nombre=list()
cmpval=list()
v=list()
v1=list()
indice_ini=list()
rval=list()
for i in range(0,len(bus)):
   nombre_temp, cmpval_temp,v_temp,v1_temp, indice_ini_temp,rval_temp=verificaciondatos.generadores(bus[i],idg[i],CON[i])
   nombre.append(nombre_temp.split()[0])
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
   if res==(pmax-P[i]):
      correcto='Correcto'
   else:
      correcto='Incorrecto'
   print('potencia maxima ',round(pmax,2), 'potencia operativa ',round(P[i],2), 'reserva ',round(res,2), 'resultado ',correcto)
   reserva.append(res)
   potencia_maxima.append(pmax)

# 6 - Registro de la reserva de todos los generadores en la hoja "Pmax_Pgen.prn"
reserva_por=list()
for i in range(0,len(bus)):
   reserva_por.append(round(((reserva[i]/P[i])*100),2))
   print('Porcentaje de reserva ',round(((reserva[i]/P[i])*100),2))
informe.Pmax_Pgen(ruta,bus,nombre,idg,potencia_maxima,P,reserva,reserva_por,porcentaje,parametros[0])

# 7 - Registro de los generadores con reserva por debajo de la óptima
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
print('la generacion total es ',generacion_total)
print('la generacion a restar es ',pge)
print('la generacion de las areas a restar es ',pga)

# Revisar generacion total del SADI
gensadi=generacion_total-pge-pga

# 12 - informes de todo esto
#Inicializacion de variables
reservahidro=0
reservatermica=0
reservahidro_rpf=0
reservatermica_rpf=0
pot_hidro=0
pot_TV=0
pot_CC=0
pot_TG=0
reserva_TV=0
reserva_CC=0
reserva_TG=0
reservatotal2=0

# Calculo de la reserva de los hidraulicos, termicos y ambos

for i,clase in enumerate(tipo):
   if clase=='HI':
      pot_hidro+=potencia_maxima[i]
      reservahidro+=reserva[i]
      if reserva_por[i]>=parametros[0]:
         reservatotal2+=reserva[i]
      if reserva_por[i]>porcentaje[i]:
         reservahidro_rpf+=P[i]*porcentaje[i]/100
      else:
         reservahidro_rpf+=reserva[i]
   elif clase=='TG':
      pot_TG+=potencia_maxima[i]
      reserva_TG+=reserva[i]
      reservatermica+=reserva[i]
      if reserva_por[i]>=parametros[0]:
         reservatotal2+=reserva[i]
      if reserva_por[i]>porcentaje[i]:
         reservatermica_rpf+=P[i]*porcentaje[i]/100
      else:
         reservatermica_rpf+=reserva[i]
   elif clase=='TV':
      pot_TV+=potencia_maxima[i]
      reserva_TV+=reserva[i]
      reservatermica+=reserva[i]
      if reserva_por[i]>=parametros[0]:
         reservatotal2+=reserva[i]
      if reserva_por[i]>porcentaje[i]:
         reservatermica_rpf+=P[i]*porcentaje[i]/100
      else:
         reservatermica_rpf+=reserva[i]
   elif clase=='CC':
      pot_CC+=potencia_maxima[i]
      reserva_CC+=reserva[i]
      reservatermica+=reserva[i]
      if reserva_por[i]>=parametros[0]:
         reservatotal2+=reserva[i]
      if reserva_por[i]>porcentaje[i]:
         reservatermica_rpf+=P[i]*porcentaje[i]/100
      else:
         reservatermica_rpf+=reserva[i]

reservahidro=round(reservahidro,2)
reservatermica=round(reservatermica,2)
reservahidro_rpf=round(reservahidro_rpf,2)
reservatermica_rpf=round(reservatermica_rpf,2)
pot_hidro=round(pot_hidro,2)
pot_TV=round(pot_TV,2)
pot_CC=round(pot_CC,2)
pot_TG=round(pot_TG,2)
reserva_TV=round(reserva_TV,2)
reserva_CC=round(reserva_CC,2)
reserva_TG=round(reserva_TG,2)
reservahidro_rpf=round(reservahidro_rpf,2)
reservatermica_rpf=round(reservatermica_rpf,2)
reserva_nueva=parametros[0]*generacion_total/100
reservatotal2=round(reservatotal2,2)

print('****************************************************************************************')
print('RESERVA ROTANTE EN MAQUINAS QUE REGULAN')
print('-----')
print('RESERVA HIDRO [MW]',reservahidro)
print('RESERVA TERMICA [MW]',reservatermica)
print('RESERVA TOTAL [MW]',reservahidro+reservatermica)
print('RESERVA ROTANTE DEL PARQUE REGULANTE [%]',round(((reservatermica+reservahidro)/generacion_total)*100,2))
print('-----')
print('RESERVA PROGRAMADA A 50Hz PARA RPF')
print('RESERVA HIDRO RPF [MW]',reservahidro_rpf)
print('RESERVA TERMICA RPF [MW]',reservatermica_rpf)
print('RESERVA TOTAL SISTEMA [MW]',reservatermica_rpf+reservahidro_rpf)
print('RESERVA PARA RPF [%]',round(((reservatermica_rpf+reservahidro_rpf)/generacion_total)*100,2))
print('COLABORACIÓN DEL PARQUE HIDRO EN RSF [MW]',reservahidro-reservahidro_rpf)
print('COLABORACIÓN DEL PARQUE HIDRO EN RSF [%]',round(((reservahidro-reservahidro_rpf)/generacion_total)*100,2))
print('-----')
print('POTENCIA OPERABLE EN EL PARQUE REGULANTE')
print('HIDRO [MW]',pot_hidro)
print('TERM. TG-CC [MW]',pot_TG+pot_CC)
print('TERM. TV [MW]',pot_TV)
print('TOTAL [MW]',pot_TV+pot_TG+pot_hidro)
print('-----')
print('RESERVA PROGRAMADA EN EL PARQUE REGULANTE')
print('HIDRO [MW]',reservahidro_rpf)
print('TERM. TG-CC [MW]',reserva_TG+reserva_CC)
print('TERM. TV [MW]',reserva_TV)
print('TOTAL [MW]',reserva_TV+reserva_TG+reservahidro_rpf)
print('RESERVA NUEVA',round(parametros[0]*generacion_total/100,2))
print('RESERVA TOTAL2',reservatotal2)

informe.reserva_total(ruta,reservahidro,reservatermica,reservahidro_rpf,reservatermica_rpf,
                     pot_hidro,pot_TG,pot_CC,pot_TV,reserva_TV,reserva_CC,reserva_TG,
                     generacion_total,reserva_nueva,reservatotal2)
'''
# Potencia operable en el parque regulante


'            ************************'
'            *    C.A.M.M.E.S.A.    *'
'            ************************'
' '
'------------------------------------------------------------------------------------'
'Gcia. de Programación de la Producción - Gcia. de Análisis y Control de la Producción'
'      Area Sistemas de Potencia        -            Area Modelos'
'------------------------------------------------------------------------------------'
' '
'**************************'
'* ANALISIS DE LA RESERVA *'
'**************************'
' '

'ESCENARIO:'
'------------------------------------------------------------'
title1
title2
#'------------------------------------------------------------'
'RESERVA ROTANTE EN MAQUINAS QUE REGULAN '
'--------------------------------------- '
'                TOTAL HIDRO          (MW) =',reservahidro:10.2 (es la suma de todos los hidraulicos)
'                TOTAL TERMICA        (MW) =',reservatermi:10.2 (es la suma de todos los termicos)
'                TOTAL SISTEMA        (MW) =',(reservatermi+RESERVAHIDRO):10.2 (suma de termicos e hidraulicos)
'-----------------------------------------------------------'
'RESERVA ROTANTE DEL PARQUE REGULANTE  (%) =',((((reservatermi+RESERVAHIDRO))/(GENSADI))*100.):9.2
(porcenaje de reserva respecto del total de la generacion)
'-----------------------------------------------------------'
 ' '
'RESERVA PROGRAMADA A 50Hz PARA RPF '
'---------------------------------- '
'                 RESERVA HIDRO   10% (MW) =',reservaHIDRO5:10.2
'                 RESERVA TERMICA  5% (MW) =',reservaTERMI5:10.2
'                 TOTAL   SISTEMA     (MW) =',(reservaTERMI5+reservaHIDRO5):10.2
(esta parte es lo mismo solo que la reserva tiene que ser mayor al porcentaje establecido como dato)
'-----------------------------------------------------------'
'RESERVA PARA RPF                      (%) =',(((reservaTERMI5+reservaHIDRO5)/(GENSADI))*100.):9.2
(calcula el porcentaje como antes pero con los datos anteriores)
'-----------------------------------------------------------'
 ' '
'COLABORACIÓN DEL PARQUE HIDRO EN RSF (MW) =',(reservahidro-reservaHIDRO5):10.2
'COLABORACIÓN DEL PARQUE HIDRO EN RSF  (%) =',(((reservahidro-reservaHIDRO5)/GENSADI)*100.):10.2
 ' '
'POTENCIA OPERABLE EN EL PARQUE REGULANTE '
'---------------------------------------- '
'                         HIDRO       (MW) =',pothi:10.2 (suma de potencias maximas de hidraulicos)
'                         TERM. TG-CC (MW) =',pottg:10.2 (suma de potencias maximas de las tgs)
'                         TERM. TV    (MW) =',pottv:10.2 (suma de potencias maximas de las tvs)
'                     ----TOTAL------ (MW) =',(pottv+pottg+pothi):10.2 (suma total de potencias maximas)
 ' '
'RESERVA PROGRAMADA EN EL PARQUE REGULANTE '
'----------------------------------------- '
'                         HIDRO       (MW) =',reservaHIDRO5:10.2
'                         TERM. TG-CC (MW) =',restg:10.2 (reserva de las tgs)
'                         TERM. TV    (MW) =',restv:10.2 (reserva de las tvs)
'                     ----TOTAL------ (MW) =',(restv+restg+reservaHIDRO5):10.2 (suma total de las reservas)
 ' '

RESERVANUEVA =((RESERVAOPTIMA/100.)*(GENSADI))
' '
'==========================================================='
' RESERVANUEVA = ',RESERVANUEVA
' RESERVAtotal2 = ',RESERVATOTAL2 (es la suma de todas las reservas menores a la optima)
'''

# 14 - Sección donde recorta si el parametro[1] es 1
print(parametros)
print(tipo)
if parametros[1]==1:
   print('recorta')
   if parametros[3]==0:
      print('ambas')
   elif parametros[3]==1:
      print('termicas')
   elif parametros[3]==2:
      print('hidraulicas')
   if parametros[2]==0:
      print('optima')
      dif_nueva=list()
      pmaxinueva=list()
      reserva_nuevax=0
      for i in range(0,len(reserva)):
         if parametros[3]==1 and tipo[i]!='HI':
            if reserva_por[i]>parametros[0]:
               dif_nueva.append(reserva_nueva*reserva[i]/sum(reserva))
            else:
               dif_nueva.append(0)
            if reserva_por[i]>parametros[0]:
               pmaxinueva.append(P[i]+dif_nueva[i])
            else:
               pmaxinueva.append(0)
            if pmaxinueva[i]>0:
               reserva_nuevax+=(pmaxinueva[i]-P[i])
         elif parametros[3]==2 and tipo[i]=='HI':
            if reserva_por[i]>parametros[0]:
               dif_nueva.append(reserva_nueva*reserva[i]/sum(reserva))
            else:
               dif_nueva.append(0)
            if reserva_por[i]>parametros[0]:
               pmaxinueva.append(P[i]+dif_nueva[i])
            else:
               pmaxinueva.append(0)
            if pmaxinueva[i]>0:
               reserva_nuevax+=(pmaxinueva[i]-P[i])
         elif parametros[3]==0:
            if reserva_por[i]>parametros[0]:
               dif_nueva.append(reserva_nueva*reserva[i]/sum(reserva))
            else:
               dif_nueva.append(0)
            if reserva_por[i]>parametros[0]:
               pmaxinueva.append(P[i]+dif_nueva[i])
            else:
               pmaxinueva.append(0)
            if pmaxinueva[i]>0:
               reserva_nuevax+=(pmaxinueva[i]-P[i])
         else:
            dif_nueva.append(0)
            pmaxinueva.append(0)
      print(reserva)
      print(dif_nueva)
      print(pmaxinueva)
      print(reserva_nuevax)
      print('-------------')
   else:
      print('dato')
      pmaxinueva=list()
      dif_nueva=list()
      for i in range(0,len(P)):
            if parametros[3]==1 and tipo[i]!='HI':
               if reserva_por[i]>parametros[0]:
                  dif_nueva.append(reserva_nueva*reserva[i]/sum(reserva))
               else:
                  dif_nueva.append(0)
               if reserva_por[i]>parametros[0]:
                  pmaxinueva.append(P[i]*(1+porcentaje[i]/100))
               else:
                  pmaxinueva.append(0)
            elif parametros[3]==2 and tipo[i]=='HI':
               if reserva_por[i]>parametros[0]:
                  dif_nueva.append(reserva_nueva*reserva[i]/sum(reserva))
               else:
                  dif_nueva.append(0)
               if reserva_por[i]>parametros[0]:
                  pmaxinueva.append(P[i]*(1+porcentaje[i]/100))
               else:
                  pmaxinueva.append(0)
            elif parametros[3]==0:
               if reserva_por[i]>parametros[0]:
                  dif_nueva.append(reserva_nueva*reserva[i]/sum(reserva))
               else:
                  dif_nueva.append(0)
               if reserva_por[i]>parametros[0]:
                  pmaxinueva.append(P[i]*(1+porcentaje[i]/100))
               else:
                  pmaxinueva.append(0)
            else:
               dif_nueva.append(0)
               pmaxinueva.append(0)
      print(reserva)
      print(P)
      print(dif_nueva)
      print(pmaxinueva)
      print('-------------')

   # 15 - Analisis de cada governor para cambiar los limites (2204)
   # 16  - Análisis de cada governor para determinar los margenes de reserva con los limites corregidos (2813)
   reserva_cl=list()
   potencia_maxima_cl=list()
   for i,gov in enumerate(governor):
      if reserva_por[i]>parametros[0] and dif_nueva[i]>0:
         CL.cambiar_limites(governor[i], indice_ini[i], rval[i], v[i], P[i], dif_nueva[i], pmaxinueva[i],CON[i])
      else:
         print('no se cambia en ', governor[i])

   def volver_a_simular():
      # Cargar el caso
      psspy.case('savnw.sav')
      
      # Configurar la simulación
      psspy.cong(0)
      psspy.conl(0, 1, 1, [0, 0], [100.0, 0.0, 0.0, 100.0])
      psspy.conl(0, 1, 2, [0, 0], [100.0, 0.0, 0.0, 100.0])
      psspy.conl(0, 1, 3, [0, 0], [100.0, 0.0, 0.0, 100.0])
      psspy.fact()
      psspy.tysl(0)
      
      # Inicializar la simulación
      #ierr = psspy.strt(0, 'output_file.out')
      #if ierr != 0:
        # print('Error al inicializar la simulación')
         #return
    
      # Ejecutar la simulación
      ierr = psspy.run(0, 1.0, 1, 1, 0)
      if ierr != 0:
         print('Error al ejecutar la simulación')
         return
   volver_a_simular()

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
      if res==(pmax-P[i]):
         correcto='Correcto'
      else:
         correcto='Incorrecto'
      print('potencia maxima ',round(pmax,2), 'potencia operativa ',round(P[i],2), 'reserva ',round(res,2), 'resultado ',correcto)
      reserva.append(res)
      potencia_maxima.append(pmax)

   reserva_por=list()
   for i in range(0,len(bus)):
      reserva_por.append(round(((reserva[i]/P[i])*100),2))

   print(reserva)
   print(reserva_por)
   print(potencia_maxima)
   # Calculo de la reserva de los hidraulicos, termicos y ambos
   reservahidro=0
   reservatermica=0
   reservahidro_rpf=0
   reservatermica_rpf=0
   pot_hidro=0
   pot_TV=0
   pot_CC=0
   pot_TG=0
   reserva_TV=0
   reserva_CC=0
   reserva_TG=0
   reservatotal2=0
   
   for i,clase in enumerate(tipo):
      if clase=='HI':
         pot_hidro+=potencia_maxima[i]
         reservahidro+=reserva[i]
         if reserva_por[i]>=parametros[0]:
            reservatotal2+=reserva[i]
         if reserva_por[i]>porcentaje[i]:
            reservahidro_rpf+=P[i]*porcentaje[i]/100
         else:
            reservahidro_rpf+=reserva[i]
      elif clase=='TG':
         pot_TG+=potencia_maxima[i]
         reserva_TG+=reserva[i]
         reservatermica+=reserva[i]
         if reserva_por[i]>=parametros[0]:
            reservatotal2+=reserva[i]
         if reserva_por[i]>porcentaje[i]:
            reservatermica_rpf+=P[i]*porcentaje[i]/100
         else:
            reservatermica_rpf+=reserva[i]
      elif clase=='TV':
         pot_TV+=potencia_maxima[i]
         reserva_TV+=reserva[i]
         reservatermica+=reserva[i]
         if reserva_por[i]>=parametros[0]:
            reservatotal2+=reserva[i]
         if reserva_por[i]>porcentaje[i]:
            reservatermica_rpf+=P[i]*porcentaje[i]/100
         else:
            reservatermica_rpf+=reserva[i]
      elif clase=='CC':
         pot_CC+=potencia_maxima[i]
         reserva_CC+=reserva[i]
         reservatermica+=reserva[i]
         if reserva_por[i]>=parametros[0]:
            reservatotal2+=reserva[i]
         if reserva_por[i]>porcentaje[i]:
            reservatermica_rpf+=P[i]*porcentaje[i]/100
         else:
            reservatermica_rpf+=reserva[i]

   reservahidro=round(reservahidro,2)
   reservatermica=round(reservatermica,2)
   reservahidro_rpf=round(reservahidro_rpf,2)
   reservatermica_rpf=round(reservatermica_rpf,2)
   pot_hidro=round(pot_hidro,2)
   pot_TV=round(pot_TV,2)
   pot_CC=round(pot_CC,2)
   pot_TG=round(pot_TG,2)
   reserva_TV=round(reserva_TV,2)
   reserva_CC=round(reserva_CC,2)
   reserva_TG=round(reserva_TG,2)
   reservahidro_rpf=round(reservahidro_rpf,2)
   reservatermica_rpf=round(reservatermica_rpf,2)
   reserva_nueva=parametros[0]*generacion_total/100
   reservatotal2=round(reservatotal2,2)

   informe.reserva_total_recorte(ruta,reservahidro,reservatermica,reservahidro_rpf,reservatermica_rpf,
                        pot_hidro,pot_TG,pot_CC,pot_TV,reserva_TV,reserva_CC,reserva_TG,
                        generacion_total,reserva_nueva,reservatotal2)
   print('****************************************************************************************')
   print('****************************************************************************************')
   print('LUEGO DEL RECORTE QUEDA')
   print('RESERVA ROTANTE EN MAQUINAS QUE REGULAN')
   print('-----')
   print('RESERVA HIDRO [MW] ',reservahidro)
   print('RESERVA TERMICA [MW] ',reservatermica)
   print('RESERVA TOTAL [MW] ',reservahidro+reservatermica)
   print('RESERVA ROTANTE DEL PARQUE REGULANTE [%] ',round(((reservatermica+reservahidro)/generacion_total)*100,2))
   print('-----')
   print('RESERVA PROGRAMADA A 50Hz PARA RPF')
   print('RESERVA HIDRO RPF [MW] ',reservahidro_rpf)
   print('RESERVA TERMICA RPF [MW] ',reservatermica_rpf)
   print('RESERVA TOTAL SISTEMA [MW] ',reservatermica_rpf+reservahidro_rpf)
   print('RESERVA PARA RPF [%] ',round(((reservatermica_rpf+reservahidro_rpf)/generacion_total)*100,2))
   print('POTENCIA OPERABLE EN EL PARQUE REGULANTE')
   print('HIDRO [MW] ' ,pot_hidro)
   print('TERM. TG-CC [MW] ',pot_TG+pot_CC)
   print('TERM. TV [MW] ',pot_TV)
   print('TOTAL [MW] ',pot_TV+pot_TG+pot_hidro)
   print('-----')
   print('RESERVA PROGRAMADA EN EL PARQUE REGULANTE')
   print('HIDRO [MW] ',reservahidro_rpf)
   print('TERM. TG-CC [MW] ',reserva_TG+reserva_CC)
   print('TERM. TV [MW] ',reserva_TV)
   print('TOTAL [MW] ',reserva_TV+reserva_TG+reservahidro_rpf)
   print('RESERVA NUEVA ',round(parametros[0]*generacion_total/100,2))
   print('RESERVA TOTAL2 ',reservatotal2)

'''
'-----------------------------------------------------------'
'LUEGO DEL RECORTE EN LA POTENCIA MAXIMA '
'(PARA OBTENER UNA RESERVA ROTANTE TOTAL EN MAQ.'
'REG IGUAL A ROPT dato.)'
'-----------------------------------------------------------'
' '
'RESERVA ROTANTE EN MAQUINAS QUE REGULAN '
'--------------------------------------- '
'                TOTAL HIDRO          (MW) =',reservahidro:10.2 (es la suma de todos los hidraulicos)
'                TOTAL TERMICA        (MW) =',reservatermi:10.2 (es la suma de todos los termicos)
'                TOTAL SISTEMA        (MW) =',(reservatermi+RESERVAHIDRO):10.2 (suma de termicos e hidraulicos)
'-----------------------------------------------------------'
'RESERVA ROTANTE DEL PARQUE REGULANTE  (%) =',((((reservatermi+RESERVAHIDRO))/(GENSADI))*100.):9.2 
(porcenaje de reserva respecto del total de la generacion)
'-----------------------------------------------------------'
 ' '
'RESERVA PROGRAMADA A 50Hz PARA RPF '
'---------------------------------- '
'                 RESERVA HIDRO   10% (MW) =',reservaHIDRO5:10.2
'                 RESERVA TERMICA  5% (MW) =',reservaTERMI5:10.2
'                 TOTAL   SISTEMA     (MW) =',(reservaTERMI5+reservaHIDRO5):10.2
(esta parte es lo mismo solo que la reserva tiene que ser mayor al porcentaje establecido como dato)
'-----------------------------------------------------------'
'RESERVA PARA RPF                      (%) =',(((reservaTERMI5+reservaHIDRO5)/(GENSADI))*100.):9.2 (calcula el porcentaje como antes pero con los datos anteriores)
'-----------------------------------------------------------'
 ' '
'POTENCIA OPERABLE EN EL PARQUE REGULANTE '
'---------------------------------------- '
'                         HIDRO       (MW) =',pothi:10.2 (suma de potencias maximas de hidraulicos)
'                         TERM. TG-CC (MW) =',pottg:10.2 (suma de potencias maximas de las tgs)
'                         TERM. TV    (MW) =',pottv:10.2 (suma de potencias maximas de las tvs)
(suma de potencias maximas de cada tipo de maquina)
'                     ----TOTAL------ (MW) =',(pottv+pottg+pothi):10.2(suma total de potencias maximas)
 ' '
'RESERVA PROGRAMADA EN EL PARQUE REGULANTE '
'----------------------------------------- '
'                         HIDRO       (MW) =',reservaHIDRO5:10.2
'                         TERM. TG-CC (MW) =',restg:10.2 (reserva de las tgs)
'                         TERM. TV    (MW) =',restv:10.2 (reserva de las tvs)
'                     ----TOTAL------ (MW) =',(restv+restg+reservaHIDRO5):10.2
 ' '
' RESERVANUEVA = ',RESERVANUEVA
' RESERVAtotal2 = ',RESERVATOTAL2 (es la suma de todas las reservas)

'''
 

   

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
donde 
difegen es la reserva
reservatotal2 es la reserva total

PMAXINUE(IGEN)=P(IGEN)+DIFNUE(IGEN) se calcula nueva potencia maxima del generador para poder cambiar los limites
donde p es la potencia del generador (se usa en caso de hacerlo con respecto a la optima)

PMAXINUE2(IGEN)=P(I.+PORCE(IGEN)/100.) se calcula la nueva potencia maxima en base al porcentaje del generador
donde porce es el porcentaje del generador (se usa en caso de hacerlo con respecto al dato)

RESERVANUEVAX=(PMAXINUE(IGEN)-P(IGEN))+RESERVANUEVAX suma de las reservas basada en la potencia de reserva optima

totadif=totadif+DIFNUE(IGEN)
nueva reserva total

totamax=totamax+pmaxiNUE(IGEN)-P(IGEN)
otra nueva reserva total
"""
