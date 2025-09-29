from clases.utils import new_canvas, set_pixel, save_ppm_p3

# para crear el .venv es python -m venv .venv

def bresenham_line (x0, y0, x1, y1):
    points = []  # Lista para almacenar los puntos de la línea
    dx = abs(x1 - x0)  # Diferencia en x    
    dy = abs(y1 - y0)  # Diferencia en y
    stepX = 1 if x0 < x1 else -1  # Determina la dirección en x
    stepY = 1 if y0 < y1 else -1  # Determina la dirección en y
    err = dx - dy  # Error inicial

    while x0 != x1 or y0 != y1:
        points.append((x0, y0))  # decide para donde moverse
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x0 += stepX
        if e2 < dx:
            err += dx
            y0 += stepY

    return points

#hardcoded
# def draw_line():
#    return [(0,0), (1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9)]

# FUNCION PARA CREAR CANVAS
# def new_canvas(w, h): # width, height
#    return [["___" for _ in range(w)] for _ in range(h)] 
# los corchetes es por la matriz, los for crean las filas y columnas, _ (variable anonima, no se crea en memoria), "__" matriz sin ningun pixel




# para probar
canvas = new_canvas(10,10)
line = bresenham_line(9, 0, 0, 9)  # Cambia los valores para probar diferentes líneas

for x, y in line:
    set_pixel(canvas, x, y)
save_ppm_p3('primeralinea.ppm', canvas)  # Guarda el canvas en un archivo PPM

# line = draw_line (0,0,3,3)

#hardcore
# line = draw_line()
# for x,y in line:
#    set_pixel(canvas, x, y)

#for x, y in line:
#    set_pixel(canvas, x, y)
# print_canvas(canvas)