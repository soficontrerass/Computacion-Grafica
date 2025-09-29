import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from utils import new_canvas, set_pixel, save_png
from bresenhamLine import bresenham_line
from middlePointCircle import middle_point_circle

WIDTH, HEIGHT = 400, 400 # Tamaño de canvas/ventana
COLOR = (255, 255, 255) # Color de figuras

# 1) Crear el canvas lógico (array de píxeles) con WIDTH y HEIGHT, inicializado con fondo negro
canvas_data = new_canvas(WIDTH, HEIGHT, (0, 0, 0))

# Tkinter setup
root = tk.Tk()
root.title("Mini Paint Casero")

# Imagen con Pillow para usar en Tkinter 
img = Image.new("RGB", (WIDTH, HEIGHT), (0, 0, 0)) # Asigno un color de fondo de la ventana de dibujo, modo oscuro
photo = ImageTk.PhotoImage(img)
label = tk.Label(root, image=photo)
label.pack()

# Estado
mode = tk.StringVar(value="linea")
points = [] # Variable global de puntos

# Copia el canvas lógico a la imagen Pillow y la refresca en Tkinter, para poder mantener la lógica de nuestros algoritmos.
def redraw_canvas():
    global photo, img
    # Flatten de los píxeles
    pixels = [pix for row in canvas_data for pix in row]
    img.putdata(pixels)
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo)
    label.image = photo

# Maneja los clicks de los botones según el modo de dibujo (línea, círculo, etc.)
def on_click(event):
    global points
    points.append((event.x, event.y))

    # --- Dibujar Línea ---
    if mode.get() == "linea" and len(points) == 2:
        linea = bresenham_line(points[0][0], points[0][1], points[1][0], points[1][1])
        for x, y in linea:
            set_pixel(canvas_data, x, y, COLOR)
        redraw_canvas()
        points = []

    # --- Dibujar Rectángulo ---
    elif mode.get() == "rect" and len(points) == 2:
        x0, y0 = points[0]
        x1, y1 = points[1]
        # Arriba
        for x, y in bresenham_line(x0, y0, x1, y0):
            set_pixel(canvas_data, x, y, COLOR)
        # Derecha
        for x, y in bresenham_line(x1, y0, x1, y1):
            set_pixel(canvas_data, x, y, COLOR)
        # Abajo
        for x, y in bresenham_line(x1, y1, x0, y1):
            set_pixel(canvas_data, x, y, COLOR)
        # Izquierda
        for x, y in bresenham_line(x0, y1, x0, y0):
            set_pixel(canvas_data, x, y, COLOR)
        redraw_canvas()
        points = []

    # --- Dibujar Círculo ---
    elif mode.get() == "circle" and len(points) == 2:
        (cx, cy), (px, py) = points
        r = int(((px - cx) ** 2 + (py - cy) ** 2) ** 0.5)
        circulo = middle_point_circle(cx, cy, r)
        for x, y in circulo:
            set_pixel(canvas_data, x, y, COLOR)
        redraw_canvas()
        points = []

    # --- Dibujar Triángulo ---
    elif mode.get() == "tri" and len(points) == 3:
        for i in range(3):
            x0, y0 = points[i]
            x1, y1 = points[(i + 1) % 3]
            for x, y in bresenham_line(x0, y0, x1, y1):
                set_pixel(canvas_data, x, y, COLOR)
        redraw_canvas()
        points = []

def save_image():
    filename = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG files", "*.png")])
    if filename:
        save_png(filename, canvas_data)

# Creamos los botones con Tkinter en un recuadro distinto al canvas
frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Línea", command=lambda: mode.set("linea")).pack(side=tk.LEFT)
tk.Button(frame, text="Rectángulo", command=lambda: mode.set("rect")).pack(side=tk.LEFT)
tk.Button(frame, text="Círculo", command=lambda: mode.set("circle")).pack(side=tk.LEFT)
tk.Button(frame, text="Triángulo", command=lambda: mode.set("tri")).pack(side=tk.LEFT)
tk.Button(frame, text="Guardar", command=save_image).pack(side=tk.LEFT)

label.bind("<Button-1>", on_click)
redraw_canvas()
root.mainloop()