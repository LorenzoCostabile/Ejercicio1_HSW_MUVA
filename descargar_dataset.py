"""
Módulo para descargar y extraer los datasets. En el ejercicio 1, solo se pide descargar el dataset Tiny ImageNet.
"""
import requests
import os
from zipfile import ZipFile
import argparse

DATASETS = {
    "tiny-imagenet-200": {
        "url": "http://cs231n.stanford.edu/tiny-imagenet-200.zip",
        "archivo": "tiny-imagenet-200.zip"
    }
}

def descargar(url, nombre_archivo):
    """
    Función de descarga del archivo de un dataset.
    """
    response = requests.get(url, stream=True)
    with open(nombre_archivo, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

def extraer_zip(file, extract_to="."):
    """
    Función para extraer un archivo zip.
    """
    with ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def descargar_dataset(dataset, carpeta_salida):
    """
    Descarga y extrae el dataset especificado en el directorio carpeta_salida
    """
    if dataset not in DATASETS:
        raise ValueError('El dataset ' + dataset + ' no está disponible.')

    url = DATASETS[dataset]["url"]
    archivo = DATASETS[dataset]["archivo"]

    if not os.path.exists(carpeta_salida):
        print('Descargando ' + dataset + ' dataset...')
        descargar(url, archivo)

        print('Extracting ' + dataset + ' dataset...')
        extraer_zip(archivo, carpeta_salida)

        os.unlink(archivo)

        print('Descarga y extracción completada.')
    else:
        print('La carpeta de salida ya existe.')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Descarga y extrae un dataset.')
    parser.add_argument('dataset',
                        type=str,
                        help='Nombre del dataset a descargar y extraer.' +
                            ' Opciones: ' +
                            str(list(DATASETS.keys())),
                        default="tiny-imagenet-200")
    parser.add_argument('carpeta_salida',
                        type=str,
                        help='Directorio relativo donde se guardará el dataset' +
                        ' descargado y extraído.',
                        default=None)

    args = parser.parse_args()

    dataset_seleccionado = args.dataset
    carpeta = args.carpeta_salida
    if carpeta is None:
        carpeta = os.path.join(os.path.dirname(os.path.abspath(__file__)), dataset_seleccionado)
    else:
        carpeta = os.path.join(os.path.dirname(os.path.abspath(__file__)), carpeta)

    descargar_dataset(dataset_seleccionado, carpeta)
