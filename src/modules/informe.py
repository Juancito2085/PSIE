import openpyxl
import os

def crear (ruta):
    """Crea el archivo excel de salida para los reportes en la ruta especificada
    :param ruta: ruta donde se guardará el archivo excel"""
    # Creamos el excel en la ruta especificada por el parametro
    wb = openpyxl.Workbook()
    # Eliminamos la hoja por defecto
    wb.remove(wb.active)
    # Creamos las hojas del excel
    wb.create_sheet('reserva_total.prn')
    wb.create_sheet('Pmax_Pgen.prn')
    wb.create_sheet('Mayor_maxima.prn')
    wb.create_sheet('Menor_optima.prn')
    wb.create_sheet('Reserva.rep')
    wb.create_sheet('Reserva.err')
    # Creamos los enacabezados de las hojas
    wb['reserva_total.prn'].append(['Escenario','Reserva Hidro','Reserva Termica','Reserva Total'])#1
    wb['Pmax_Pgen.prn'].append(['IBUS','NOMBRE','ID','POT_MAX[MW]','POT_GEN[MW]','MAX_GEN[MW]','RESERVA_DATO[%]','PORCENTAJE[%]','RES_OPT[%]'])
    wb['Mayor_maxima.prn'].append(['IBUS','NOMBRE','ID','POT_MAX[MW]','POT_GEN[MW]','MAX_GEN[MW]','RESERVA_DATO[%]','PORCENTAJE[%]','RESOPT[%]'])
    wb['Menor_optima.prn'].append(['IBUS','NOMBRE','ID','POT_MAX[MW]','POT_GEN[MW]','MAX_GEN[MW]','RESERVA_DATO[%]','PORCENTAJE[%]','RESOPT[%]'])
    wb['Reserva.rep'].append(['Escenario','Reserva Hidro','Reserva Termica','Reserva Total'])#2
    wb['Reserva.err'].append(['Error'])#3
    # Guardamos el excel con el nombre Reserva_salida.xlsx
    ruta_completa= ruta+'/Reserva_salida1.xlsx'
    wb.save(ruta_completa)
    # Mensaje que avisa que el archivo se ha creado en la ruta especificada
    print('Archivo creado en la ruta: ',ruta_completa)
    return

def reserva_total(ruta):
    """Completa los datos de la hoja reserva_total.prn
    :param ruta: ruta donde se encuentra el archivo excel de entrada"""
    #Abrimos el archivo de excel
    workbook = openpyxl.load_workbook(ruta)
    #Seleccionamos la hoja donde vamos a completar con datos
    sheet = workbook['reserva_total.prn']
    #Escribimos los datos en la hoja debajo de los encabezados en la fila 2

    return

def Pmax_Pgen(ruta,ibus,nombre,id,pot_max,pot_gen,max_gen,reserva,por_dato,resopt):
    """Completa los datos de la hoja Pmax_Pgen.prn
    :param ruta: ruta donde se encuentra el archivo excel de entrada"""
    #Verificamos que se pueda abrir el excel
    try:
        workbook = openpyxl.load_workbook(ruta+'/Reserva_salida1.xlsx')
    except:
        print('No se pudo abrir el archivo')
        return
    #Seleccionamos la hoja donde vamos a completar con datos
    sheet = workbook['Pmax_Pgen.prn']
    # Escribimos todos los datos de las listas
    for i in range(len(ibus)):
        row=i+2
        sheet.cell(row=row, column=1).value = ibus[i]
        sheet.cell(row=row, column=2).value = nombre[i]
        sheet.cell(row=row, column=3).value = id[i]
        sheet.cell(row=row, column=4).value = pot_max[i]
        sheet.cell(row=row, column=5).value = pot_gen[i]
        sheet.cell(row=row, column=6).value = max_gen[i]
        sheet.cell(row=row, column=7).value = reserva[i]
        sheet.cell(row=row, column=8).value = por_dato[i]
        sheet.cell(row=row, column=9).value = resopt

    

    # Guardamos el archivo de excel
    workbook.save(ruta + '/Reserva_salida1.xlsx')
    workbook.close()
    return

def Mayor_maxima(ruta,ibus,nombre,id,pot_max,pot_gen,max_gen,reserva,por_dato,resopt):
    """Completa los datos de la hoja Mayor_maxima.prn
    :param ruta: ruta donde se encuentra el archivo excel de entrada"""
    #Abrimos el archivo de excel
    try:
        workbook = openpyxl.load_workbook(ruta+'/Reserva_salida1.xlsx')
    except:
        print('No se pudo abrir el archivo')
        return
    #Seleccionamos la hoja donde vamos a completar con datos
    sheet = workbook['Mayor_maxima.prn']
    # Escribimos todos los datos de las listas donde los generadores tenga una reserva mayor a la maxima
    j=0
    for i in range(len(ibus)):
        if reserva[i]>resopt:
            row=j+2
            sheet.cell(row=row, column=1).value = ibus[i]
            sheet.cell(row=row, column=2).value = nombre[i]
            sheet.cell(row=row, column=3).value = id[i]
            sheet.cell(row=row, column=4).value = pot_max[i]
            sheet.cell(row=row, column=5).value = pot_gen[i]
            sheet.cell(row=row, column=6).value = max_gen[i]
            sheet.cell(row=row, column=7).value = reserva[i]
            sheet.cell(row=row, column=8).value = por_dato[i]
            sheet.cell(row=row, column=9).value = resopt
            j+=1

    # Guardamos el archivo de excel
    workbook.save(ruta + '/Reserva_salida1.xlsx')
    workbook.close()
    return

def Menor_optima(ruta,ibus,nombre,id,pot_max,pot_gen,max_gen,reserva,por_dato,resopt):
    """Completa los datos de la hoja Menor_optima.prn
    :param ruta: ruta donde se encuentra el archivo excel de entrada"""
    #Abrimos el archivo de excel
    try:
        workbook = openpyxl.load_workbook(ruta+'/Reserva_salida1.xlsx')
    except:
        print('No se pudo abrir el archivo')
        return
    #Seleccionamos la hoja donde vamos a completar con datos
    sheet = workbook['Menor_optima.prn']
    # Escribimos todos los datos de las listas donde los generadores tenga una reserva mayor a la maxima
    j=0
    for i in range(len(ibus)):
        if reserva[i]<resopt:
            row=j+2
            sheet.cell(row=row, column=1).value = ibus[i]
            sheet.cell(row=row, column=2).value = nombre[i]
            sheet.cell(row=row, column=3).value = id[i]
            sheet.cell(row=row, column=4).value = pot_max[i]
            sheet.cell(row=row, column=5).value = pot_gen[i]
            sheet.cell(row=row, column=6).value = max_gen[i]
            sheet.cell(row=row, column=7).value = reserva[i]
            sheet.cell(row=row, column=8).value = por_dato[i]
            sheet.cell(row=row, column=9).value = resopt
            j+=1

    # Guardamos el archivo de excel
    workbook.save(ruta + '/Reserva_salida1.xlsx')
    workbook.close()
    return

def Reserva_rep(ruta):
    """Completa los datos de la hoja Reserva.rep
    :param ruta: ruta donde se encuentra el archivo excel de entrada"""
    #Abrimos el archivo de excel
    workbook = openpyxl.load_workbook(ruta)
    #Seleccionamos la hoja donde vamos a completar con datos
    sheet = workbook['Reserva.rep']
    #Escribimos los datos en la hoja debajo de los encabezados en la fila 2

    return

def Reserva_err(ruta, error):
    """Completa los datos de la hoja Reserva.err
    :param ruta: ruta donde se encuentra el archivo excel de entrada"""
    #Abrimos el archivo de excel
    workbook = openpyxl.load_workbook(ruta +'/Reserva_salida1.xlsx')
    #Seleccionamos la hoja donde vamos a completar con datos
    sheet = workbook['Reserva.err']
    #Escribimos los datos en la primera celda en blanco
    last_row = sheet.max_row + 1
    sheet.cell(row=last_row, column=1, value=error)
    workbook.save(ruta+'/Reserva_salida1.xlsx')
    workbook.close()

    return

