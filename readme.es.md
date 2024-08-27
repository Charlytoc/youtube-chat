# Asistente de Video de YouTube

Este proyecto proporciona un conjunto de herramientas para descargar audio, video y transcripciones de videos de YouTube. Además, puede generar resúmenes y permitir a los usuarios chatear con el contenido del video utilizando varios proveedores de IA.

## Requisitos Previos

Antes de comenzar, asegúrate de haber cumplido con los siguientes requisitos:

- **Python**: Asegúrate de tener Python 3.6 o superior instalado. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
- **Git**: Asegúrate de tener Git instalado. Puedes descargarlo desde [git-scm.com](https://git-scm.com/downloads).

## Instalación

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/Charlytoc/youtube-chat.git
   cd YouTube-Video-Assistant
   ```

2. **Instala las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configura las variables de entorno**:
   - Copia el archivo `.env.example` a `.env`:
     ```bash
     cp .env.example .env
     ```
   - Agrega tus claves API al archivo `.env`:
     ```
     OPENAI_API_KEY=tu_clave_api_de_openai
     GROQ_API_KEY=tu_clave_api_de_groq
     ```

## Uso

1. **Ejecuta el script**:

   ```bash
   python main.py
   ```

2. **Sigue las indicaciones**:

   - Introduce la URL del video de YouTube cuando se te solicite.
   - Selecciona las opciones deseadas ingresando los números correspondientes separados por comas:
     ```
     1. Audio
     2. Video
     3. Transcripción
     4. Todo
     5. Generar Resumen
     6. Chatear con el Video
     ```

3. **Generar Resumen**:

   - Si seleccionas la opción "Generar Resumen", el script generará un resumen de la transcripción del video y lo guardará en el directorio de salida.

4. **Chatear con el Video**:
   - Si seleccionas la opción "Chatear con el Video", puedes interactuar con el contenido del video haciendo preguntas. El script utilizará el proveedor de IA seleccionado para generar respuestas basadas en la transcripción del video.

## Ejemplo

Aquí tienes un ejemplo de cómo usar el script:

1. Ejecuta el script:

   ```bash
   python main.py
   ```

2. Introduce la URL del video de YouTube:

   ```
   Por favor, introduce el enlace del vídeo de YouTube: https://www.youtube.com/watch?v=dQw4w9WgXcQ
   ```

3. Selecciona las opciones deseadas:

   ```
   1. Audio
   2. Video
   3. Transcripción
   4. Todo
   5. Generar Resumen
   6. Chatear con el Video
   Introduce los números de las opciones deseadas separados por comas: 4,5,6
   ```

4. Sigue las indicaciones para generar un resumen y chatear con el contenido del video.

## Contribuir

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature-branch`).
3. Realiza tus cambios y haz un commit (`git commit -m 'Agregar alguna característica'`).
4. Empuja a la rama (`git push origin feature-branch`).
5. Crea un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.