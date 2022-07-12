from lib2to3.pytree import Base
from tkinter import ANCHOR, BOTH, Frame, PhotoImage, Tk, Canvas
from tracemalloc import start

# -----------------------------
# Variables globales
# -----------------------------
BASE = 460
ALTURA = 380

# -----------------------------
# Ventana principal
# -----------------------------

ventana_principal = Tk()
ventana_principal.title("Grafica 2D - Texto")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="green")

# -----------------------------
# Frame de graficacion
# -----------------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="white", width=480, height=400)
frame_graficacion.pack(fill=BOTH, padx=10, pady=10)

# Creacion canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.place(x=10, y=10)

# Texto
texto = c.create_text(BASE/2, ALTURA/2, anchor="center", text= "UIS El Socorro", font=("Arial", "20", "bold"), fill="blue", activefill="red")

# Lineas rectas
linea1 = c.create_line(0,0, BASE, ALTURA, fill="red")
linea2 = c.create_line(0, ALTURA, BASE, 0, fill="black")
linea3 = c.create_line(BASE/2, 0, BASE/2, ALTURA/2, fill="blue")
linea4 = c.create_line(BASE, ALTURA/2, BASE/2, ALTURA/2, fill="orange")
linea5 = c.create_line(BASE/2, ALTURA, BASE/2, ALTURA/2, fill="pink")
linea6 = c.create_line(0, ALTURA/2, BASE/2, ALTURA/2, fill="purple")

# Cuadrados y rectangulos
rect1 = c.create_rectangle(0, 0, BASE/2-20, ALTURA/2-20, fill="yellow", outline="yellow")
rect2 = c.create_rectangle(10,10, 70, 70, fill="black", outline="green")

# Poligonos
Pol1 = c.create_polygon(0, ALTURA, BASE/2, 0, BASE, ALTURA, fill="beige", outline="gray", width=5)
"""Pol2 = c.create_polygon(0, 0, BASE/2, BASE, BASE/2, 0, fill="beige", outline="gray", width=5)"""

# Elipses - Circulos
elip1 = c.create_oval(0, 0, BASE/2, ALTURA/2, fill="orange")
elip2 = c.create_oval(BASE/2, ALTURA/2, BASE/2+40, ALTURA/2+40, fill="violet")

# Arcos
ar1 = c.create_arc(50, 50, 150, 150, fill="green", start=45, extent=5000)

# Imagenes
img = PhotoImage(file="a.gif")
pelota = c.create_image(300,300, image=img, anchor="center")

# Desplegar ventana principal. Queda a la espera de los eventos
ventana_principal.mainloop()