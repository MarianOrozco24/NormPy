import customtkinter as ctk
import customtkinter as ctk
from tkinter import messagebox
from window.divisions.clases.clases import Filtrar, Crear, Destruir_pantalla


def tercero_primera_division():
    try:
        # Variables que almacenana informacion para la conexion con base de datos
        global datos_base, df
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = """SELECT * FROM terceraño_educacion WHERE curso = 3 and division = 1"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        VentanaTerceroPrimera = ctk.CTk()
        VentanaTerceroPrimera.title("3/1")
        screen_width = VentanaTerceroPrimera.winfo_screenwidth()
        screen_height = VentanaTerceroPrimera.winfo_screenheight()

        VentanaTerceroPrimera.geometry(f"{screen_width}x{screen_height}")

        TablaPrimero = Crear(VentanaTerceroPrimera)
        columnas_editables = ["Lengua", "matematica", "educacion_fisica", "lengua_extranjera", "geografia", "historia", "fisica", "biologia", "practicas_artisticas", "procesos_educativos", "educacion_contextos"]
        TablaPrimero.CrearTabla(df, columnas_editables, "terceraño_educacion")
        boton_volver = ctk.CTkButton(VentanaTerceroPrimera, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaTerceroPrimera, "Hola mundo"))
        boton_volver.grid(pady=20, padx=10)
    except Exception as tpd:
        messagebox.showerror("Exception", f"Excepcion en: {tpd}")
    finally:
        VentanaTerceroPrimera.mainloop()
def tercero_segunda_division():
    try:
        # Variables que almacenana informacion para la conexion con base de datos
        global datos_base, df
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = """SELECT * FROM terceraño_educacion WHERE curso = 3 and division = 2"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        VentanaTerceroSegunda = ctk.CTk()
        VentanaTerceroSegunda.title("3/2")
        screen_width = VentanaTerceroSegunda.winfo_screenwidth()
        screen_height = VentanaTerceroSegunda.winfo_screenheight()

        VentanaTerceroSegunda.geometry(f"{screen_width}x{screen_height}")

        TablaPrimero = Crear(VentanaTerceroSegunda)
        columnas_editables = ["Lengua", "matematica", "educacion_fisica", "lengua_extranjera", "geografia", "historia", "fisica", "biologia", "practicas_artisticas", "procesos_educativos", "educacion_contextos"]
        TablaPrimero.CrearTabla(df, columnas_editables, "terceraño_educacion")
        boton_volver = ctk.CTkButton(VentanaTerceroSegunda, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaTerceroSegunda, "Hola mundo"))
        boton_volver.grid(pady=20, padx=10)
    except Exception as tsd:
        messagebox.showerror("Exception", f"Excepcion en: {tsd}")
    finally:
        VentanaTerceroSegunda.mainloop()
def tercero_tercera_division():
    try:
        # Variables que almacenana informacion para la conexion con base de datos
        global datos_base, df
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = """SELECT * FROM terceraño_cn WHERE curso = 3 and division = 3"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        VentanaTerceroTercera = ctk.CTk()
        VentanaTerceroTercera.title("3/3")
        screen_width = VentanaTerceroTercera.winfo_screenwidth()
        screen_height = VentanaTerceroTercera.winfo_screenheight()

        VentanaTerceroTercera.geometry(f"{screen_width}x{screen_height}")

        TablaPrimero = Crear(VentanaTerceroTercera)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "geografia", "historia", "fisica", "biologia", "quimica", "practicas_artisicas", "integral_adolecencia"]
        TablaPrimero.CrearTabla(df, columnas_editables,"terceraño_cn")
        boton_volver = ctk.CTkButton(VentanaTerceroTercera, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaTerceroTercera, "Hola mundo"))
        boton_volver.grid(pady=20, padx=10)
    except Exception as ttd:
        messagebox.showerror("Exception", f"Excepcion en {ttd}")
    finally:
        VentanaTerceroTercera.mainloop()
def tercero_cuarta_division():
    try:    # Variables que almacenana informacion para la conexion con base de datos
        global datos_base, df
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = """SELECT * FROM terceraño_cn WHERE curso = 3 and division = 4"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        VentanaTerceroCuarta = ctk.CTk()
        VentanaTerceroCuarta.title("3/4")
        screen_width = VentanaTerceroCuarta.winfo_screenwidth()
        screen_height = VentanaTerceroCuarta.winfo_screenheight()

        VentanaTerceroCuarta.geometry(f"{screen_width}x{screen_height}")

        TablaPrimero = Crear(VentanaTerceroCuarta)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "geografia", "historia", "fisica", "biologia", "quimica", "practicas_artisicas", "integral_adolecencia"]
        TablaPrimero.CrearTabla(df, columnas_editables,"terceraño_cn")
        boton_volver = ctk.CTkButton(VentanaTerceroCuarta, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaTerceroCuarta, "Hola mundo"))
        boton_volver.grid(pady=20, padx=10)
    except Exception as tcd:
        messagebox.showerror("Exception", f"Excepcion en {tcd}")
    finally:
        VentanaTerceroCuarta.mainloop()
def tercero_quinta_division():
    # Variables que almacenana informacion para la conexion con base de datos
    try:
        global datos_base, df
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = """SELECT * FROM terceraño_cn WHERE curso = 3 and division = 5"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        VentanaTerceroQuinta = ctk.CTk()
        VentanaTerceroQuinta.title("3/5")
        screen_width = VentanaTerceroQuinta.winfo_screenwidth()
        screen_height = VentanaTerceroQuinta.winfo_screenheight()

        VentanaTerceroQuinta.geometry(f"{screen_width}x{screen_height}")

        TablaPrimero = Crear(VentanaTerceroQuinta)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "geografia", "historia", "fisica", "biologia", "quimica", "practicas_artisicas", "integral_adolecencia"]
        TablaPrimero.CrearTabla(df, columnas_editables,"terceraño_cn")
        boton_volver = ctk.CTkButton(VentanaTerceroQuinta, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaTerceroQuinta, "Hola mundo"))
        boton_volver.grid(pady=20, padx=10)
    except Exception as tqd:
        messagebox.showerror("Exception", f"Excepcion: {tqd}")
    finally:
        VentanaTerceroQuinta.mainloop()