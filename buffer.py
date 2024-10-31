import glm
from numpy import array, float32
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

class Buffer(object):
    def __init__(self, data):
        self.vertBuffer = array(data, float32)

        # Vertex Buffer Object
        self.VBO = glGenBuffers(1)

        # Vertex Array Object
        self.VAO = glGenVertexArrays(1)

    def Render(self):
        # Atar los buffer objects a la tarjeta de video
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBindVertexArray(self.VAO)

        # Mandar la información de vértices
        glBufferData(GL_ARRAY_BUFFER,
                     self.vertBuffer.nbytes,  # Buffer size in bytes
                     self.vertBuffer,         # Buffer data
                     GL_STATIC_DRAW)          # Usage

        # Atributos

        # Atributo de posiciones
        glVertexAttribPointer(0,                  # Attribute number
                              3,                  # Number of components per vertex
                              GL_FLOAT,           # Data type
                              GL_FALSE,           # Normalized or not
                              4*8,                # Stride
                              ctypes.c_void_p(0)) # Offset
        glEnableVertexAttribArray(0)

        # Atributo de textura
        glVertexAttribPointer(1,                  # Attribute number
                              2,                  # Number of components per vertex
                              GL_FLOAT,           # Data type
                              GL_FALSE,           # Normalized or not
                              4*8,                # Stride
                              ctypes.c_void_p(4*3))  # Offset
        glEnableVertexAttribArray(1)             # Enable attribute array

        # Otro atributo  nomales(ajustar según corresponda)
        glVertexAttribPointer(2,                  # Attribute number
                              3,                  # Number of components per vertex
                              GL_FLOAT,           # Data type
                              GL_FALSE,           # Normalized or not
                              4*8,                # Stride
                              ctypes.c_void_p(4*5)) # Offset
        glEnableVertexAttribArray(2)

        glDrawArrays(GL_TRIANGLES, 0, int(len(self.vertBuffer) / 8))
