import customtkinter as ctk
import customtkinter as ctk
from tkinter import messagebox
from window.divisions.clases.clases import Filtrar, Crear, Destruir_pantalla

def quinto_primera_division():
    # Variables que almacenana informacion para la conexion con base de datos
    try:
        global datos_base, df
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = """SELECT * FROM quintoaño_educacion WHERE curso = 5 and division = 1"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        VentanaQuintoPrimera = ctk.CTk()
        VentanaQuintoPrimera.title("5/1")
        screen_width = VentanaQuintoPrimera.winfo_screenwidth()
        screen_height = VentanaQuintoPrimera.winfo_screenheight()

        VentanaQuintoPrimera.geometry(f"{screen_width}x{screen_height}")

        TablaPrimero = Crear(VentanaQuintoPrimera)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "formacion_vida", "formacion_etica", "economia_social", "comunicacion", "filosofia", "perspectivas_pedagogicas", "problemas_educativos", "proyecto_socioeducativo"]
        TablaPrimero.CrearTabla(df, columnas_editables, "quintoaño_educacion")
        boton_volver = ctk.CTkButton(VentanaQuintoPrimera, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaQuintoPrimera, "Hola mundo"))
        boton_volver.grid(pady=20, padx=10)
    except Exception as qpd:
        messagebox.showerror("Exception", f"Exception: {qpd}")
    finally:
        VentanaQuintoPrimera.mainloop()
def quinto_segunda_division():
    # Variables que almacenana informacion para la conexion con base de datos
    try:
        global datos_base, df
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = """SELECT * FROM quintoaño_educacion WHERE curso = 5 and division = 2"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        VentanaQuintoSegunda = ctk.CTk()
        VentanaQuintoSegunda.title("5/2")
        screen_width = VentanaQuintoSegunda.winfo_screenwidth()
        screen_height = VentanaQuintoSegunda.winfo_screenheight()

        VentanaQuintoSegunda.geometry(f"{screen_width}x{screen_height}")

        TablaPrimero = Crear(VentanaQuintoSegunda)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "formacion_vida", "formacion_etica", "economia_social", "comunicacion", "filosofia", "perspectivas_pedagogicas", "problemas_educativos", "proyecto_socioeducativo"]    
        TablaPrimero.CrearTabla(df, columnas_editables, "quintoaño_educacion")
        boton_volver = ctk.CTkButton(VentanaQuintoSegunda, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaQuintoSegunda, "Hola mundo"))
        boton_volver.grid(pady=20, padx=10)
    except Exception as qsd:
        messagebox.showerror("Exception", f"Exception qsd: {qsd}")
    finally: 
        VentanaQuintoSegunda.mainloop()    
def quinto_tercera_division():
    # Variables que almacenana informacion para la conexion con base de datos
    try:
        global datos_base, df
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = """SELECT * FROM quintoaño_cn WHERE curso = 5 and division = 3"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        VentanaQuintoTercera = ctk.CTk()
        VentanaQuintoTercera.title("5/3")
        screen_width = VentanaQuintoTercera.winfo_screenwidth()
        screen_height = VentanaQuintoTercera.winfo_screenheight()

        VentanaQuintoTercera.geometry(f"{screen_width}x{screen_height}")

        TablaPrimero = Crear(VentanaQuintoTercera)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "formacion_vida", "formacion_etica", "economia_social", "comunicacion","proyecto_intervencion",  "filosofia", "salud_sociedad", "problematicas_socioambientales", "ciencias_tierra"]    
        TablaPrimero.CrearTabla(df, columnas_editables, "quintoaño_cn")
        boton_volver = ctk.CTkButton(VentanaQuintoTercera, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaQuintoTercera, "Hola mundo"))
        boton_volver.grid(pady=20, padx=10)
    except Exception as qtd:
        messagebox.showerror("Exception", f"Exception qtd: {qtd}")
    finally:
        VentanaQuintoTercera.mainloop()
def quinto_cuarta_division():
    # Variables que almacenana informacion para la conexion con base de datos
    try:
        global datos_base, df
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = """SELECT * FROM quintoaño_cn WHERE curso = 5 and division = 4"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        VentanaQuintoCuarta = ctk.CTk()
        VentanaQuintoCuarta.title("5/4")
        screen_width = VentanaQuintoCuarta.winfo_screenwidth()
        screen_height = VentanaQuintoCuarta.winfo_screenheight()

        VentanaQuintoCuarta.geometry(f"{screen_width}x{screen_height}")

        TablaPrimero = Crear(VentanaQuintoCuarta)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "formacion_vida", "formacion_etica", "economia_social", "comunicacion", "filosofia", "salud_sociedad", "problematicas_socioambientales", "ciencias_tierra"]    
        TablaPrimero.CrearTabla(df, columnas_editables, "quintoaño_cn")
        boton_volver = ctk.CTkButton(VentanaQuintoCuarta, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaQuintoCuarta, "Hola mundo"))
        boton_volver.grid(pady=20, padx=10)
    except Exception as qcd:
        messagebox.showerror("Exception," f"Exception qcd: {qcd}")
    finally:
        VentanaQuintoCuarta.mainloop()
def quinto_quinta_division():
    # Variables que almacenana informacion para la conexion con base de datos
    try:
        global datos_base, df
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = """SELECT * FROM quintoaño_cn WHERE curso = 5 and division = 5"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        VentanaQuintoQuinta = ctk.CTk()
        VentanaQuintoQuinta.title("5/5")
        screen_width = VentanaQuintoQuinta.winfo_screenwidth()
        screen_height = VentanaQuintoQuinta.winfo_screenheight()

        VentanaQuintoQuinta.geometry(f"{screen_width}x{screen_height}")

        TablaPrimero = Crear(VentanaQuintoQuinta)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "formacion_vida", "formacion_etica", "economia_social", "comunicacion", "filosofia", "salud_sociedad", "problematicas_socioambientales", "ciencias_tierra"]    
        TablaPrimero.CrearTabla(df, columnas_editables, "quintoaño_cn")
        boton_volver = ctk.CTkButton(VentanaQuintoQuinta, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaQuintoQuinta, "Hola mundo"))
        boton_volver.grid(pady=20, padx=10)
    except Exception as qqd:
        messagebox.showerror("Exception",f"Exception qqd: {qqd}")
    finally:
        VentanaQuintoQuinta.mainloop()
