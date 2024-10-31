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


faceModel  = Model("Gun.obj")
faceModel.AddTexture("Gun.bmp")
rend.scene.append(faceModel)

faceModel.rotation.y = 0
faceModel.translation.z = -3
isRunning = True


while isRunning:
  #esto va a tener mas uso en un frame rate mas aceptable
  deltaTime = clock.tick(60) / 1000
  keys = pygame.key.get_pressed()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      isRunning = False
    elif event.type == pygame.KEYDOWN:
      if event.key  == pygame.K_ESCAPE:
        isRunning = False
      elif event.key == pygame.K_F1:
        Renderer.FillMode()
      elif event.key == pygame.K_F2:
        Renderer.WireFrameMode()
      elif event.key == pygame.K_3:
        vShader = vertex_shader
        Renderer.SetShaders(vShader, fShader)
      elif event.key == pygame.K_4:
        vShader = distortion_shader
        Renderer.SetShaders(vShader, fShader)
      elif event.key == pygame.K_5:
        vShader = water_shader
        Renderer.SetShaders(vShader, fShader)
      elif event.key == pygame.K_6:
        fShader = fragmet_shader
        Renderer.SetShaders(vShader, fShader)
      elif event.key == pygame.K_7:
        fShader = negative_shader
        Renderer.SetShaders(vShader, fShader)
  
        #move model
    if keys[K_LEFT]:
        faceModel.rotation.y -=10*deltaTime
    if keys[K_RIGHT]:
        faceModel.rotation.y +=10*deltaTime
    
    if keys[K_a]:
        Renderer.camera.position.x -= 1 *deltaTime
    
    if keys[K_d]:
        Renderer.camera.position.x += 1 *deltaTime
    
    if keys[K_w]:
        Renderer.camera.position.y += 1 *deltaTime
    
    if keys[K_s]:
        Renderer.camera.position.y -= 1 *deltaTime


    #Move LIghte
    
    if keys[K_j]:
        Renderer.pointLight.x -= 1 *deltaTime
    
    if keys[K_l]:
        Renderer.pointLight.x += 1 *deltaTime
    
    if keys[K_i]:
        Renderer.pointLight.z -= 1 *deltaTime
    
    if keys[K_k]:
        Renderer.pointLight.z += 1 *deltaTime

    
    deltaTime = clock.tick(60) / 1000
    # print(deltaTime)

    rend.Render()
    pygame.display.flip()

pygame.quit()
