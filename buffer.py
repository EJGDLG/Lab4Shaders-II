# pip install PyOpenGL
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
							4*6,                  # Stride
							ctypes.c_void_p(4*3))
                             						# Offset
		glEnableVertexAttribArray(0)              # Enable attribute array
	
		glDrawArrays( GL_TRIANGLES, 0, int(len(self.vertBuffer)/6) )

