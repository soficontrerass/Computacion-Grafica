#version 330

in vec2 in_pos;
in vec3 in_color;
out vec3 v_color;

uniform float u_time;

void main() {
    // Rotación animada
    float angle = u_time;
    mat2 rot = mat2(cos(angle), -sin(angle), sin(angle), cos(angle));
    vec2 pos = rot * in_pos;
    gl_Position = vec4(pos, 0.0, 1.0);
    v_color = in_color;
}
