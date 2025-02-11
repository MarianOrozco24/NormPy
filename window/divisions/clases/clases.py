import customtkinter as ctk
import pandas as pd
import pymysql
from tkinter import messagebox
from config import Config


class Filtrar:
    def __init__(self, datos_base):
        self.conn = None
        self.cursor= None
        self.datos_base = datos_base
        self.df = None

    
    def extraer_datos (self, consulta):
        try:
            # Iniciamos la conexion con base de datos y la extraemos a un DataFrame
            self.conn = pymysql.connect(host=self.datos_base[0], user=self.datos_base[1], password=self.datos_base[2], database=self.datos_base[3])
            self.df = pd.read_sql_query(consulta, self.conn)
        except Exception as Filtrado_database:
            print(f"Ocurrio una excepcion en el filtrado de datos: {Filtrado_database}")
            exit(0)
        finally:
            # Cerramos conexion con base de datos y extraemos df
            if self.conn is not None:
                self.conn.close()
            return self.df
    def Guardar_cambios(self, df, row, col, entrada, curso):
        try:
            # Iniciamos la conexion con base de datos
            self.conn = pymysql.connect(host=self.datos_base[0], user=self.datos_base[1], password=self.datos_base[2], database=self.datos_base[3])
            self.cursor = self.conn.cursor()

            # Extraemos el valor modificado
            nuevo_valor = entrada.get()    
            df.iloc[row, col] = nuevo_valor
            print(f"El nuevo valor de la fila: {row} y la columna {col}, es: {nuevo_valor}")

            # Actualizamos la base de datos con el nuevo valor
            columna_nombre_xxx = df.columns[col]
            id_alumno = df.iloc[row, 13]
            consulta_actualizar = f"""UPDATE {curso} SET {columna_nombre_xxx} = %s WHERE id_alumnos = %s """
            self.cursor.execute(consulta_actualizar, (nuevo_valor, id_alumno))
            self.conn.commit()
        except Exception as exc:
            print(f"Ocurrio un error al guardar los cambios {exc}")
            messagebox.showerror("Conexion base de datos", f"Error en la conexion a base de datos\n {exc}")
            exit(1)
        finally:
            self.conn.close()
class Crear:
    def __init__(self, ventana):
        # Inicialización de variables
        self.ventana = ventana
        self.encabezdos = None
        self.contenedor = ctk.CTkFrame(self.ventana)
        self.canvas = ctk.CTkCanvas(self.contenedor)
        self.canvas_frame = ctk.CTkFrame(self.canvas)
        
        # Crear los scrollbars
        self.scrollbar_vertical = ctk.CTkScrollbar(self.contenedor, orientation="vertical", command=self.canvas.yview)
        self.scrollbar_horizontal = ctk.CTkScrollbar(self.contenedor, orientation="horizontal", command=self.canvas.xview)
        
        # Configuración del canvas
        self.canvas.configure(yscrollcommand=self.scrollbar_vertical.set, xscrollcommand=self.scrollbar_horizontal.set)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar_vertical.grid(row=0, column=1, sticky="ns")
        self.scrollbar_horizontal.grid(row=1, column=0, sticky="ew")

        # Configurar el contenedor para que ajuste el tamaño del canvas
        self.contenedor.grid_rowconfigure(0, weight=1)
        self.contenedor.grid_columnconfigure(0, weight=1)
        self.contenedor.grid(row=0, column=0, sticky="nsew")
        
        # Agregar el canvas_frame al canvas
        self.canvas.create_window((0, 0), window=self.canvas_frame, anchor="nw")
          
    def CrearTabla(self, df, columnas_editables, curso):
        datos_base = Config.info_db
        entradas_editables = []
        encabezados = list(df.columns)
        # Ultima_col = df.columns[len(df.columns) - 1]

        # Ajustar el tamaño de la fuente
        font = ("Arial", 10)

        # Crear encabezados
        for col, header in enumerate(encabezados):
            encabezados_label = ctk.CTkLabel(self.canvas_frame, text=header, font=("Arial", 14))
            encabezados_label.grid(row=0, column=col, pady=2, padx=5, sticky="nsew")

        # Crear filas de datos
        for row in df.index:
            for col in range(len(encabezados)):
                valor = df.iloc[row, col]
                if encabezados[col] in columnas_editables:

                    # Crear un campo editable
                    entrada = ctk.CTkEntry(self.canvas_frame, font=font)
                    entrada.insert("end", str(valor))
                    entrada.grid(row=row+1, column=col, padx=5, pady=5, sticky="nsew")
                    entradas_editables.append((entrada, (row, col)))
                    guardar = Filtrar(datos_base)
                    entrada.bind("<FocusOut>", lambda e, r=row, c=col, widget=entrada: guardar.Guardar_cambios(df, r, c, widget, curso))
                else:

                    # Crear una etiqueta inmodificable
                    label = ctk.CTkLabel(self.canvas_frame, text=valor, font=font)
                    label.grid(row=row+1, column=col, padx=5, pady=5, sticky="nsew")

        # Hacer que las columnas se expandan proporcionalmente
        for col in range(len(encabezados)):
            self.canvas_frame.grid_columnconfigure(col, weight=1)

        # Actualizar el canvas y su región de scroll
        self.canvas_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        # Ajustar el tamaño del canvas para que se ajuste al contenido
        self.canvas_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        # Hacer que el contenedor, canvas y tabla se redimensionen con la ventana
        self.ventana.grid_rowconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(0, weight=1)
        self.contenedor.grid_rowconfigure(0, weight=1)
        self.contenedor.grid_columnconfigure(0, weight=1)

   
class Adeudantes:
    def __init__(self, datos_base, consulta):
        self.conn = None
        self.cursor=None
        self.datos_base = datos_base
        self.consulta = consulta
    def DataExtract_adeudantes (self):
        try: 
            self.conn  = pymysql.connect(host=self.datos_base[0], user=self.datos_base[1], password=self.datos_base[2], database=self.datos_base[3])
            self.cursor = self.conn.cursor()
            self.cursor.execute(self.consulta)
            Resultado_adeudantes = self.cursor.fetchone()
        except Exception as DEA:
            messagebox.showerror("Exception",f"Exception DEA: {DEA}")
        finally:
            if self.cursor is not None:
                self.cursor.close()
            if self.conn is not None:
                self.conn.close()    
            return Resultado_adeudantes
    def DataExtract_database(self):
        try:
            # Establecemos conexion con la base de datos 
            self.conn = pymysql.connect(host=self.datos_base[0], user=self.datos_base[1], password=self.datos_base[2], database=self.datos_base[3])
            self.cursor = self.conn.cursor()
            Resultado = pd.read_sql_query(self.consulta, self.conn)             
            # Extraemos el resultado de la consulta 
            
        except Exception as DE:

            # imprimimos el mensaje de error
            print(f"Excepcion en extraer datos - {DE}")
            messagebox.showerror("Exception",f"Excepcion en extraer datos - {DE}")
        finally:
            # Cerramos la conexion con base de datos y extraemos el resultado
            if self.cursor is not None:
                self.cursor.close()
            if self.conn is not None:
                self.conn.close()
                return Resultado
    def Analisis_datos(self,df_resultado, scroll_frame_recursantes, scroll_frame_adeudantes ):
        global VentanaPrincipal
        # Cerramos la ventana principal
        if VentanaPrincipal is not None:
            VentanaPrincipal.destroy()
            VentanaPrincipal = None
        # Creamos la variable cantidad_col para manipular con mayor facildad el num de columnas
        cantidad_col = len(df_resultado.columns) - 1

        # Creacion de dataframe vacio y variables necesarias para la extraccion del df
        df_vacio = pd.DataFrame()
        contador_nombres_condicional = 0

          # Creacion de columnas para guardar en df_vacio
        df_vacio['Año'] = ''
        df_vacio['Nombre y apellido'] = ''
        df_vacio['Division'] = ''
        df_vacio['materia0'] = ''
        df_vacio['materia1'] = ''
        df_vacio['materia2'] = ''
        df_vacio['materia3'] = ''
        df_vacio['materia4'] = ''
        df_vacio['materia5'] = ''
        df_vacio['materia6'] = ''
        df_vacio['materia7'] = ''
        df_vacio['materia8'] = ''
        df_vacio['materia9'] = ''
        df_vacio['materia10'] = ''
        df_vacio['materia11'] = ''

        # Ciclo for que nos permite recorrer el Df_resultado y obtener los valores de las filas
        for c in range(0,len(df_resultado.index)):
            datos = df_resultado.iloc[c]
            contador = 0
            materias = []

            # Ciclo for que nos permite recorres las columnas y asi compararlas
            for i in range(5, len(df_resultado.columns) - 1):
                datos2 = datos[i]

                # Condicion para filtrar datos obtenidos 
                if  datos2 >= 1 and datos2 < 7:
                    contador = contador + 1
                    obtener_id = datos[cantidad_col]
                    materias.append(df_resultado.columns[i])

                    
                    
            if contador != 0:
                # Creamos un contador para indicar en que fila tiene que colocarse el nombre
                # y los datos del alumnos en el df_vacio
                contador_nombres_condicional = contador_nombres_condicional + 1

                # Obtenemos los datos del alumno basandonos en el id que obtuvimos anteiormente
                consulta = f'SELECT nombre_completo FROM alumnos WHERE id_alumnos = {obtener_id}'
                consulta_año = f'SELECT año_en_curso FROM primeraño WHERE id_alumnos = {obtener_id}'
                consulta_division = f'SELECT division FROM primeraño WHERE id_alumnos = {obtener_id}'
                extraer_nombre = Adeudantes(self.datos_base, consulta)
                Nombre_extraido = extraer_nombre.DataExtract_adeudantes() 
                extraer_año_curso = Adeudantes(self.datos_base, consulta_año)
                año_extraido = extraer_año_curso.DataExtract_adeudantes()
                extraer_division= Adeudantes(self.datos_base, consulta_division)
                division_extraida = extraer_division.DataExtract_adeudantes()
                division = division_extraida[0]
                Año = año_extraido[0]
                Nombre = Nombre_extraido[0]
                ##########################
                # Cargamos los datos al df
                df_vacio.loc[contador_nombres_condicional, 'Nombre y apellido'] = Nombre
                df_vacio.loc[df_vacio['Nombre y apellido'] == Nombre, 'Año'] = Año
                df_vacio.loc[df_vacio['Nombre y apellido'] == Nombre, 'Division'] = division
                for d in range(len(materias)):
                    df_vacio.loc[df_vacio['Nombre y apellido'] == Nombre, f'materia{d}'] = materias [d]
                ###################################
                
                if contador >=3:
                    label= ctk.CTkLabel(scroll_frame_recursantes, text =f"{Año} | {Nombre} Adeuda: {contador} materias ---> {materias}", anchor = "w", font=("Helvetica", 14))
                    label.pack(pady=5, padx=5, fill = "both")
                else:
                    label = ctk.CTkLabel(scroll_frame_adeudantes, text =f"{Año} | {Nombre} adeuda: {contador} materias ---> {materias}", anchor="w", font=("Helvetica", 14))
                    label.pack(pady=5, padx=5, fill="both")
                
            else:
                continue
            
      
        
        return df_vacio
class VerAdeudantes:
    def __init__(self):
        # Cerramos las ventana anteriores


        # Inicializamos las variables necesarias
        self._titulo_label = None
        self._titulo_ventana = None
        self.ventana_adeudantes = None
        self.frame_titulo = None
        self.scroll_frame_adeudantes = None
        self.scroll_frame_recursantes = None
    def destruir_anterior(self, ventana_anterior):
        if ventana_anterior is not None:
            ventana_anterior.destroy()
            ventana_anterior=None

    # Con esta funcion cargamos el nombre de la ventana
    def set_cargar_titulo_ventana (self, titulo_ventana):
        self._titulo_ventana = titulo_ventana

    # Con esta funcion cargamos el titulo de la ventana
    def set_cargar_titulo_label(self,titulo_label ):
        self._titulo_label = titulo_label

    # Creamos la ventana con el nombre creado anteriormente
    def configuracion_ventana(self):
        self.ventana_adeudantes = ctk.CTk()
        self.ventana_adeudantes.title(self._titulo_ventana)
        self.ventana_adeudantes.geometry("600x600")

    # Se crean los labels
    def configuracion_carga_label (self):
        # Creacion de frames para alojar datos
        self.frame_titulo = ctk.CTkFrame(self.ventana_adeudantes)
        self.frame_titulo.pack(pady=5,padx=5, fill="both")
        self. scroll_frame_adeudantes =  ctk.CTkScrollableFrame(self.ventana_adeudantes)
        self.scroll_frame_adeudantes.pack(pady=2, padx=2, fill="both", expand=True)
        self.scroll_frame_recursantes = ctk.CTkScrollableFrame(self.ventana_adeudantes)
        self.scroll_frame_recursantes.pack(pady=2, padx=2, fill="both", expand=True)
        frame_volver =ctk.CTkFrame(self.ventana_adeudantes)
        frame_volver.pack(pady=2, padx=2, fill ="both")
        # Creacion de titulo
        title = ctk.CTkLabel(self.frame_titulo, text= self._titulo_label, font=("Helvetica", 20, "bold"))
        title.pack(pady=5, padx=5)

        # Creacion de subtitulos 
        subtitle = ctk.CTkLabel(self.scroll_frame_adeudantes, text="Adeudantes", font=("Helvetica", 15,"bold"))
        subtitle.pack(pady=5, padx=5)
        subtitle = ctk.CTkLabel(self.scroll_frame_recursantes, text= "Recursantes", font=("Helvetica", 15, "bold"))
        subtitle.pack(pady=5, padx=5) 

        

    def mostrar_datos(self,datos_base, consulta):
        # Funciones que realizan la extraccion y hacen las comparaciones necesarias
        adeudantes_primer_año = Adeudantes(datos_base, consulta)
        df_resultado = adeudantes_primer_año.DataExtract_database()
        self.df_vacio = adeudantes_primer_año.Analisis_datos(df_resultado, self.scroll_frame_adeudantes, self.scroll_frame_recursantes)
        
        #Ejecutamos la funcion ventana
        self.ventana_adeudantes.mainloop()   
    
def extraer_lista_datos(database, consulta):
    conn = pymysql.connect(host = database[0], user = database[1],password= database[2],database= database[3])
    cursor = conn.cursor()
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    # Cerramos la conexion con base de datos
    conn.close()
    return resultado
    


def Destruir_pantalla (fuction,fuction_abrir):
    if fuction is not None:
        fuction.destroy()
        # fuction = None
    if fuction_abrir is str:
        print("Ventana cerrada")
    else:
        fuction_abrir()
        