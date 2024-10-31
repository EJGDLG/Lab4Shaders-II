import glm  # pip install PyGLM
# pip install PyOpenGL
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

class Renderer(object):
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_rect().size
        
        glClearColor(0.2, 0.2, 0.2, 1.0)
        glEnable(GL_DEPTH_TEST)
        glViewport(0, 0, self.width, self.height)

        self.scene = []
        self.active_shaders = None

    def SetShaders(self, vShader, fShader):
        if vShader is not None and fShader is not None:
            self.active_shaders = compileProgram(
                compileShader(vShader, GL_VERTEX_SHADER),
                compileShader(fShader, GL_FRAGMENT_SHADER)
            )
        else:
            self.active_shaders = None

    def Render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if self.active_shaders is not None:
            glUseProgram(self.active_shaders)

        for obj in self.scene:
          
            if self.active_shaders is not None:
              glUniformMatrix4fv(glGetUniformLocation(self.active_shaders, "modelMatrix"),
                                 1, GL_FALSE, glm.value_ptr(obj.GetModelMatrix()))
              
              
            obj.Render()
