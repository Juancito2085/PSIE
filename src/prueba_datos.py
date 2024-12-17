import os
import sys

import sys
import os

sys_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSPY34'
os_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSBIN'

# Configurar las rutas seleccionadas
sys.path.append(sys_path_PSSE)
os.environ['PATH'] += '' + os_path_PSSE
os.environ['PATH'] += '' + sys_path_PSSE

import datetime
import re
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

caso = 'savnw.sav'
entrada = 'C:/Users/jcbru/Desktop/psie/Reserva_entrada.xlsx'
nombre_archivo = 'informe de prueba'
destino = 'C:/Users/jcbru/Desktop/psie'

psspy.psseinit(1000)

psspy.case(caso)

psspy.cong(0)
psspy.conl(0,1,1,[0,0],[ 100.0,0.0,0.0, 100.0])
psspy.conl(0,1,2,[0,0],[ 100.0,0.0,0.0, 100.0])
psspy.conl(0,1,3,[0,0],[ 100.0,0.0,0.0, 100.0])
psspy.fact()
psspy.tysl(0)

# Open snap.
sfile = caso.split('.')[0]
psspy.rstr(sfile)
psspy.dynamicsmode(0)

# Se leen datos de los generadores
bus,governor,CON,porcentaje,idg,comentario,tipo=lectura.generadores(entrada)

#Verificacion de los datos
nombre=list()
cmpval=list()
v=list()
v1=list()
indice_ini=list()
rval=list()
ierr=list()
for i in range(0,len(bus)):
    print(bus[i],governor[i],CON[i])
    nombre_temp, cmpval_temp,v_temp,v1_temp, indice_ini_temp,rval_temp, ierr_temp = verificaciondatos.generadores(destino, nombre_archivo,bus[i],idg[i],CON[i])
    nombre.append(nombre_temp.split()[0])
    cmpval.append(cmpval_temp)
    v.append(v_temp)
    v1.append(v1_temp)
    indice_ini.append(indice_ini_temp)
    rval.append(rval_temp)
    ierr.append(ierr_temp)
print(nombre,cmpval,v,v1,indice_ini,rval, ierr)

# Se extrae la potencia máxima de los generadores
pmax = psspy.amachreal(-1, 4, 'PMAX')
pmax = pmax[1][0]
nombre = psspy.amachchar(-1, 4, 'NAME') 
nombre = nombre[1][0]
nombres = list()
for i in nombre:
    nombres.append(i.strip())

# Se crea un diccionario
generadores = dict()
generadores['pmax'] = pmax
generadores['nombre'] = nombres

# Se muestran las potencias máximas de los generadores
for i in range(len(generadores['nombre'])):
    print(generadores['nombre'][i], round(generadores['pmax'][i],2))

valores_cons= list()
valores_cons_cambiados = list()
# Mostrar los valores de los CONS para cada generador
for i in range(len(bus)):
    print('Generador ' +generadores['nombre'][i],' Bus ', bus[i])
    ierr, con_value = psspy.dsrval('CON', (indice_ini[i] + CON[i]))
    valores_cons.append(con_value)


# Abro el snap de savwn_nuevo.snp
psspy.rstr('C:/Users/jcbru/Desktop/psie/savnw_nuevo.snp')

# Mostrar los valores de los CONS para cada generador
for i in range(len(bus)):
    print('Generador ' +generadores['nombre'][i],' Bus ', bus[i])
    ierr, con_value_cambiado = psspy.dsrval('CON', indice_ini[i] + CON[i])
    valores_cons_cambiados.append(con_value_cambiado)

for i in range(len(bus)):
    print('Generador ' + generadores['nombre'][i], ' CON: ', valores_cons[i], ' CON nuevo: ', valores_cons_cambiados[i])