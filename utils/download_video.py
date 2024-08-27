import yt_dlp as youtube_dl
from pydub import AudioSegment
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
import os
import re
import traceback

def sanitize_title(title):
    # Eliminar caracteres que no sean alfanuméricos, espacios, guiones o guiones bajos
    return re.sub(r'[^a-zA-Z0-9\s_-]', '', title)

def format_time(time):
    # Formatear el tiempo a dos decimales
    return f"{time:.2f}"

def download_audio_and_transcript(video_url, options, output_path='./output'):
    result = {}
    try:
        # Verificar si la URL es válida
        if "youtube.com/watch?v=" not in video_url:
            raise ValueError("La URL del vídeo no es válida. Asegúrate de que esté en el formato correcto.")

        # Obtener el título del video para usarlo como nombre de la carpeta
        ydl_opts = {
            'format': 'bestvideo+bestaudio' if 'video' in options else 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }] if 'audio' in options else [],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            video_title = info_dict.get('title', None)
            video_id = info_dict.get('id', None)
            video_ext = info_dict.get('ext', None)

        # Sanitize the video title
        sanitized_title = sanitize_title(video_title)

        # Crear la carpeta con el nombre del video
        video_folder = os.path.join(output_path, sanitized_title)
        os.makedirs(video_folder, exist_ok=True)

        # Descargar el video y/o el audio
        ydl_opts['outtmpl'] = os.path.join(video_folder, '%(title)s.%(ext)s')
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        # Guardar la ruta del archivo de audio si se descargó
        if 'audio' in options or 'all' in options:
            audio_path = os.path.join(video_folder, f"{sanitized_title}.mp3")
            result['audio_path'] = audio_path

        # Guardar la ruta del archivo de video si se descargó
        if 'video' in options or 'all' in options:
            video_path = os.path.join(video_folder, f"{sanitized_title}.{video_ext}")
            result['video_path'] = video_path

        # Obtener las transcripciones si se especifica en las opciones
        if 'transcription' in options or 'all' in options:
            transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
            transcript_paths = []

            # Guardar las transcripciones en archivos separados por idioma
            for transcript in transcripts:
                try:
                    transcript_data = transcript.fetch()
                    if not transcript_data:
                        print(f"No se encontró transcripción para el idioma {transcript.language_code}")
                        continue

                    language_code = transcript.language_code
                    transcript_path = os.path.join(video_folder, f'transcription.{language_code}.txt')
                    # Asegurarse de que el directorio existe antes de escribir el archivo
                    os.makedirs(os.path.dirname(transcript_path), exist_ok=True)
                    with open(transcript_path, 'w', encoding='utf-8') as f:
                        for entry in transcript_data:
                            start_time = format_time(entry['start'])
                            end_time = format_time(entry['start'] + entry['duration'])
                            f.write(f"{start_time} - {end_time}: {entry['text']}\n")
                    print(f"Transcripción en {language_code} guardada en {transcript_path}")
                    transcript_paths.append(transcript_path)
                except (TranscriptsDisabled, NoTranscriptFound):
                    print(f"No se encontró transcripción para el idioma {transcript.language_code}")

            result['transcription_paths'] = transcript_paths

        result['base_path'] = video_folder
        print(f"Video, audio y transcripciones guardados en {video_folder}")
        return result

    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
        return result
