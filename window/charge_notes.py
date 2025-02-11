import customtkinter as ctk
from window.divisions.primero import primero_primera, primero_segunda_division, primero_tercera_division, primero_cuarta_division, primero_quinta_division
from window.divisions.segundo import segundo_primera_division, segundo_segunda_division, segundo_tercera_division, segundo_cuarta_division, segundo_quinta_division
from window.divisions.tercero import tercero_primera_division, tercero_segunda_division, tercero_tercera_division, tercero_cuarta_division, tercero_quinta_division
from window.divisions.cuarto import cuarto_primera_division, cuarto_segunda_division, cuarto_tercera_division, cuarto_cuarta_division, cuarto_quinta_division
from window.divisions.quinto import quinto_primera_division, quinto_segunda_division, quinto_tercera_division, quinto_cuarta_division, quinto_quinta_division

def charge_notes ():
    ## Creamos la ventana de carga de notas
    charge_window = ctk.CTk()
    charge_window.title("Cargar Notas")
    charge_window.geometry("850x450")

    # Title
    label_title = ctk.CTkLabel(charge_window, text="Cargar Notas", font=("Helvetica", 20, "bold"))
    label_title.pack(pady=25, padx=5)

    # año
    label_año = ctk.CTkLabel(charge_window, text="Seleccione un año", font=("Helvetica", 15))
    label_año.pack(pady=5, padx=5)


    def option_selected_year (option):
        print(f"Has seleccionado el año: {option}")
        global año
        año = int(option)

    def option_selected_div (option):
        print(f"Has seleccionado la division: {option}")
        global div
        div = int(option)

    # Crear un ComboBox con opciones
    combo_year = ctk.CTkComboBox(charge_window, 
                            values=["1","2","3","4","5"],
                            command=option_selected_year)  # Se ejecuta al seleccionar
    combo_year.pack(pady=5)

    # Establecer un valor por defecto
    combo_year.set("Seleccionar año")

    # Seleccionar division
    label_division = ctk.CTkLabel(charge_window, text="Seleccionar division", font=("Helvetica", 15))
    label_division.pack(pady=5, padx=5)

    # Crear un ComboBox con opciones
    combo_div = ctk.CTkComboBox(charge_window, 
                            values=["1","2","3","4","5"],
                            command=option_selected_div)  # Se ejecuta al seleccionar
    combo_div.pack(pady=5)

    # Establecer un valor por defecto
    combo_div.set("Selecciona año")


    # boton continuar
    frame_button_continue = ctk.CTkFrame(charge_window, fg_color="#6A0DAD")
    frame_button_continue.pack(pady=15, padx=5, side="bottom")
    button_continue = ctk.CTkButton(frame_button_continue, text="Continuar", fg_color="#2C2F33", command=lambda:condicional_continuar(año, div))
    button_continue.pack(pady=2, padx=2)

    charge_window.mainloop()


def condicional_continuar (año, div):
    if año == 1:
        if div == 1:
            print("Se esta ejecutando 1ro 1ra")
            primero_primera()
        elif div ==2:
            print("Se esta ejecutando 1ro 2ra")
            primero_segunda_division()
        elif div == 3:
            print("Se esta ejecutando 1ro 3ra")
            primero_tercera_division()
        elif div== 4:
            print("Se esta ejecutando 1ro 4ra")
            primero_cuarta_division()
        else:
            print("Se esta ejecutando 1ro 5ra")
            primero_quinta_division()
    elif año == 2:
        
        if div == 1:
            print("Se esta ejecutando 2ro 1ra")
            segundo_segunda_division()
        elif div ==2:
            print("Se esta ejecutando 2ro 2ra")
            segundo_segunda_division()
        elif div == 3:
            print("Se esta ejecutando 2ro 3ra")
            segundo_tercera_division()
        elif div== 4:
            print("Se esta ejecutando 2ro 4ra")
            segundo_cuarta_division()
        else:
            print("Se esta ejecutando 2ro 5ra")
            segundo_quinta_division()
    elif año == 3:

        if div == 1:
            print("Se esta ejecutando 3ro 1ra")
            tercero_primera_division()
        elif div ==2:
            print("Se esta ejecutando 3ro 2ra")
            tercero_segunda_division()
        elif div == 3:
            print("Se esta ejecutando 3ro 3ra")
            tercero_tercera_division()
        elif div== 4:
            print("Se esta ejecutando 3ro 4ra")
            tercero_cuarta_division()
        else:
            print("Se esta ejecutando 3ro 5ra")
            tercero_quinta_division()
    elif año == 4:
        if div == 1:
            print("Se esta ejecutando 4ro 1ra")
            cuarto_primera_division()
            
        elif div ==2:
            print("Se esta ejecutando 4ro 2ra")
            cuarto_segunda_division()
        elif div == 3:
            print("Se esta ejecutando 4o 3ra")
            cuarto_tercera_division()
        elif div== 4:
            print("Se esta ejecutando 4ro 4ra")
            cuarto_cuarta_division()
        else:
            print("Se esta ejecutando 4ro 5ra")
            cuarto_quinta_division()
    else:
        if div == 1:
            print("Se esta ejecutando 5ro 1ra")
            quinto_primera_division()
        elif div ==2:
            print("Se esta ejecutando 5ro 2ra")
            quinto_segunda_division()
        elif div == 3:
            print("Se esta ejecutando 5ro 3ra")
            quinto_tercera_division()
        elif div== 4:
            print("Se esta ejecutando 5ro 4ra")
            quinto_cuarta_division()
        else:
            print("Se esta ejecutando 5ro 5ra")
            quinto_quinta_division()