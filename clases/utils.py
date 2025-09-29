from PIL import Image

# FUNCION PARA CREAR CANVAS
def new_canvas(w, h, backgroundColor = (0, 0, 0)): # width, height, rgb color negro
    return [[backgroundColor for _ in range(w)] for _ in range(h)]

# FUNCION PARA DIBUJAR UN PIXEL (caracter)
def set_pixel(canvas, x, y, pixelColor = (1,1,1)):
    h = len(canvas)  # ver el espacio que tengo
    w = len(canvas[0])  # posicionarlo
    if 0 <= x < w and 0 <= y < h:
        canvas[y][x] = pixelColor

# FUNCION PARA MOSTRAR EL CANVAS EN CONSOLA 
def print_canvas(imagen):
    for row in imagen:
        print('|'.join(row)) 

def save_ppm_p3(filename, canvas):
    #guardar en formato ppm p3 (con caracteres)
    #la estructura: ancho, alto, valor max de color, triplas de pixeles
    h = len (canvas)
    w = len (canvas[0])
    with open(filename, 'w', encoding = "ascii") as f:
        f.write(f'P3\n{w} {h}\n255\n')  # P3 es el formato, ancho y alto, valor maximo de color
        for row in canvas:
            line = []
            for (r,g,b) in row:
                line.append(f'{r} {g} {b}')
            f.write(' '.join(line) + '\n')


# FUNCION PARA GUARDAR EN FORMATO PNG
def save_png(filename, canvas):
    """Guarda la imagen en PNG usando Pillow""" # texto descriptivo para una funcion, util
    h = len(canvas)
    w = len(canvas[0])
    image = Image.new("RGB", (w, h))
    # Flatten de la lista de listas
    pixels_flat = [pixel for row in canvas for pixel in row] # recorre cada fila de img y dentro de cada fila recorre cada pixel
    image.putdata(pixels_flat)
    image.save(filename, "PNG")