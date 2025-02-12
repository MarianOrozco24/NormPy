from tkinter import messagebox
from window.clases.clases import VerAdeudantes

def ver_adeudantes_primero ():
    try:
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = 'SELECT * FROM primeraño'
        adeudantes_primer_año = VerAdeudantes()
        adeudantes_primer_año.set_cargar_titulo_ventana("Primer año")
        adeudantes_primer_año.set_cargar_titulo_label("Primer año")
        adeudantes_primer_año.configuracion_ventana()
        adeudantes_primer_año.configuracion_carga_label()
        adeudantes_primer_año.mostrar_datos(datos_base, consulta)
    except Exception as vap:
        messagebox.showerror("Error", f"ver_adeudantes_primero | {vap}")
def ver_adeudantes_segundo():
    datos_base = ["localhost", "root","1234", "normal1"]
    consulta = 'SELECT * FROM segundo_año'
    adeudantes_segundo_año = VerAdeudantes()
    adeudantes_segundo_año.set_cargar_titulo_ventana("Segundo año")
    adeudantes_segundo_año.set_cargar_titulo_label("2do Normal")
    adeudantes_segundo_año.configuracion_ventana()
    adeudantes_segundo_año.configuracion_carga_label()
    adeudantes_segundo_año.mostrar_datos(datos_base, consulta)
   
def ver_adeudantes_tercero_cn():
    try:
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = 'SELECT * FROM terceraño_cn'
        adeudantes_tercer_año = VerAdeudantes()
        adeudantes_tercer_año.set_cargar_titulo_ventana("Tercer año")
        adeudantes_tercer_año.set_cargar_titulo_label("Tercer año | Ciencias Naturales")
        adeudantes_tercer_año.configuracion_ventana()
        adeudantes_tercer_año.configuracion_carga_label()
        adeudantes_tercer_año.mostrar_datos(datos_base, consulta)
    except Exception as vap:
        messagebox.showerror("Error", f"ver_adeudantes_tercero_cn | {vap}")
def ver_adeudantes_tercero_edu():
    try:
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = 'SELECT * FROM terceraño_educacion'
        adeudantes_tercero_edu = VerAdeudantes()
        adeudantes_tercero_edu.set_cargar_titulo_ventana("Tercer año")
        adeudantes_tercero_edu.set_cargar_titulo_label("Tercer año | Educacion")
        adeudantes_tercero_edu.configuracion_ventana()
        adeudantes_tercero_edu.configuracion_carga_label()
        adeudantes_tercero_edu.mostrar_datos(datos_base, consulta)
    except Exception as vap:
        messagebox.showerror("Error", f"ver_adeudantes_tercero_edu | {vap}")
def ver_adeudantes_cuarto_cn():
    try:
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = 'SELECT * FROM cuartoaño_cn'
        adeudatnes_cuarto_cn = VerAdeudantes()
        adeudatnes_cuarto_cn.set_cargar_titulo_ventana("Cuarto año")
        adeudatnes_cuarto_cn.set_cargar_titulo_label("Cuarto año | Ciencias Naturales")
        adeudatnes_cuarto_cn.configuracion_ventana()
        adeudatnes_cuarto_cn.configuracion_carga_label()
        adeudatnes_cuarto_cn.mostrar_datos(datos_base, consulta)
    except Exception as vap:
        messagebox.showerror("Error", f"ver_adeudantes_cuarto_cn | {vap}")
def ver_adeudantes_cuarto_edu():
    try:
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = 'SELECT * FROM cuartoaño_educacion'
        adeudantes_cuarto_edu = VerAdeudantes()
        adeudantes_cuarto_edu.set_cargar_titulo_ventana("Cuarto año")
        adeudantes_cuarto_edu.set_cargar_titulo_label("Cuarto año | Educacion")
        adeudantes_cuarto_edu.configuracion_ventana()
        adeudantes_cuarto_edu.configuracion_carga_label()
        adeudantes_cuarto_edu.mostrar_datos(datos_base, consulta)
    except Exception as vap:
        messagebox.showerror("Error", f"ver_adeudantes_cuarto_edu | {vap}")
def ver_adeudantes_quinto_cn():
    try:
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = 'SELECT * FROM quintoaño_cn'
        adeudantes_quinto_cn = VerAdeudantes()
        adeudantes_quinto_cn.set_cargar_titulo_ventana("Quinto año")
        adeudantes_quinto_cn.set_cargar_titulo_label("Quinto año | Ciencias Naturales")
        adeudantes_quinto_cn.configuracion_ventana()
        adeudantes_quinto_cn.configuracion_carga_label()
        adeudantes_quinto_cn.mostrar_datos(datos_base, consulta)
    except Exception as vap:
        messagebox.showerror("Error", f"ver_adeudantes_quinto_cn | {vap}")
def ver_adeudantes_quinto_edu():
    try:
        datos_base = ["localhost", "root","1234", "normal1"]
        consulta = 'SELECT * FROM quintoaño_educacion'
        adeudantes_quinto_edu = VerAdeudantes()
        adeudantes_quinto_edu.set_cargar_titulo_ventana("Quinto año")
        adeudantes_quinto_edu.set_cargar_titulo_label("Quinto año | Educacion")
        adeudantes_quinto_edu.configuracion_ventana()
        adeudantes_quinto_edu.configuracion_carga_label()
        adeudantes_quinto_edu.mostrar_datos(datos_base, consulta)
    except Exception as vap:
        messagebox.showerror("Error", f"ver_adeudantes_quinto_edu | {vap}")
    
