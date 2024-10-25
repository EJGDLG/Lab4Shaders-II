from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# Vertex Shader
vertex_shader_code = """
#version 330 core
layout(location = 0) in vec3 position;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main() {
    gl_Position = projection * view * model * vec4(position, 1.0);
}
"""

# Fragment Shader
fragment_shader_code = """
#version 330 core
out vec4 fragColor;

void main() {
    fragColor = vec4(1.0, 1.0, 1.0, 1.0);  # Color blanco
}
"""

class Renderer:
    def __init__(self):
        # Shader program
        self.shaderProgram = None

        # Vertex Array Object (VAO)
        self.VAO = None

        # Matrices de transformación
        self.modelMatrix = np.identity(4, dtype=np.float32)
        self.viewMatrix = np.identity(4, dtype=np.float32)
        self.projectionMatrix = np.identity(4, dtype=np.float32)

        self.vertices = np.array([
            [-0.5, -0.5, 0.0],
            [0.5, -0.5, 0.0],
            [0.0,  0.5, 0.0]
        ], dtype=np.float32)

    def compile_shader(self, source, shader_type):
        shader = glCreateShader(shader_type)
        glShaderSource(shader, source)
        glCompileShader(shader)

        if not glGetShaderiv(shader, GL_COMPILE_STATUS):
            raise RuntimeError(glGetShaderInfoLog(shader))
        return shader

    def create_shader_program(self, vertex_source, fragment_source):
        vertex_shader = self.compile_shader(vertex_source, GL_VERTEX_SHADER)
        fragment_shader = self.compile_shader(fragment_source, GL_FRAGMENT_SHADER)

        program = glCreateProgram()
        glAttachShader(program, vertex_shader)
        glAttachShader(program, fragment_shader)
        glLinkProgram(program)

        if not glGetProgramiv(program, GL_LINK_STATUS):
            raise RuntimeError(glGetProgramInfoLog(program))
        return program

    def createBuffer(self):
        # Crear Vertex Array Object (VAO)
        self.VAO = glGenVertexArrays(1)
        glBindVertexArray(self.VAO)

        # Crear Vertex Buffer Object (VBO)
        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        # Especificar el formato de los vértices
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 4, None)
        glEnableVertexAttribArray(0)

    def set_matrices(self):
        # Obtener ubicaciones uniformes para las matrices
        modelLoc = glGetUniformLocation(self.shaderProgram, "model")
        viewLoc = glGetUniformLocation(self.shaderProgram, "view")
        projLoc = glGetUniformLocation(self.shaderProgram, "projection")

        # Cargar las matrices a los shaders
        glUniformMatrix4fv(modelLoc, 1, GL_FALSE, self.modelMatrix)
        glUniformMatrix4fv(viewLoc, 1, GL_FALSE, self.viewMatrix)
        glUniformMatrix4fv(projLoc, 1, GL_FALSE, self.projectionMatrix)

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Usa el programa de shaders
        glUseProgram(self.shaderProgram)

        # Cargar matrices de transformación
        self.set_matrices()

        # Dibujar el triángulo
        glBindVertexArray(self.VAO)
        glDrawArrays(GL_TRIANGLES, 0, 3)

        glutSwapBuffers()

    def setup(self):
        self.shaderProgram = self.create_shader_program(vertex_shader_code, fragment_shader_code)
        self.createBuffer()

def display():
    renderer.render()

def initGL():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Establecer color de fondo
    glEnable(GL_DEPTH_TEST)  # Habilitar el test de profundidad

def reshape(w, h):
    glViewport(0, 0, w, h)

    # Actualizar la matriz de proyección
    fov = 45.0
    near, far = 0.1, 100.0
    aspect = w / h

    renderer.projectionMatrix = np.array(gluPerspective(fov, aspect, near, far), dtype=np.float32)
    renderer.viewMatrix = np.array(gluLookAt(0, 0, 3, 0, 0, 0, 0, 1, 0), dtype=np.float32)

if __name__ == "__main__":
    # Inicialización de GLUT y creación de ventana
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("OpenGL Renderer")

    # Crear instancia del renderer
    renderer = Renderer()

    # Inicializar OpenGL
    initGL()

    # Configurar display y reshape
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    # Setup del renderer (cargar shaders y buffer de vértices)
    renderer.setup()

    # Bucle principal de GLUT
    glutMainLoop()
