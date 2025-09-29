#version 330

in vec3 v_color;
out vec4 f_color;

uniform float u_time;

void main() {
    // Color animado con el tiempo
    float pulse = abs(sin(u_time));
    f_color = vec4(v_color * pulse, 1.0);
}