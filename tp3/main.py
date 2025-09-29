import pyglet
import moderngl
import numpy as np
from pathlib import Path

class Window(pyglet.window.Window):
    def __init__(self):
        super().__init__(640, 480, "TP3 - Triángulo Animado")
        self.ctx = moderngl.create_context()
        shader_dir = Path(__file__).parent

        with open(shader_dir / "vertex.glsl") as f:
            vertex_shader_src = f.read()
        with open(shader_dir / "fragment.glsl") as f:
            fragment_shader_src = f.read()

        self.prog = self.ctx.program(
            vertex_shader=vertex_shader_src,
            fragment_shader=fragment_shader_src
        )

        # Triángulo: x, y, r, g, b
        triangle = [
            (0.0,  0.3, 1.0, 0.0, 0.0),  # arriba, rojo
            (-0.3, -0.3, 0.0, 1.0, 0.0), # izquierda, verde
            (0.3, -0.3, 0.0, 0.0, 1.0),  # derecha, azul
        ]
        vertices = []
        for (px, py, r, g, b) in triangle:
            vertices.extend([px, py, r, g, b])
        vertices_array = np.array(vertices, dtype="f4")
        vbo = self.ctx.buffer(vertices_array.tobytes())
        self.vao = self.ctx.vertex_array(
            self.prog, [(vbo, "2f 3f", "in_pos", "in_color")]
        )

        self.time = 0.0
        self.paused = False

    def on_draw(self):
        self.clear()
        self.ctx.clear(0.1, 0.1, 0.1)
        self.prog['u_time'].value = self.time
        self.vao.render(mode=moderngl.TRIANGLES)

    def update(self, dt):
        if not self.paused:
            self.time += dt

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.SPACE:
            self.paused = not self.paused

if __name__ == "__main__":
    win = Window()
    pyglet.clock.schedule_interval(win.update, 1/60)
    pyglet.app.run()