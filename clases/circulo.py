# x^2 + y^2 = r^2
# y = raiz (r^2 - x^2) -> radio de un circulo

# vamos a dibujar 1/8 y luego lo vamos a reflejar

from clases.utils import new_canvas, set_pixel, save_png

def draw_circle(centerX, centerY, radio):
    points = []
    x = 0
    y = -radio 
    while x < -y:
        midPoint = y + 0.5
        decisionPoint =  x** 2 + midPoint**2 - radio**2 # punto de decisión
        if(decisionPoint > radio): # si el punto se esta alejando de la curva, tiene que bajar 
            y += 1
        points.append((centerX + x, centerY + y)) # primer octante
        points.append((centerX - x, centerY + y)) # segundo octante
        points.append((centerX + x, centerY - y)) # tercer octante
        points.append((centerX - x, centerY - y)) # cuarto octante
        points.append((centerX + y, centerY + x)) # quinto octante
        points.append((centerX - y, centerY + x)) # sexto octante
        points.append((centerX + y, centerY - x)) # septimo octante
        points.append((centerX - y, centerY - x)) # octavo octante
        x += 1
    return points

height = 256
width = 256
canvas = new_canvas(width, height)
circle = draw_circle(width//2, height//2, 20)

for x, y in circle:
    set_pixel(canvas, x, y, (255, 255, 255))
save_png("Circulo.png", canvas)
print("done")
