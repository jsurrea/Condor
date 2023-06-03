# Condor
  Integrantes: 
    
    -Juan Sebastian Urrea Lopez
    
    -Haider Yesid Fonseca Najar
    
    -Karol Daniela Arenas Solano
    
    -Juan Andres Guevara Angel
    
    -David Camilo Ocaña Orbes

Esta librería open source en Python está diseñada para identificar objetos de interés en videos y extraer entidades en noticias relacionadas con la afectación ambiental en la Amazonía colombiana. Además, identificar entidades en noticias que describan afectaciones medio 
ambientales a la Amazonía colombiana.

## Objetivo 1: Identificación de objetos en videos




## Objetivo 2: Identificación de entidades en noticias

### Función load_data(path_to_filename: str) -> pd.DataFrame:
Esta funcion se encarga de cargar un archivo de Excel como un DataFrame de pandas y eliminar las muestras que contengan textos vacíos. 

### Función get_impact(text)
Esta función es necesaria ejecutarla después de haber ejecutado el archivo .py correspondiente para cargar y entrenar el modelo. Recibe como parámetro un texto y retorna la categoría predicha para ese texto.

Entrada:
texto: El texto para el cual queremos realizar la predicción de la categoría.
Salida:
categoría: La etiqueta predicha para el texto proporcionado.

Es importante ejecutar el archivo .py antes de utilizar esta función para asegurarse de que el modelo esté cargado y listo para hacer predicciones.

### Funcion ner_from_str(text: str, output_path: str) -> None:
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

### Funcion ner_from_file(text_path: str, output_path: str) -> None:
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

### Funcion ner_from_url(url: str, output_path: str) -> None:
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

