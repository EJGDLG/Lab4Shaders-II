import pygame
from pygame.locals import *
from gl import Renderer
from buffer import Buffer
from model import Model
from shaders import *

width = 960
height = 540

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen)

#rend.SetShaders(vertex_shader, fragment_shader)

#        Positions          Color
#triangle = [-0.5, -0.5, 0,    1, 0, 0,
#             0, 0.5, 0,      0, 1, 0,
#             0.5, -0.5, 0,   0, 0, 1]

#rend.scene.append(Buffer(triangle))

faceModel  = Model("Gun.obj")
faceModel.AddTexture("Gun.bmp")
rend.scene.append(faceModel)

isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

    deltaTime = clock.tick(60) / 1000
    # print(deltaTime)

    rend.Render()
    pygame.display.flip()

pygame.quit()
