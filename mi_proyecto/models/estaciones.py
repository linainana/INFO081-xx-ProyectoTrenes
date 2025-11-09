class Estacion:
    def __init__(self, nombre, region, poblacion):
        self.nombre = nombre
        self.region = region
        self.poblacion = poblacion
        self.conexiones = []  

    def agregar_conexion(self, estacion_destino):
        if estacion_destino not in self.conexiones:
            self.conexiones.append(estacion_destino)

    def descripcion_estacion(self):
        return f"{self.nombre} ({self.region}) - Población: {self.poblacion}"
