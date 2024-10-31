import pygame
from pygame.locals import *
from gl import Renderer
from buffer import Buffer
from model import Model
from shaders import *

width = 1060
height = 1040

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen=screen)

#rend.SetShaders(vShader=vertex_shader, fShader=fragmet_shader)

faceModel = Model("Gun.obj")
faceModel.AddTexture("Gun.bmp")
rend.scene.append(faceModel)

faceModel.rotation.y = 0
faceModel.translation.z = -3
isRunning = True

# Set default shaders
vShader = vertex_shader  # Default vertex shader
fShader = fragmet_shader  # Default fragment shader
#rend.SetShaders(vShader, fShader)
while isRunning:
    deltaTime = clock.tick(60) / 1000
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
            elif event.key == pygame.K_F1:
                Renderer.FillMode()
            elif event.key == pygame.K_F2:
                Renderer.WireFrameMode()
            elif event.key == pygame.K_1:  # Vertex Shader Básico
                vShader = vertex_shader
                fShader = fragmet_shader
                Renderer.SetShaders(vShader, fShader)
            elif event.key == pygame.K_2:  # Wobble Shader
                vShader = Wobble_Shader
                Renderer.SetShaders(vShader, fShader)
            elif event.key == pygame.K_3:  # Twist Shader
                vShader = Twist_Shader
                Renderer.SetShaders(vShader, fShader)
            elif event.key == pygame.K_4:  # Ripple Shader
                vShader = Ripple_Shader
                Renderer.SetShaders(vShader, fShader)
            elif event.key == pygame.K_5:  # Glow Shader
                fShader = Glow_Shader
                Renderer.SetShaders(vShader, fShader)
            elif event.key == pygame.K_6:  # Sepia Shader (si lo tienes disponible)
                fShader = Sepia_Shader
                Renderer.SetShaders(vShader, fShader)

    # Movimiento del modelo
    if keys[K_LEFT]:
        faceModel.rotation.y -= 10 * deltaTime
    if keys[K_RIGHT]:
        faceModel.rotation.y += 10 * deltaTime

    if keys[K_a]:
        Renderer.camera.position.x -= 1 * deltaTime

    if keys[K_d]:
        Renderer.camera.position.x += 1 * deltaTime

    if keys[K_w]:
        Renderer.camera.position.y += 1 * deltaTime

    if keys[K_s]:
        Renderer.camera.position.y -= 1 * deltaTime

    # Movimiento de la luz
    if keys[K_j]:
        Renderer.pointLight.x -= 1 * deltaTime

    if keys[K_l]:
        Renderer.pointLight.x += 1 * deltaTime

    if keys[K_i]:
        Renderer.pointLight.z -= 1 * deltaTime

    if keys[K_k]:
        Renderer.pointLight.z += 1 * deltaTime

    rend.Render()
    pygame.display.flip()

pygame.quit()
