# Condor
  Integrantes: 
    
    -Juan Sebastian Urrea Lopez
    
    -Haider Yesid Fonseca Najar
    
    -Karol Daniela Arenas Solano
    
    -Juan Andres Guevara Angel
    
    -David Camilo Ocaña Orbes

Esta librería open source en Python está diseñada para identificar objetos de interés en videos y extraer entidades en noticias relacionadas con la afectación ambiental en la Amazonía colombiana. Además, identificar entidades en noticias que describan afectaciones medio 
ambientales a la Amazonía colombiana.

## Instalación

Nuestro modelo usa el modelo [SAM](https://github.com/facebookresearch/segment-anything). Para instalarlo, ejecute: 
```
pip install git+https://github.com/facebookresearch/segment-anything.git
pip install opencv-python pycocotools matplotlib onnxruntime onnx
```

Otras dependencias:
```
apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
pip install av torch torchvision numpy easyocr matplotlib opencv-python pandas scikit-learn flair beautifulsoup4
```

## Uso

Instalar con pip: `pip install git+https://github.com/jsurrea/Condor.git`

 ```
 from Condor.Video.segmentation import detect_objects_in_video
 from Condor.Text.NER import ner_from_str, ner_from_file, ner_from_url
 ```

## Objetivo 1: Identificación de objetos en videos

### Función `detect_objects_in_video(video_path: str, output_path: str)`:

Detecta objetos en el video en la ruta `video_path` y guarda un csv de resultados en la ruta `output_path` y un directorio de imágenes segmentadas en el directorio de `output_path`. Ejemplo de uso: `detect_objects_in_video("codefest-data/Videos/VideoCodefest_001-11min.mpg", "Video1.csv")`


## Objetivo 2: Identificación de entidades en noticias

### Función `load_data(path_to_filename: str) -> pd.DataFrame`:
Esta funcion se encarga de cargar un archivo de Excel como un DataFrame de pandas y eliminar las muestras que contengan textos vacíos. 

### Funcion `ner_from_str(text: str, output_path: str) -> None`: 
Recibe como entrada un texto de una noticia y la ruta de salida de un archivo, realiza el proceso de reconocimiento de entidades y la clasificación del impacto del texto. Luego agrupa la información en un diccionario y exporta los resultados en un archivo JSON.

Input:
text (str): El texto de la noticia que se desea analizar.
output_path (str): La ruta del archivo donde se exportarán los resultados.

Output:
Esta función no devuelve ningún valor explícito, pero exporta los resultados en un archivo JSON en la ubicación especificada por output_path.

Resultados:
"text": El texto original de la noticia.
"org": Una lista de entidades organizacionales mencionadas en el texto.
"loc": Una lista de ubicaciones mencionadas en el texto.
"per": Una lista de personas mencionadas en el texto.
"dates": Una lista de fechas mencionadas en el texto.
"misc": Una lista de otras entidades relevantes mencionadas en el texto.
"impact": Una cadena que indica el tipo de impacto medioambiental detectado en el texto.

### Funcion `ner_from_file(text_path: str, output_path: str) -> None`:
recibe como entrada la ruta hacia un archivo de texto y la ruta de salida de un archivo, realiza el proceso de reconocimiento de entidades y la clasificación del impacto del texto contenido en el archivo. Luego, agrupa la información en un diccionario y exporta los resultados en un archivo JSON.

Input:
text_path (str): La ruta del archivo de texto que se desea analizar.
output_path (str): La ruta del archivo donde se exportarán los resultados.

Output:
Esta función no devuelve ningún valor explícito, pero exporta los resultados en un archivo JSON en la ubicación especificada por output_path.

Resultados:
"text": El texto original de la noticia.
"org": Una lista de entidades organizacionales mencionadas en el texto.
"loc": Una lista de ubicaciones mencionadas en el texto.
"per": Una lista de personas mencionadas en el texto.
"dates": Una lista de fechas mencionadas en el texto.
"misc": Una lista de otras entidades relevantes mencionadas en el texto.
"impact": Una cadena que indica el tipo de impacto medioambiental detectado en el texto.

### Funcion `ner_from_url(url: str, output_path: str) -> None:
Recibe como entrada una URL que apunta hacia una noticia y la ruta de salida de un archivo, realiza el proceso de reconocimiento de entidades y la clasificación del impacto del texto contenido en la noticia. Luego, agrupa la información en un diccionario y exporta los resultados en un archivo JSON.

Input:
url (str): La URL de la noticia que se desea analizar.
output_path (str): La ruta del archivo donde se exportarán los resultados.

Output:
Esta función no devuelve ningún valor explícito, pero exporta los resultados en un archivo JSON en la ubicación especificada por output_path.

Resultados:
"text": El texto original de la noticia.
"org": Una lista de entidades organizacionales mencionadas en el texto.
"loc": Una lista de ubicaciones mencionadas en el texto.
"per": Una lista de personas mencionadas en el texto.
"dates": Una lista de fechas mencionadas en el texto.
"misc": Una lista de otras entidades relevantes mencionadas en el texto.
"impact": Una cadena que indica el tipo de impacto medioambiental detectado en el texto.

