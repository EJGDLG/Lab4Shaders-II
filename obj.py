class Obj(object):
    def __init__(self, filename):
        # Asumiendo que el archivo es un formato .obj
        with open(filename, 'r') as file:
            lines = file.read().splitlines()

        self.vertices = []
        self.texcoords = []
        self.normals = []
        self.faces = []

        for line in lines:
            # Si la línea no cuenta con un prefijo y un valor, seguimos a la siguiente línea
            line = line.rstrip()

            try:
                prefix, value = line.split(" ", 1)
            except:
                continue

            # Dependiendo del prefijo, parseamos y guardamos la información en el contenedor correcto
            if prefix == "v":  # Vértices
                vert = list(map(float, value.split(" ")))
                self.vertices.append(vert)

            elif prefix == "vt":  # Coordenadas de textura
                vts = list(map(float, value.split(" ")))
                self.texcoords.append([vts[0], vts[1]])

            elif prefix == "vn":  # Normales
                norm = list(map(float, value.split(" ")))
                self.normals.append(norm)

            elif prefix == "f":  # Caras
                face = []
                for vert in value.split(" "):
                    face.append(list(map(int, vert.split("/"))))
                self.faces.append(face)
