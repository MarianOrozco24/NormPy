import datetime

class Config:
    info_db = ["localhost", "root", "1234", "normal1"]
    ruta_salida_excek_adeudantes = "c:/Users/Usuario/OneDrive/Escritorio/"
    
    ruta_directorio_input = "C:/Users/Usuario/OneDrive/Escritorio/Workspace/Normpy/inputs"
    ruta_salida = "C:/Users/Usuario/OneDrive/Escritorio/Workspace/Normpy/Outputs"


    ''' Vamos a condicionar el archivo procesador. cosa de que cunado el mes en curso sea >= 2 and <= 4 me filtre solamente
    la columna que se llama acreditacion y cuando sea > 4 and <= 1 que me filtre la columna calificacion final'''
    fecha_actual = datetime.datetime.now()
    mes = fecha_actual.month
