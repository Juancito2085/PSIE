import csv

def lectura(file):
    '''
    Lee los datos de los generadores.
    Recibe como entrada un string que es el nombre del archivo
    Devuelve listas de los datos en el siguiente orden
    bus
    governor
    CON
    porcentaje
    idg
    comentario
    '''

    bloque=0
    bloque_1=list()
    bloque_2=list()
    bloque_3=list()

    #Listas correspondientes al Bloque 1
    bus=list()
    governor=list()
    CON=list()
    porcentaje=list()
    idg=list()
    comentario=list()
    tipo=list()

    #Listas correspondientes al Bloque 2
    narea=list()
    nombre_area=list()

    #Listas correspondientes al Bloque 3
    bus_sale=list()
    nombre_sale=list()
    id_sale=list()

    with open(file,encoding='UTF-8') as archivo:
        informacion=csv.reader(archivo,delimiter=";",)
        for linea in informacion:
            if linea[0]=="1º BLOQUE":
                bloque=1 
                next(informacion) 
            if linea[0]=="2º BLOQUE":
                bloque=2
                next(informacion)
            if linea[0]=="3º BLOQUE":
                bloque=3   
                next(informacion) 
            #Dependiendo el bloque en el que este guarda los 3 bloques en diferentes registros
            if bloque==1 and linea[0]!="1º BLOQUE":
                bus.append(int(linea[0]))
                governor.append(linea[1])
                CON.append(int(linea[2]))
                porcentaje.append(float(linea[3]))
                idg.append(linea[4])
                comentario.append(linea[5])

            if bloque==2 and linea[0]!="2º BLOQUE":
                narea.append(linea[0])
                nombre_area.append(linea[1])

            if bloque==1 and linea[0]!="3º BLOQUE":
                bus_sale.append(linea[0])
                nombre_sale.append(linea[1])
                id_sale.append(linea[2])
    return(bus,governor,CON,porcentaje,idg,comentario)