import json
import os

class EstadoGuardado:

  def __init__(self, ruta_archivo="config/estado_guardado.json"):
    self.ruta_archivo = ruta_archivo

  def guardar(self, estado):
    try:
      carpeta=os.path.dirname(self.ruta_archivo)



