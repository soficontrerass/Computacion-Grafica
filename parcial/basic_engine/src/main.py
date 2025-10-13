from window import Window
from texture import Texture
from material import Material
from shader_program import ShaderProgram
from cube import Cube
from quad import Quad
from camera import Camera
from scene import Scene, RayScene  # Importa RayScene
import numpy as np
from pathlib import Path

# --- Loop principal ---

WIDTH, HEIGHT = 800, 600  # Constantes globales

window = Window(WIDTH, HEIGHT, "Basic Graphic Engine")

# Shaders
BASE_DIR = Path(__file__).parent.parent
SHADERS_DIR = BASE_DIR / "shaders"

shader_program = ShaderProgram(
    window.ctx,
    str(SHADERS_DIR / 'basic.vert'),
    str(SHADERS_DIR / 'basic.frag')
)
shader_program_skybox = ShaderProgram(
    window.ctx,
    str(SHADERS_DIR / 'sprite.vert'),
    str(SHADERS_DIR / 'sprite.frag')
)

# Textura para el Quad (framebuffer del raytracer)
skybox_texture = Texture(width=WIDTH, height=HEIGHT, channels_amount=3, color=(0, 0, 0))

# Materiales
material = Material(shader_program)
material_sprite = Material(shader_program_skybox, textures_data=[skybox_texture])

# Objetos
cube1 = Cube((-2, 0, 2), (0, 45, 0), (1, 1, 1), name="Cube1")
cube2 = Cube((2, 0, 2), (0, 45, 0), (1, 0.5, 1), name="Cube2")
quad = Quad((0, 0, 0), (0, 0, 0), (6.5, 1, 1), name="Sprite", hittable=False)

# Cámara
camera = Camera((0, 0, 10), (0, 0, 0), (0, 1, 0), 45, WIDTH / HEIGHT, 0.1, 100.0)

# Escena con Raytracing CPU
scene = RayScene(window.ctx, camera, WIDTH, HEIGHT)
scene.add_object(quad, material_sprite)
scene.add_object(cube1, material)
scene.add_object(cube2, material)
window.set_scene(scene)

window.run()