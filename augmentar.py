"""
Módulo que permite augmentar un dataset pasado por parámetro.
"""
import os
import argparse
from PIL import Image
import yaml
import tqdm

class Augmentador:
    """
    Clase que realiza una augmentación de un dataset. Configurada mediante
    un perfil de augmentación en un archivo yaml. Este perfil de augmentación
    tiene como parametros:

        blur: true | false Indica si se aplica un blur a la imagen.
        blur_range: [min, max] Rango de valores para el blur.
        resize: true | false Indica si se aplica un resize a la imagen.
        resize_range: [min, max] Rango de valores para el resize.
        rotate_left_right: true | false Indica si se aplica un rotate left right a la imagen.
        rotate_flip_top_bottom: true | false Indica si se aplica un rotate
                                                flip top bottom a la imagen.
        rotate_90: true | false Indica si se aplica un rotate 90 a la imagen.
        rotate_180: true | false Indica si se aplica un rotate 180 a la imagen.
        rotate_270: true | false Indica si se aplica un rotate 270 a la imagen.
        rotate_transpose: true | false Indica si se aplica un rotate transpose a la imagen.
    
    La clase tiene como parámetros para su construcción:
        ruta_dataset: Ruta de la carpeta donde estan las imagenes a aumentar.
        Se mantendrá la estructura
                        de carpetas del dataset si la hubiera.
        ruta_salida: Ruta de la carpeta donde se guardarán las imágenes aumentadas habiendo
                        mantenido la estructura de carpetas del dataset si la hubiera.
        factor_aumentacion: Factor de aumentación que se aplicará a cada imagen. Minimo 2,
                            si el factor es menor que 2 se lanzará un error en la construcción
                            de la clase.
        ruta_perfil_aumentacion: Ruta del archivo yaml que contiene el perfil de aumentación.
                                Si esta ruta no existe se lanzará un error en la construcción
                                de la clase.
    Para el uso de la clase se debe llamar a la función augmentar() que aplicará la aumentación
    a las imágenes
    """

    def __init__(self,
                 ruta_dataset,
                 ruta_salida,
                 factor_aumentacion,
                 ruta_perfil_aumentacion):

        self.ruta_dataset = ruta_dataset
        self.ruta_salida = ruta_salida
        self.factor_aumentacion = factor_aumentacion
        if self.factor_aumentacion < 2:
            raise ValueError('El factor de aumentación debe ser mayor o igual que 2.')
        self.__cargar_perfil_augmentacion(ruta_perfil_aumentacion)

    def __cargar_perfil_augmentacion(self, ruta_perfil_aumentacion):
        """
        Carga el perfil de aumentación desde un archivo yaml.
        """
        if not os.path.exists(ruta_perfil_aumentacion):
            raise ValueError('El perfil de augmentación ' + ruta_perfil_aumentacion + ' no existe.')

        with open(ruta_perfil_aumentacion, 'r', encoding='utf8') as perfil:
            self.perfil = yaml.load(perfil, Loader=yaml.FullLoader)

    def augmentar(self):
        """
        Función que aplica la aumentación de imágenes.
        """
        
        


