import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import math

def redondear_cientos(n): return round(n, -3)

def calcular_poblacion():
    try:
        año1 = int(entry_año1.get())
        p1 = int(entry_p1.get())
        año2 = int(entry_año2.get())
        p2 = int(entry_p2.get())
        año_estimado = int(entry_año_estimado.get())
        if año1 < 0 or año2 < 0 or año_estimado < 0:
            messagebox.showwarning("Los años deben ser valores positivos.")
            return
        if año_estimado <= año2:
            messagebox.showwarning("Advertencia","El año para estimar la población debe ser mayor que el segundo año.")
            return
        if p2 <= p1:
            messagebox.showwarning("Advertencia","La población del segundo año debe ser mayor que la del primer año.")
            return
        if año2 <= año1:
            messagebox.showwarning("Advertencia", "El segundo año debe ser mayor que el primer año.")
            return
        t = año2 - año1
        if t == 0:
            messagebox.showwarning("Advertencia","Los años no deben ser iguales.")
            return
        k = (math.log(p2) - math.log(p1)) / t
        t_estimado = año_estimado - año1
        poblacion_estimada = p1 * math.exp(k * t_estimado)
        poblacion_estimada_redondeada = redondear_cientos(poblacion_estimada)
        label_resultado.config(text=f"Población enferma estimada en el año {año_estimado}: {int(poblacion_estimada_redondeada)}", foreground="black")
    except ValueError as e:
        messagebox.showerror("Advertencia", f"Por favor, ingrese valores válidos.\n{e}")
        return
    
ventana = tk.Tk()
ventana.title("Calculadora de enfermedades usando ED")
ventana.geometry("450x300")
ventana.resizable(False, False)
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TFrame", background="#f0f0f0")
frame = ttk.Frame(ventana, padding="10 10 10 10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
ttk.Label(frame, text="Primer año:").grid(row=0, column=0, sticky=tk.W, pady=5)
entry_año1 = ttk.Entry(frame, width=25)
entry_año1.grid(row=0, column=1, pady=5)
ttk.Label(frame, text="Población enferma en el primer año:").grid(row=1, column=0, sticky=tk.W, pady=5)
entry_p1 = ttk.Entry(frame, width=25)
entry_p1.grid(row=1, column=1, pady=5)
ttk.Label(frame, text="Segundo año:").grid(row=2, column=0, sticky=tk.W, pady=5)
entry_año2 = ttk.Entry(frame, width=25)
entry_año2.grid(row=2, column=1, pady=5)
ttk.Label(frame, text="Población enferma en el segundo año:").grid(row=3, column=0, sticky=tk.W, pady=5)
entry_p2 = ttk.Entry(frame, width=25)
entry_p2.grid(row=3, column=1, pady=5)
ttk.Label(frame, text="Año para estimar la población enferma:").grid(row=4, column=0, sticky=tk.W, pady=5)
entry_año_estimado = ttk.Entry(frame, width=25)
entry_año_estimado.grid(row=4, column=1, pady=5)
btn_calcular = ttk.Button(frame, text="Calcular población", command=calcular_poblacion)
btn_calcular.grid(row=5, columnspan=2, pady=10)
label_resultado = ttk.Label(frame, text="")
label_resultado.grid(row=6, columnspan=2, pady=10)
ventana.mainloop()