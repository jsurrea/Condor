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

### Función ner_from_str(text, output_path)
Esta función recibe un texto como entrada y genera un archivo JSON con el resultado del análisis de reconocimiento de entidades. El archivo de salida contiene el texto original, las entidades identificadas de tipo organización, ubicación, persona, fechas y otras entidades misceláneas, así como el impacto relacionado con la afectación medioambiental.

### Función get_impact(text)
Esta función es necesaria ejecutarla después de haber ejecutado el archivo .py correspondiente para cargar y entrenar el modelo. Recibe como parámetro un texto y retorna la categoría predicha para ese texto.

Entrada:
texto: El texto para el cual queremos realizar la predicción de la categoría.
Salida:
categoría: La etiqueta predicha para el texto proporcionado.

Es importante ejecutar el archivo .py antes de utilizar esta función para asegurarse de que el modelo esté cargado y listo para hacer predicciones.






