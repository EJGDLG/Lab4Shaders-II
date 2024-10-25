from obj import Obj
from buffer import Buffer
from  pygame import image

class Model(object):
    def __init__(self, filename):
        objFile = Obj(filename)

        self.vertices = objFile.vertices
        self.texCoords = objFile.texcoords
        self.normals = objFile.normals
        self.faces = objFile.faces
        self.texture = None
        self.buffer = Buffer(self.BuildBuffer())

    def BuildBuffer(self):
        data = []

        for face in self.faces:

            faceVerts = []

            for i in range(len(face)):
                vert = []

                position = self.vertices[face[i][0] - 1]

                for value in position:
                    vert.append(value)

                vts = self.texCoords[face[i][1] - 1]

                for value in vts:
                    vert.append(value)

                normals = self.texCoords[face[i][1] - 1]

                for value in normals:
                    vert.append(value)

                faceVerts.append(vert)

                for value in faceVerts[0]: 
                    data.append(value)
                for value in faceVerts[1]:
                    data.append(value)
                for value in faceVerts[2]:
                    data.append(value)
                if len(faceVerts) == 4:
                    for value in faceVerts[0]:
                        data.append(value)
                    for value in faceVerts[2]:
                        data.append(value)
                    for value in faceVerts[3]:
                        data.append(value)

                return data


    def AddTexture(self, textureFilename):
        self.textureSurface = image.load(textureFilename)
        self.textureData = image.tostring(self.textureSurface, "RGB", True)
        self.texture = glGenTextures(1)

    def Render(self):
        # Dar la textura
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.texture)

        glTexImage2D(GL_TEXTURE_2D,
                    0,              # Positions
                    GL_RGB,         # Format
                    0,              # Width
                    0,              # Height
                    0,              # Border
                    0,              # Format
                    0,              # Type
                    0)              # Data

      
        self.buffer.Render()          