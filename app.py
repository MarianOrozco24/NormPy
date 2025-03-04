import customtkinter as ctk
from window.charge_notes import charge_notes
from window.show_debtops import show_debtops
from window.quick_analysis_window import fuction_scraping_window

# Creamos la interfaz grafica
principal_windows = ctk.CTk()
principal_windows.title("Pantalla principal")
principal_windows.geometry("850x500")

#Frames 

# Texto de la explicacion
text= """ Seleccione una opcion para continuar """


#Labels
label_title = ctk.CTkLabel(principal_windows, text="Ventana Principal", font=("Helvetica", 20, "bold"))
label_title.pack(pady=15 , padx=15)
label_explication = ctk.CTkLabel(principal_windows, text=text ,font=("Helvetica", 15, "bold"))
label_explication.pack(pady=25, padx=5)


# Frames para botones
frame_charge_notes = ctk.CTkFrame(principal_windows,fg_color="#6A0DAD")
frame_charge_notes.pack(pady=15, padx=5)
frame_debtors = ctk.CTkFrame(principal_windows, fg_color="#6A0DAD")
frame_debtors.pack(pady=15, padx=5)
frame_delete_students = ctk.CTkFrame(principal_windows, fg_color="#6A0DAD")
frame_delete_students.pack(pady=15, padx=5)
frame_add_students = ctk.CTkFrame(principal_windows, fg_color="#6A0DAD")
frame_add_students.pack(pady=15, padx=5)
frame_fast_analitics = ctk.CTkFrame(principal_windows, fg_color="#6A0DAD")
frame_fast_analitics.pack(pady=15, padx=5)

# buttons
charge_notes_button = ctk.CTkButton(frame_charge_notes, text="Cargar Notas", fg_color="#2C2F33", command=charge_notes)
charge_notes_button.pack(pady=2, padx=2)
show_debtors_button = ctk.CTkButton(frame_debtors, text="Ver adeudantes", fg_color="#2C2F33", command=show_debtops)
show_debtors_button.pack(pady=2, padx=2)
delete_students_button = ctk.CTkButton(frame_delete_students, text="Eliminar alumnos", fg_color="#2C2F33")
delete_students_button.pack(pady=2, padx=2)
add_students_button = ctk.CTkButton(frame_add_students, text="Agregar alumnos", fg_color="#2C2F33")
add_students_button.pack(pady=2, padx=2)
fast_analitics_buttom = ctk.CTkButton(frame_fast_analitics, text="Analisis rapido", fg_color="#2C2F33", command=fuction_scraping_window)
fast_analitics_buttom.pack(pady=2, padx=2)



principal_windows.mainloop()



