import customtkinter as ctk
import customtkinter as ctk
from tkinter import messagebox
from config import Config
from window.clases.clases import Filtrar, Crear, Destruir_pantalla
global datos_base
datos_base = Config.info_db

def primero_primera ():
    
    global datos_base, df
    consulta = """SELECT * FROM primeraño WHERE curso = 1 and division = 1"""
    probando = Filtrar(datos_base)
    df = probando.extraer_datos(consulta)
    print(df.columns)

    VentanaPrimeroPrimera = ctk.CTk()
    VentanaPrimeroPrimera.title("1/1")
    screen_width = VentanaPrimeroPrimera.winfo_screenwidth()
    screen_height = VentanaPrimeroPrimera.winfo_screenheight()

    VentanaPrimeroPrimera.geometry(f"{screen_width}x{screen_height}")

    TablaPrimero = Crear(VentanaPrimeroPrimera)
    columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "Geografia", "Historia", "Ciencias_naturales", "musica", "Artes_visuales"]
    TablaPrimero.CrearTabla( df, columnas_editables, "primeraño")
    frmae_button = ctk.CTkFrame(VentanaPrimeroPrimera, fg_color="#6A0DAD")
    frmae_button.grid(pady=15, padx=5)
    boton_volver = ctk.CTkButton(frmae_button, text="Volver", command= lambda: Destruir_pantalla(VentanaPrimeroPrimera, "Hola mundo"), fg_color="#2C2F33")
    boton_volver.grid(pady=2, padx=2)
    
    VentanaPrimeroPrimera.mainloop()   

def primero_segunda_division():
    # Destruir la ventana anterior
    try:
        global datos_base
        consulta = """SELECT * FROM primeraño WHERE curso = 1 and division = 2"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        # Creamos la ventana para alojar la tabla 
        VentanaPrimeroSegunda = ctk.CTk()
        VentanaPrimeroSegunda.title("1/2")
        screen_width = VentanaPrimeroSegunda.winfo_screenwidth()
        screen_height = VentanaPrimeroSegunda.winfo_screenheight()

        VentanaPrimeroSegunda.geometry(f"{screen_width}x{screen_height}")   

        TablaPrimero = Crear(VentanaPrimeroSegunda)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "Geografia", "Historia", "Ciencias_naturales", "musica", "Artes_visuales"]
        TablaPrimero.CrearTabla(df, columnas_editables,"primeraño")
        frmae_button = ctk.CTkFrame(VentanaPrimeroSegunda, fg_color="#6A0DAD")
        frmae_button.grid(pady=15, padx=5)
        boton_volver = ctk.CTkButton(VentanaPrimeroSegunda, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaPrimeroSegunda, "Hola mundo",fg_color="#2C2F33"))
        boton_volver.grid(pady=2, padx=2)
    except Exception as psd:
        messagebox.showerror("Exception", f"Excepcion en: {psd}")
    finally:    
        VentanaPrimeroSegunda.mainloop()
def primero_tercera_division():
    try:
        global datos_base
        consulta = """SELECT * FROM primeraño WHERE curso = 1 and division = 3"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        # Creamos la ventana para alojar la tabla 
        VentanaPrimeroTercera = ctk.CTk()
        VentanaPrimeroTercera.title("1/2")
        screen_width = VentanaPrimeroTercera.winfo_screenwidth()
        screen_height = VentanaPrimeroTercera.winfo_screenheight()
        VentanaPrimeroTercera.geometry(f"{screen_width}x{screen_height}")   

        TablaPrimero = Crear(VentanaPrimeroTercera)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "Geografia", "Historia", "Ciencias_naturales", "musica", "Artes_visuales"]
        TablaPrimero.CrearTabla(df, columnas_editables,"primeraño")
        frmae_button = ctk.CTkFrame(VentanaPrimeroTercera, fg_color="#6A0DAD")
        frmae_button.grid(pady=15, padx=5)
        boton_volver = ctk.CTkButton(VentanaPrimeroTercera, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaPrimeroTercera, "Hola mundo"),fg_color="#2C2F33")
        boton_volver.grid(pady=2, padx=2)
    except Exception as ptd:
        messagebox.showerror("Exception", f"Excepcion en: {ptd}")
    finally:    
        VentanaPrimeroTercera.mainloop()
def primero_cuarta_division ():
    try:
        global datos_base
        consulta = """SELECT * FROM primeraño WHERE curso = 1 and division = 4"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        # Creamos la ventana para alojar la tabla 
        VentanaPrimeroCuarta = ctk.CTk()
        VentanaPrimeroCuarta.title("1/4")
        screen_width = VentanaPrimeroCuarta.winfo_screenwidth()
        screen_height = VentanaPrimeroCuarta.winfo_screenheight()

        VentanaPrimeroCuarta.geometry(f"{screen_width}x{screen_height}")
        
    

        TablaPrimero = Crear(VentanaPrimeroCuarta)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "Geografia", "Historia", "Ciencias_naturales", "musica", "Artes_visuales"]
        TablaPrimero.CrearTabla(df, columnas_editables,"primeraño")
        frmae_button = ctk.CTkFrame(VentanaPrimeroCuarta, fg_color="#6A0DAD")
        frmae_button.grid(pady=15, padx=5)
        boton_volver = ctk.CTkButton(VentanaPrimeroCuarta, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaPrimeroCuarta, "Hola mundo"),fg_color="#2C2F33")
        boton_volver.grid(pady=2, padx=2)
    except Exception as pcd:
        messagebox.showerror("Exception", f"Excepcion en: {pcd}")
    finally:    
        VentanaPrimeroCuarta.mainloop()
def primero_quinta_division ():
    try:
        global datos_base
        consulta = """SELECT * FROM primeraño WHERE curso = 1 and division = 5"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        # Creamos la ventana para alojar la tabla 
        VentanaPrimeroQuinta = ctk.CTk()
        VentanaPrimeroQuinta.title("1/5")
        screen_width = VentanaPrimeroQuinta.winfo_screenwidth()
        screen_height = VentanaPrimeroQuinta.winfo_screenheight()

        VentanaPrimeroQuinta.geometry(f"{screen_width}x{screen_height}")
    

        TablaPrimero = Crear(VentanaPrimeroQuinta)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "Geografia", "Historia", "Ciencias_naturales", "musica", "Artes_visuales"]
        TablaPrimero.CrearTabla(df, columnas_editables,"primeraño")
        frmae_button = ctk.CTkFrame(VentanaPrimeroQuinta, fg_color="#6A0DAD")
        frmae_button.grid(pady=15, padx=5)
        boton_volver = ctk.CTkButton(VentanaPrimeroQuinta, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaPrimeroQuinta, "Hola mundo"),fg_color="#2C2F33")
        boton_volver.grid(pady=2, padx=2)
    except Exception as pqd:
        messagebox.showerror("Exception", f"Excepcion en {pqd}")
    finally:
        VentanaPrimeroQuinta.mainloop()

