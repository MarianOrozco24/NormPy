import customtkinter as ctk
import pandas as pd
from tkinter import messagebox
from window.clases.clases import Filtrar, Crear, Destruir_pantalla
from config import Config

datos_base = Config.info_db


def segundo_primera_division():
    try:    
        global datos_base, df
        consulta = """SELECT * FROM segundo_año WHERE curso = 2 and division = 1"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        VentanaSegundoPrimera = ctk.CTk()
        VentanaSegundoPrimera.title("1/1")
        screen_width = VentanaSegundoPrimera.winfo_screenwidth()
        screen_height = VentanaSegundoPrimera.winfo_screenheight()

        VentanaSegundoPrimera.geometry(f"{screen_width}x{screen_height}")

        TablaPrimero = Crear(VentanaSegundoPrimera)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "educacion_tecnologica", "historia", "ciencias_naturales", "teatro", "comunicacion_social"]
        TablaPrimero.CrearTabla(df, columnas_editables,"segundo_año")
        frmae_button = ctk.CTkFrame(VentanaSegundoPrimera, fg_color="#6A0DAD")
        frmae_button.grid(pady=15, padx=5)
        boton_volver = ctk.CTkButton(frmae_button, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaSegundoPrimera, "Hola mundo"))
        boton_volver.grid(pady=2, padx=2)
    except Exception as spd:
        messagebox.showerror("Exception", f"Exception: {spd}")
    finally:
        VentanaSegundoPrimera.mainloop()
def segundo_segunda_division():
    try:
        global datos_base, df
        consulta = """SELECT * FROM segundo_año WHERE curso = 2 and division = 2"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        VentanaSegundoSegunda = ctk.CTk()
        VentanaSegundoSegunda.title("1/1")
        screen_width = VentanaSegundoSegunda.winfo_screenwidth()
        screen_height = VentanaSegundoSegunda.winfo_screenheight()

        VentanaSegundoSegunda.geometry(f"{screen_width}x{screen_height}")

        TablaPrimero = Crear(VentanaSegundoSegunda)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "educacion_tecnologica", "historia", "ciencias_naturales", "teatro", "comunicacion_social"]
        TablaPrimero.CrearTabla(df, columnas_editables,"segundo_año")
        frmae_button = ctk.CTkFrame(VentanaSegundoSegunda, fg_color="#6A0DAD")
        frmae_button.grid(pady=15, padx=5)
        boton_volver = ctk.CTkButton(frmae_button, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaSegundoSegunda, "Hola mundo"))
        boton_volver.grid(pady=2, padx=2)
    except Exception as ssd:
        messagebox.showerror("Exception", f"Exception: {ssd}")
    finally:
        VentanaSegundoSegunda.mainloop()
def segundo_tercera_division():
    try:
        global datos_base, df
        consulta = """SELECT * FROM segundo_año WHERE curso = 2 and division = 3"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        VentanaSegundoTercera = ctk.CTk()
        VentanaSegundoTercera.title("1/1")
        screen_width = VentanaSegundoTercera.winfo_screenwidth()
        screen_height = VentanaSegundoTercera.winfo_screenheight()

        VentanaSegundoTercera.geometry(f"{screen_width}x{screen_height}")

        TablaPrimero = Crear(VentanaSegundoTercera)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "educacion_tecnologica", "historia", "ciencias_naturales", "teatro", "comunicacion_social"]
        TablaPrimero.CrearTabla(df, columnas_editables,"segundo_año")
        frmae_button = ctk.CTkFrame(VentanaSegundoTercera, fg_color="#6A0DAD")
        frmae_button.grid(pady=15, padx=5)
        boton_volver = ctk.CTkButton(frmae_button, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaSegundoTercera, "Hola mundo"))
        boton_volver.grid(pady=2, padx=2)
    except Exception as std:
        messagebox.showerror("Exception", f"Exception: {std}")
    finally:
        VentanaSegundoTercera.mainloop()
def segundo_cuarta_division():
    try:
        # Variables que almacenana informacion para la conexion con base de datos
        global datos_base, df
        consulta = """SELECT * FROM segundo_año WHERE curso = 2 and division = 4"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        VentanaSegundoCuarta = ctk.CTk()
        VentanaSegundoCuarta.title("1/1")
        screen_width = VentanaSegundoCuarta.winfo_screenwidth()
        screen_height = VentanaSegundoCuarta.winfo_screenheight()

        VentanaSegundoCuarta.geometry(f"{screen_width}x{screen_height}")

        TablaPrimero = Crear(VentanaSegundoCuarta)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "educacion_tecnologica", "historia", "ciencias_naturales", "teatro", "comunicacion_social"]
        TablaPrimero.CrearTabla(df, columnas_editables,"segundo_año")
        frmae_button = ctk.CTkFrame(VentanaSegundoCuarta, fg_color="#6A0DAD")
        frmae_button.grid(pady=15, padx=5)
        boton_volver = ctk.CTkButton(frmae_button, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaSegundoCuarta, "Hola mundo"))
        boton_volver.grid(pady=2, padx=2)
    except Exception as scd:
           messagebox.showerror("Exception", f"Exception: {scd}")
    finally:
        VentanaSegundoCuarta.mainloop()
def segundo_quinta_division():
    try:
        # Variables que almacenana informacion para la conexion con base de datos
        global datos_base, df
        consulta = """SELECT * FROM segundo_año WHERE curso = 2 and division = 5"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        VentanaSegundoQuinta = ctk.CTk()
        VentanaSegundoQuinta.title("1/1")
        screen_width = VentanaSegundoQuinta.winfo_screenwidth()
        screen_height = VentanaSegundoQuinta.winfo_screenheight()

        VentanaSegundoQuinta.geometry(f"{screen_width}x{screen_height}")

        TablaPrimero = Crear(VentanaSegundoQuinta)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "educacion_tecnologica", "historia", "ciencias_naturales", "teatro", "comunicacion_social"]
        TablaPrimero.CrearTabla(df, columnas_editables,"segundo_año")
        frmae_button = ctk.CTkFrame(VentanaSegundoQuinta, fg_color="#6A0DAD")
        frmae_button.grid(pady=15, padx=5)
        boton_volver = ctk.CTkButton(frmae_button, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaSegundoQuinta, "Hola mundo"))
        boton_volver.grid(pady=2, padx=2)
    except Exception as sqd:
        messagebox.showerror("Exception", f"Exception: {sqd}")
    finally:
        VentanaSegundoQuinta.mainloop()