import customtkinter as ctk
from window.divisions_debtops.all_debtops import ver_adeudantes_primero, ver_adeudantes_segundo, ver_adeudantes_tercero_edu, ver_adeudantes_tercero_cn, ver_adeudantes_cuarto_edu, ver_adeudantes_cuarto_cn, ver_adeudantes_quinto_edu, ver_adeudantes_quinto_cn
def option_selected_year(option):
    print(f"Has seleccionado el curso {option}")
    global año
    año = option

def option_selected_div(option):
    print(f"Has seleccionado la division {option}")
    global div
    div = option

def show_debtops ():
    # Creacion de ventana
    debtops_window = ctk.CTk()
    debtops_window.title("Ventana Adeudantes")
    debtops_window.geometry("850x450")

    # Label_title
    label_title = ctk.CTkLabel(debtops_window, text="Adeudantes", font=("Helvetica", 20, "bold"))
    label_title.pack(pady=25, padx=5)

    label_año = ctk.CTkLabel(debtops_window, text="Seleccione el año", font=("Helvetica", 15))
    label_año.pack(pady=5, padx=5)

    # Creamos un Combobox
    combo_year = ctk.CTkComboBox(debtops_window, 
                                values=["1","2","3","4","5"],
                                command=option_selected_year)  # Se ejecuta al seleccionar
    combo_year.pack(pady=5)

    # Establecer un valor por defecto
    combo_year.set("Seleccionar año")

    label_div = ctk.CTkLabel(debtops_window, text="Seleccione una division", font=("Helvetica", 15))
    label_div.pack(pady=5, padx=5)
    # Creamos un Combobox
    combo_div = ctk.CTkComboBox(debtops_window, 
                                values=["1","2","3","4","5"],
                                command=option_selected_div)  # Se ejecuta al seleccionar
    combo_div.pack(pady=5)

    # Establecer un valor por defecto
    combo_div.set("Seleccione una opcion")

    # Creacion de boton continuar
    frame_continue = ctk.CTkFrame(debtops_window, fg_color="#6A0DAD")
    frame_continue.pack(pady=5, padx=5, side="bottom")
    buttom_continue = ctk.CTkButton(frame_continue, text="Continuar", fg_color="#2C2F33", command=lambda: debtops_conditional(año, div))
    buttom_continue.pack(pady=2, padx=2)



    debtops_window.mainloop()


def debtops_conditional (año, div):
    if año == 1:
        ver_adeudantes_primero()
    elif año == 2:
        ver_adeudantes_segundo()
    elif año == 3:
        if div == 1 or div == 2:
            ver_adeudantes_tercero_edu()
        else:
            ver_adeudantes_tercero_cn()
    elif año == 4:
        if div == 1 or div == 2:
            ver_adeudantes_cuarto_edu()
        else:
            ver_adeudantes_cuarto_cn()
    else:
        if div == 1 or div == 2:
            ver_adeudantes_quinto_edu()
        else:
            ver_adeudantes_quinto_cn