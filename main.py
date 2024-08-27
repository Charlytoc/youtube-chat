from utils.download_video import download_audio_and_transcript
from utils.completions import (
    create_completion_ollama,
    create_groq_completion,
    create_openai_completion,
)
from utils.print_in_color import print_in_color
import os
from dotenv import load_dotenv


def load_env_variables():
    load_dotenv()


def get_video_url():
    return input("Por favor, introduce el enlace del vídeo de YouTube: ")


def get_user_options():
    print_in_color(
        "1. Audio\n2. Video\n3. Transcription\n4. All\n5. Generate Summary\n6. Chat with Video",
        "blue",
    )
    option_numbers = input(
        "Introduce los números de las opciones deseadas separados por comas: "
    ).split(",")
    options_map = {
        "1": "audio",
        "2": "video",
        "3": "transcription",
        "4": "all",
        "5": "generate_summary",
        "6": "chat_with_video",
    }
    options = [
        options_map[num.strip()] for num in option_numbers if num.strip() in options_map
    ]

    # Ensure transcription is selected if generate_summary or chat_with_video is selected
    if "generate_summary" in options and "transcription" not in options:
        options.append("transcription")
    if "chat_with_video" in options and "transcription" not in options:
        options.append("transcription")

    return options


def generate_summary(transcription_paths, base_path):
    if transcription_paths:
        # Read the transcription content
        with open(transcription_paths[0], "r", encoding="utf-8") as f:
            transcription_content = f.read()

        # Create system prompt
        system_prompt = (
            "You are an AI assistant that summarizes YouTube video transcriptions."
        )
        api_key = os.getenv("OPENAI_API_KEY")  # Use the actual API key from .env

        # Generate summary
        summary = create_completion_ollama(
            system_prompt, transcription_content, api_key
        )

        # Save the summary
        summary_path = os.path.join(
            base_path,
            f"{os.path.basename(transcription_paths[0]).replace('transcription', 'summary')}",
        )
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(summary)

        print_in_color(f"Resumen generado y guardado en {summary_path}", "green")


def chat_with_video(transcription_paths, base_path):
    if transcription_paths:
        # Read the transcription content
        with open(transcription_paths[0], "r", encoding="utf-8") as f:
            transcription_content = f.read()

        # Ask for AI provider
        print_in_color("Selecciona el proveedor de IA:", "blue")
        print_in_color("1. OpenAI\n2. Ollama (local)\n3. Groq", "blue")
        ai_provider = input("Introduce el número del proveedor de IA deseado: ").strip()

        # Set API key based on provider
        if ai_provider == "1":
            api_key = os.getenv("OPENAI_API_KEY")
            create_completion = create_openai_completion
        elif ai_provider == "2":
            api_key = "your_local_ollama_api_key"  # Replace with your actual local Ollama API key
            create_completion = create_completion_ollama
        elif ai_provider == "3":
            api_key = os.getenv("GROQ_API_KEY")
            create_completion = create_groq_completion
        else:
            print_in_color("Proveedor de IA no válido.", "red")
            return

        # Start chat session
        print_in_color("Pregunta lo que quieras sobre el video:", "blue")
        chat_history = []
        chat_file_path = os.path.join(base_path, "chat.txt")
        while True:
            user_question = input("Tú: ")
            if user_question.lower() in ["exit", "salir"]:
                print_in_color("Sesión de chat terminada.", "red")
                break

            # Create system prompt
            system_prompt = "You are an AI assistant that answers questions based on YouTube video transcriptions."

            # Generate response
            context = "\n".join(chat_history[-4:])  # Last 4 messages
            response = create_completion(
                system_prompt,
                f"{transcription_content}\n\n{context}\nPregunta: {user_question}",
                api_key,
            )

            # Update chat history
            chat_history.append(f"Tú: {user_question}")
            chat_history.append(f"AI: {response}")

            # Save chat to file
            with open(chat_file_path, "a", encoding="utf-8") as chat_file:
                chat_file.write("\n\n---------------------\n\n")
                chat_file.write(f"Tú: {user_question}")
                chat_file.write("\n\n---------------------\n\n")
                chat_file.write(f"AI: {response}")

            print_in_color(f"Tú: {user_question}", "grey")
            print_in_color(f"AI: {response}", "green")


def main():
    load_env_variables()

    video_url = get_video_url()
    options = get_user_options()

    output_path = "./output"
    result = download_audio_and_transcript(video_url, options, output_path)

    base_path = result.get("base_path", output_path)

    # Generate summary if the option is selected
    if "generate_summary" in options:
        generate_summary(result.get("transcription_paths", []), base_path)

    # Chat with video if the option is selected
    if "chat_with_video" in options:
        chat_with_video(result.get("transcription_paths", []), base_path)


if __name__ == "__main__":
    main()
