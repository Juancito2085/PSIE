import psspy
import modules.informe as informe



def total(destino, nombre_archivo):
    '''
    Función que calcula la generación total del sistema.

    :param destino: Ruta donde se guardará el archivo de salida.
    :param nombre_archivo: Nombre del archivo de salida.
    '''
    ruta=destino + nombre_archivo
    ierr, cmpval = psspy.systot('GEN')

    if(ierr)==2:
        error='***** ERROR EN EL SISTEMA ***** NO SE ENCUENTRAN BARRAS EN EL CASO EN ESTUDIO'
        informe.Reserva_err(ruta,error)

    if(ierr)==1:
        error='***** ERROR EN LOS DATOS DE reserva_DEMANDAS ***** ERROR EN EL STRING '
        informe.Reserva_err(ruta,error)

    p=cmpval.real
    q=cmpval.imag
 
    return(p,q)
