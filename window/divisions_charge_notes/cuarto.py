import customtkinter as ctk
import customtkinter as ctk
from tkinter import messagebox
from window.clases.clases import Filtrar, Crear, Destruir_pantalla


def cuarto_primera_division():
    # Variables que almacenana informacion para la conexion con base de datos
    try:
        global datos_base, df
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = """SELECT * FROM cuartoaño_educacion WHERE curso = 4 and division = 1"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        VentanaCuartoPrimera = ctk.CTk()
        VentanaCuartoPrimera.title("4/1")
        screen_width = VentanaCuartoPrimera.winfo_screenwidth()
        screen_height = VentanaCuartoPrimera.winfo_screenheight()

        VentanaCuartoPrimera.geometry(f"{screen_width}x{screen_height}")

        TablaPrimero = Crear(VentanaCuartoPrimera)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "geografia", "historia", "educacion_tic", "logica_epistemologia", "quimica", "psicologia", "perspectivas_pedagogicas"]
        TablaPrimero.CrearTabla(df, columnas_editables,"cuartoaño_educacion")
        boton_volver = ctk.CTkButton(VentanaCuartoPrimera, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaCuartoPrimera, "Hola mundo"))
        boton_volver.grid(pady=20, padx=10)
    except Exception as cpd:
        messagebox.showerror("Exception", f"Excepcion: {cpd}")
    finally:
        VentanaCuartoPrimera.mainloop()
def cuarto_segunda_division():
    # Variables que almacenana informacion para la conexion con base de datos
    try:
        global datos_base, df
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = """SELECT * FROM cuartoaño_educacion WHERE curso = 4 and division = 2"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        VentanaCuartoSegunda = ctk.CTk()
        VentanaCuartoSegunda.title("4/2")
        screen_width = VentanaCuartoSegunda.winfo_screenwidth()
        screen_height = VentanaCuartoSegunda.winfo_screenheight()

        VentanaCuartoSegunda.geometry(f"{screen_width}x{screen_height}")

        TablaPrimero = Crear(VentanaCuartoSegunda)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "geografia", "historia", "educacion_tic", "logica_epistemologia", "quimica", "psicologia", "perspectivas_pedagogicas"]
        TablaPrimero.CrearTabla(df, columnas_editables,"cuartoaño_educacion")
        boton_volver = ctk.CTkButton(VentanaCuartoSegunda, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaCuartoSegunda, "Hola mundo"))
        boton_volver.grid(pady=20, padx=10)
    except Exception as csd:
        messagebox.showerror("Exception", f"Excepcion: {csd}")
    finally:
        VentanaCuartoSegunda.mainloop()
def cuarto_tercera_division():
    # Variables que almacenana informacion para la conexion con base de datos
    try:
        global datos_base, df
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = """SELECT * FROM cuartoaño_cn WHERE curso = 4 and division = 3"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        VentanaCuartoTercera = ctk.CTk()
        VentanaCuartoTercera.title("4/3")
        screen_width = VentanaCuartoTercera.winfo_screenwidth()
        screen_height = VentanaCuartoTercera.winfo_screenheight()

        VentanaCuartoTercera.geometry(f"{screen_width}x{screen_height}")

        TablaPrimero = Crear(VentanaCuartoTercera)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "ciencias_naturales_tic", "formacion_etica", "fisica", "biologia", "quimica", "construccion_social", "metodologia"]
        TablaPrimero.CrearTabla(df, columnas_editables,"cuartoaño_cn")
        boton_volver = ctk.CTkButton(VentanaCuartoTercera, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaCuartoTercera, "Hola mundo"))
        boton_volver.grid(pady=20, padx=10)
    except Exception as ctd:
        messagebox.showerror("Exception", f"Excepcion: {ctd}")
    finally:
        VentanaCuartoTercera.mainloop()
def cuarto_cuarta_division():
    # Variables que almacenana informacion para la conexion con base de datos
    try:
        global datos_base, df
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = """SELECT * FROM cuartoaño_cn WHERE curso = 4 and division = 4"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        VentanaCuartoCuarta = ctk.CTk()
        VentanaCuartoCuarta.title("4/4")
        screen_width = VentanaCuartoCuarta.winfo_screenwidth()
        screen_height = VentanaCuartoCuarta.winfo_screenheight()

        VentanaCuartoCuarta.geometry(f"{screen_width}x{screen_height}")

        TablaPrimero = Crear(VentanaCuartoCuarta)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "ciencias_naturales_tic", "formacion_etica", "fisica", "biologia", "quimica", "construccion_social", "metodologia"]
        TablaPrimero.CrearTabla(df, columnas_editables,"cuartoaño_cn")
        boton_volver = ctk.CTkButton(VentanaCuartoCuarta, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaCuartoCuarta, "Hola mundo"))
        boton_volver.grid(pady=20, padx=10)
    except Exception as ccd:
        messagebox.showerror("Exception", f"Excepcion: {ccd}")
    finally:
        VentanaCuartoCuarta.mainloop()
def cuarto_quinta_division():
    # Variables que almacenana informacion para la conexion con base de datos
    try:
        global datos_base, df
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = """SELECT * FROM cuartoaño_cn WHERE curso = 4 and division = 5"""
        probando = Filtrar(datos_base)
        df = probando.extraer_datos(consulta)

        VentanaCuartoQuinta = ctk.CTk()
        VentanaCuartoQuinta.title("4/5")
        screen_width = VentanaCuartoQuinta.winfo_screenwidth()
        screen_height = VentanaCuartoQuinta.winfo_screenheight()

        VentanaCuartoQuinta.geometry(f"{screen_width}x{screen_height}")

        TablaPrimero = Crear(VentanaCuartoQuinta)
        columnas_editables = ["lengua", "matematica", "educacion_fisica", "lengua_extranjera", "ciencias_naturales_tic", "formacion_etica", "fisica", "biologia", "quimica", "construccion_social", "metodologia"]
        TablaPrimero.CrearTabla(df, columnas_editables,"cuartoaño_cn")
        boton_volver = ctk.CTkButton(VentanaCuartoQuinta, text="<-- Volver", command= lambda: Destruir_pantalla(VentanaCuartoQuinta, "Hola mundo"))
        boton_volver.grid(pady=20, padx=10)
    except Exception as cqd:
        messagebox.showerror("Exception", f"Excepcion: {cqd}")
    finally:
        VentanaCuartoQuinta.mainloop()