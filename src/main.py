'''import os
import sys
#ruta para notebook
#os_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSPY34'
#ruta para pc de escritorio
sys_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSPY34'
sys.path.append(sys_path_PSSE)

#ruta para notebook
#os_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSBIN'
#ruta para pc de escritorio
os_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSBIN'
os.environ['PATH'] += '' + os_path_PSSE
os.environ['PATH'] += '' + sys_path_PSSE

# Importación de librerias necesarias
#import redirect
import datetime
import re
import tkinter as tk
from tkinter import filedialog, messagebox,Menu
import pssexplore34
import psspy'''

import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

# verificamos que exista el archivo de configuracion
if  not os.path.exists("reserva7_cfg.txt"):       
    # Crear una ventana oculta para usar los diálogos de archivo
    root = tk.Tk()
    root.title("Seleccionar Directorios")

    # Definir el tamaño de la ventana secundaria
    window_width = 600
    window_height = 400

    # Obtener el tamaño de la pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calcular la posición para centrar la ventana secundaria
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    # Establecer la geometría de la ventana secundaria usando format()
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, position_right, position_top))


    # Variables globales para almacenar las rutas seleccionadas
    sys_path_PSSE = None
    os_path_PSSE = None

    # Función para seleccionar el directorio sys_path_PSSE
    def seleccionar_sys_path_PSSE():
        global sys_path_PSSE
        while True:
            sys_path_PSSE = filedialog.askdirectory(title="Seleccionar directorio de la carpeta PSSPY34")
            if sys_path_PSSE:
                if sys_path_PSSE.endswith("PSSPY34"):
                    sys_path_label.config(text="sys_path_PSSE: " + sys_path_PSSE)
                    break
                else:
                    messagebox.showerror("Error", "El directorio seleccionado debe terminar con 'PSSPY34'. Por favor, seleccione nuevamente.")

    # Función para seleccionar el directorio os_path_PSSE
    def seleccionar_os_path_PSSE():
        global os_path_PSSE
        while True:
            os_path_PSSE = filedialog.askdirectory(title="Seleccionar directorio de la carpeta PSSBIN")
            if os_path_PSSE:
                if os_path_PSSE.endswith("PSSBIN"):
                    os_path_label.config(text="os_path_PSSE: " + os_path_PSSE)
                    break
                else:
                    messagebox.showerror("Error", "El directorio seleccionado debe terminar con 'PSSBIN'. Por favor, seleccione nuevamente.")
            else:
                break

    # Función para confirmar las selecciones y cerrar la ventana
    def confirmar_seleccion():
        if not sys_path_PSSE or not os_path_PSSE:
            messagebox.showerror("Error", "Debe seleccionar ambos directorios para continuar.")
        else:
            with open("reserva7_cfg.txt", "w") as f:
                f.write("sys_path_PSSE: " + sys_path_PSSE + "\n")
                f.write("os_path_PSSE: " + os_path_PSSE + "\n")
            root.destroy()

    # Guardar las rutas seleccionadas en un .txt
    def guardar_rutas():
        with open("reserva7_cfg.txt", "w") as f:
            f.write("sys_path_PSSE: " + sys_path_PSSE + "\n")
            f.write("os_path_PSSE: " + os_path_PSSE + "\n")

    # Crear etiquetas y botones para seleccionar los directorios
    sys_path_label = tk.Label(root, text="sys_path_PSSE: No seleccionado")
    sys_path_label.pack(pady=10)

    btn_seleccionar_sys_path = tk.Button(root, text="Seleccionar sys_path_PSSE", command=seleccionar_sys_path_PSSE)
    btn_seleccionar_sys_path.pack(pady=10)

    os_path_label = tk.Label(root, text="os_path_PSSE: No seleccionado")
    os_path_label.pack(pady=10)

    btn_seleccionar_os_path = tk.Button(root, text="Seleccionar os_path_PSSE", command=seleccionar_os_path_PSSE)
    btn_seleccionar_os_path.pack(pady=10)

    btn_confirmar = tk.Button(root, text="Confirmar", command=confirmar_seleccion)
    btn_confirmar.pack(pady=20)

    # Ejecutar el bucle principal de tkinter
    root.mainloop()
else:
    with open("reserva7_cfg.txt", "r") as f:
        lines = f.readlines()
        sys_path_PSSE = lines[0].split(": ")[1].strip()
        os_path_PSSE = lines[1].split(": ")[1].strip()
        
# Verificar que los directorios hayan sido seleccionados
if not sys_path_PSSE or not os_path_PSSE:
    sys.exit(1)

# Configurar las rutas seleccionadas
sys.path.append(sys_path_PSSE)
os.environ['PATH'] += '' + os_path_PSSE
os.environ['PATH'] += '' + sys_path_PSSE

# Importación de librerías necesarias
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

# Definir las variables globales
destino = None
caso = None
nombre = None
entrada = None
 
# Definición de las funciones

def seleccionar_entrada():
    global entrada
    entrada = filedialog.askopenfilename(title="Seleccionar entrada")
    if entrada:
        extension = os.path.splitext(entrada)[1]
        if extension.lower() in ['.xlsx']:  # Verificar si la extensión es .xlsx
            entrada_label.config(text="Archivo seleccionado: " + entrada)
        else:
            tk.messagebox.showerror("Error", "El archivo seleccionado no tiene una extensión válida .xlsx")
            entrada = None

def seleccionar_destino():
    global destino
    destino = filedialog.askdirectory(title="Seleccionar destino")
    destino_label.config(text="Carpeta seleccionada: "+ destino)

def seleccionar_caso():
    global caso
    caso = filedialog.askopenfilename(title="Seleccionar caso")
    if caso:
        extension = os.path.splitext(caso)[1]
        if extension.lower() in ['.sav']:  # Verificar si la extensión es .sav
            #se extrae la extension del archivo
            caso_label.config(text="Caso seleccionado: " + caso)
        else:
            tk.messagebox.showerror("Error", "El archivo seleccionado no tiene una extensión válida (.sav)")
            caso = None
def seleccionar_snap():
    global snap
    snap = filedialog.askopenfilename(title="Seleccionar snap")
    if snap:
        extension = os.path.splitext(snap)[1]
        if extension.lower() in ['.snp']:  # Verificar si la extensión es .sav
            #se extrae la extension del archivo
            snap_label.config(text="Snap seleccionado: " + snap)
        else:
            tk.messagebox.showerror("Error", "El archivo seleccionado no tiene una extensión válida (.snp)")
            snap = None

def nombre_informe():
    global nombre
    nombre = nombre.entry.get()
    nombre_label.config(text="Nombre del informe: " + nombre)

def abrir_ventana_secundaria():
    ventana_secundaria = tk.Toplevel(root)
    ventana_secundaria.title("Nombre del informe")

    # Definir el tamaño de la ventana secundaria
    window_width = 400
    window_height = 300

    # Obtener el tamaño de la pantalla
    screen_width = ventana_secundaria.winfo_screenwidth()
    screen_height = ventana_secundaria.winfo_screenheight()

    # Calcular la posición para centrar la ventana secundaria
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    # Establecer la geometría de la ventana secundaria usando format()
    ventana_secundaria.geometry("{}x{}+{}+{}".format(window_width, window_height, position_right, position_top))

    tk.Label(ventana_secundaria, text="Escriba el nombre del informe").pack(pady=20)
    
    nombre_entry_secundaria = tk.Entry(ventana_secundaria)
    nombre_entry_secundaria.pack(pady=10)

    # Crear variables para el estado de los checkboxes
    incluir_hora_var = tk.IntVar()
    incluir_fecha_var = tk.IntVar()
    
    # Crear los checkboxes
    tk.Checkbutton(ventana_secundaria, text="Incluir hora", variable=incluir_hora_var).pack(pady=10)
    tk.Checkbutton(ventana_secundaria, text="Incluir fecha", variable=incluir_fecha_var).pack(pady=10)

    global hora
    global fecha

    # Lógica de los checkboxes
    if incluir_hora_var.get() == 1:
        
        hora = datetime.datetime.now().strftime("%H:%M:%S")
    if incluir_fecha_var.get() == 1:
        
        fecha = datetime.datetime.now().strftime("%d/%m/%Y")

    # Función para guardar el nombre del informe y cerrar la ventana secundaria
    def guardar_y_cerrar():
        global nombre
        nombre = nombre_entry_secundaria.get()
        
        hora = ""
        fecha = ""

        # Lógica de los checkboxes
        if incluir_hora_var.get() == 1:
            hora = "_" + datetime.datetime.now().strftime("%H%M%S")
        if incluir_fecha_var.get() == 1:
            fecha = "_" + datetime.datetime.now().strftime("%d%m%Y")
        nombre_label.config(text="Nombre del informe: " + nombre+hora+fecha)
        nombre=nombre+hora+fecha

        ventana_secundaria.destroy()

    tk.Button(ventana_secundaria, text="Guardar", command=guardar_y_cerrar).pack(pady=10)
    

def quit_app():
    root.quit()

# Creacion de la ventana principal
root = tk.Tk()
root.title("Calculo de reserva")

# Obtener el tamaño de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Definir el tamaño de la ventana
window_width = 1350
window_height = 900

# Calcular la posición para centrar la ventana
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

# Establecer la geometría de la ventana
root.geometry("{}x{}+{}+{}".format(window_width, window_height, position_right, position_top))

# Label para mostrar el archivo de entrada
entrada_label = tk.Label(root, text="Selecciona un archivo de entrada", font=("Arial", 14))
entrada_label.pack(pady=20)

# Crear botones
btn_seleccionar_entrada = tk.Button(root, text="Seleccionar entrada", command=seleccionar_entrada, width=20, height=2)
btn_seleccionar_entrada.pack(pady=10)

# Label para mostrar el destino seleccionado
destino_label = tk.Label(root, text="Selecciona una carpeta para guardar el informe", font=("Arial", 14))
destino_label.pack(pady=20)

# Crear botón para seleccionar el destino
btn_seleccionar_destino = tk.Button(root, text="Seleccionar destino", command=seleccionar_destino, width=20, height=2)
btn_seleccionar_destino.pack(pady=10)

# Label para mostrar el caso seleccionado
caso_label = tk.Label(root, text="Selecciona un caso para realizar el análisis", font=("Arial", 14))
caso_label.pack(pady=20)

# Crear botón para seleccionar el caso
btn_seleccionar_caso = tk.Button(root, text="Seleccionar caso", command=seleccionar_caso, width=20, height=2)
btn_seleccionar_caso.pack(pady=10)

# Label para mostrar el snap seleccionado
snap_label = tk.Label(root, text="Selecciona un snap para realizar el análisis", font=("Arial", 14))
snap_label.pack(pady=20)

# Crear botón para seleccionar el snap
btn_seleccionar_snap = tk.Button(root, text="Seleccionar snap", command=seleccionar_snap, width=20, height=2)
btn_seleccionar_snap.pack(pady=10)

# Crear un label para mostrar el nombre del informe
nombre_label = tk.Label(root, text="Sin nombre seleccionado", font=("Arial", 14))
nombre_label.pack(pady=20)

# Crear botón para abrir la ventana secundaria
btn_nombre_informe = tk.Button(root, text="Nombre informe", command=abrir_ventana_secundaria, width=20, height=2)
btn_nombre_informe.pack(pady=10)

# Crear botón para ejecutar el script
btn_ejecutar = tk.Button(root, text="Ejecutar", command=lambda: ejecutar(entrada, destino, caso, nombre), width=40, height=4)
btn_ejecutar.pack(pady=10)

btn_salir = tk.Button(root, text="Salir", command=quit_app, width=20, height=2)
btn_salir.pack(pady=30)

def ejecutar(entrada, destino, caso, nombre_archivo):
    print(destino,caso, nombre_archivo)
    if entrada is None:
        tk.messagebox.showerror("Error", "No se ha seleccionado un archivo de entrada")
        return
    elif destino is None:
        tk.messagebox.showerror("Error", "No se ha seleccionado una carpeta de destino")
        return
    elif caso is None:
        tk.messagebox.showerror("Error", "No se ha seleccionado un caso")
        return
    elif nombre_archivo is None:
        tk.messagebox.showerror("Error", "No se ha seleccionado un nombre para el informe")
        return
    tk.messagebox.showinfo("Ejecutando", "El script se está ejecutando")

    _i = psspy.getdefaultint()
    _f = psspy.getdefaultreal()
    _s = psspy.getdefaultchar()

    psspy.psseinit(1000)

    psspy.case(caso)

    psspy.cong(0)
    psspy.conl(0,1,1,[0,0],[ 100.0,0.0,0.0, 100.0])
    psspy.conl(0,1,2,[0,0],[ 100.0,0.0,0.0, 100.0])
    psspy.conl(0,1,3,[0,0],[ 100.0,0.0,0.0, 100.0])
    psspy.fact()
    psspy.tysl(0)

    # Abrir el snap
    sfile = snap
    psspy.rstr(sfile)
    psspy.dynamicsmode(0)
    nombre_archivo=nombre_archivo +'.xlsx'

    # 1 - Crear el archivo de salida
    informe.crear(destino, nombre_archivo)

    # 2 - Lectura de los parametros
    parametros=lectura.parametros(entrada)

    # 3 - Lectura de datos del archivo "reserva.dat"
    bus,governor,CON,porcentaje,idg,comentario,tipo=lectura.generadores(entrada)
    print(bus,governor,CON,porcentaje,idg,comentario,tipo)

    # 4 - Verificacion de los datos
    nombre=list()
    cmpval=list()
    v=list()
    v1=list()
    indice_ini=list()
    rval=list()
    ierr=list()
    for i in range(0,len(bus)):
        print(bus[i],governor[i],CON[i])
        nombre_temp, cmpval_temp,v_temp,v1_temp, indice_ini_temp,rval_temp, ierr_temp=verificaciondatos.generadores(destino, nombre_archivo,bus[i],idg[i],CON[i])
        nombre.append(nombre_temp.split()[0])
        cmpval.append(cmpval_temp)
        v.append(v_temp)
        v1.append(v1_temp)
        indice_ini.append(indice_ini_temp)
        rval.append(rval_temp)
        ierr.append(ierr_temp)
    print(nombre,cmpval,v,v1,indice_ini,rval, ierr)

    # 5 - Determinación de los margenes de reserva
    P=list()
    Q=list()
    for pq in cmpval:
        P.append(pq.real)
        Q.append(pq.imag)

    reserva=list()
    potencia_maxima=list()
    for i,gov in enumerate(governor):
        if ierr[i]==0:
            res,pmax=CR.calculo(gov,indice_ini[i],rval[i],v[i],P[i])
            if res==(pmax-P[i]):
                correcto='Correcto'
            else:
                correcto='Incorrecto'
            print('potencia maxima ',round(pmax,2), 'potencia operativa ',round(P[i],2), 'reserva ',round(res,2), 'resultado ',correcto)
            reserva.append(res)
            potencia_maxima.append(pmax)
        else:
            reserva.append(0)
            potencia_maxima.append(0)

    # 6 - Registro de la reserva de todos los generadores en la hoja "Pmax_Pgen.prn"
    reserva_por=list()
    for i in range(0,len(bus)):
        reserva_por.append(round(((reserva[i]/P[i])*100),2))
        print('Porcentaje de reserva ',round(((reserva[i]/P[i])*100),2))
    informe.Pmax_Pgen(destino,nombre_archivo,bus,nombre,idg,potencia_maxima,P,reserva,reserva_por,porcentaje,parametros[0])

    # 7 - Registro de los generadores con reserva por debajo de la óptima
    informe.Menor_optima(destino,nombre_archivo, bus,nombre,idg,potencia_maxima,P,reserva,reserva_por,porcentaje,parametros[0])

    # 8 - Registro de los generadores con reserva mayor a la maxima
    informe.Mayor_maxima(destino,nombre_archivo, bus,nombre,idg,potencia_maxima,P,reserva,reserva_por,porcentaje,parametros[0])

    # 9 - Extracción de la generación del sistema
    ibus_sale,nombre_sale,id_sale=lectura.generadores_no_suman(entrada)

    cmpval_sale=list()
    ierr_gen_sale=list()
    for i in range(0,len(ibus_sale)):
        cmpval_sale_temp, ierr_gen_sale_temp = verificaciondatos.gensale(destino, nombre_archivo, ibus_sale[i],nombre_sale[i],id_sale[i])
        cmpval_sale.append(cmpval_sale_temp)
        ierr_gen_sale.append(ierr_gen_sale_temp)
    pge=0
    for pq in cmpval_sale:
        if pq is not None and ierr_gen_sale==0:
            pge+=pq.real()

    # 10 - Areas a restar
    iarea,nombre_area=lectura.regiones_paises_limitrofes(entrada)

    for i in range(0,len(iarea)):
        cmpval_area=verificaciondatos.area(destino, nombre_archivo,iarea[i],nombre_area[i])

    pga=0

    for pq in cmpval_sale:
        if pq is not None:
            pga+=pq.real()

    # 11 - Generación total a restar
    total_A, total_R=generacion.total(destino, nombre_archivo)
    generacion_total=total_A
    print('la generacion total es ',generacion_total)
    print('la generacion a restar es ',pge)
    print('la generacion de las areas a restar es ',pga)

    # Revisar generacion total del SADI
    gensadi=generacion_total-pge-pga

    # Variables que se utilizan para el informe
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

    # 13 - Calculo de la reserva de los hidraulicos, termicos y ambos

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
    reserva_nueva=round(parametros[0]*generacion_total/100,2)
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

    informe.reserva_total(destino,nombre_archivo,reservahidro,reservatermica,reservahidro_rpf,reservatermica_rpf,
                        pot_hidro,pot_TG,pot_CC,pot_TV,reserva_TV,reserva_CC,reserva_TG,
                        generacion_total,reserva_nueva,reservatotal2)

    # 14 - Sección a la que ingresa en que el caso que se quiera recortar (en el caso de que parametro[1]==1)
    print(parametros)
    print(tipo)
    if parametros[1]==1:
        print('recorta')
        if parametros[3]==0:
            print('ambas')
            tipo_ajustado='AMBOS'
        elif parametros[3]==1:
            print('termicas')
            tipo_ajustado='TERMICAS'
        elif parametros[3]==2:
            print('hidraulicas')
            tipo_ajustado='HIDRAULICAS'
        if parametros[2]==0:
            print('optima')
            ajuste='ÓPTIMA'
            dif_nueva=list()
            pmaxinueva=list()
            reserva_nuevax=0
            for i in range(0,len(reserva)):
                if parametros[3]==1 and tipo[i]!='HI':
                    if reserva_por[i]>parametros[0]:
                        dif_nueva.append(reserva_nueva*reserva[i]/reservatotal2)
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
                        dif_nueva.append(reserva_nueva*reserva[i]/reservatotal2)
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
                        dif_nueva.append(reserva_nueva*reserva[i]/reservatotal2)
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
            ajuste='DATO'
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

        # 15 - Analisis de cada governor para cambiar los limites 
        reserva_cl=list()
        potencia_maxima_cl=list()
        for i,gov in enumerate(governor):
            if reserva_por[i]>parametros[0] and dif_nueva[i]>0:
                CL.cambiar_limites(governor[i], indice_ini[i], rval[i], v[i], P[i], dif_nueva[i], pmaxinueva[i],CON[i])
            else:
                print('no se cambia en ', governor[i])
        # 16 - Volver a simular el caso por las dudas
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
        # volver_a_simular()

        #guardar un nuevo snap
        nuevo_sfile = os.path.join(destino, caso.split('/')[-1].split('.')[0]+ '_reserva.snp')
        nuevo_sfile = nuevo_sfile.replace('\\', '/')
        
        psspy.snap([-1, -1, -1, -1, -1], nuevo_sfile)

        # 4 - Se vuelven a verificar los datos (revisar esto)
        nombre=list()
        cmpval=list()
        v=list()
        v1=list()
        indice_ini=list()
        rval=list()
        ierr=list()
        for i in range(0,len(bus)):
            nombre_temp, cmpval_temp,v_temp,v1_temp, indice_ini_temp,rval_temp, ierr_temp=verificaciondatos.generadores(destino, nombre_archivo, bus[i],idg[i],CON[i])
            nombre.append(nombre_temp)
            cmpval.append(cmpval_temp)
            v.append(v_temp)
            v1.append(v1_temp)
            indice_ini.append(indice_ini_temp)
            rval.append(rval_temp)
            ierr

        # 17 - Determinación de los margenes de reserva con los recortes realizados
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

        # Variables que se utilizan para el informe una vez recortado
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
        reserva_nueva=round(parametros[0]*generacion_total/100,2)
        reservatotal2=round(reservatotal2,2)

        informe.reserva_total_recorte(destino,nombre_archivo, ajuste, tipo_ajustado,reservahidro,reservatermica,reservahidro_rpf,reservatermica_rpf,
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
        print('TOTAL [MW] ',round(pot_TV+pot_TG+pot_hidro,2))
        print('-----')
        print('RESERVA PROGRAMADA EN EL PARQUE REGULANTE')
        print('HIDRO [MW] ',reservahidro_rpf)
        print('TERM. TG-CC [MW] ',reserva_TG+reserva_CC)
        print('TERM. TV [MW] ',reserva_TV)
        print('TOTAL [MW] ',reserva_TV+reserva_TG+reservahidro_rpf)
        print('RESERVA NUEVA ',round(parametros[0]*generacion_total/100,2))
        print('RESERVA TOTAL2 ',reservatotal2)
        print(destino)
        print(caso)
        print(nuevo_sfile)  
# Inicio del bucle de la ventana principal
root.mainloop()

