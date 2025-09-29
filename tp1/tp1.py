from utils import new_canvas, set_pixel, save_ppm_p3

def bresenham_line(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    stepX = 1 if x0 < x1 else -1
    stepY = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x0 += stepX
        if e2 < dx:
            err += dx
            y0 += stepY
    return points



# --- Dibujo del TP1 ---
canvas = new_canvas(50, 50)

# Línea diagonal de esquina superior izq a inferior der
for x, y in bresenham_line(0, 0, 49, 49):
    set_pixel(canvas, x, y, (255, 0, 0))  # rojo

# Línea diagonal de esquina superior der a inferior izq
for x, y in bresenham_line(49, 0, 0, 49):
    set_pixel(canvas, x, y, (0, 255, 0))  # verde

save_ppm_p3('tp1.ppm', canvas)
