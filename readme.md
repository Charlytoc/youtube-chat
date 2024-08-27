# YouTube Video Assistant

This project provides a set of tools to download audio, video, and transcriptions from YouTube videos. Additionally, it can generate summaries and allow users to chat with the video content using various AI providers.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python**: Make sure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).
- **Git**: Ensure you have Git installed. You can download it from [git-scm.com](https://git-scm.com/downloads).

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Charlytoc/youtube-chat.git
   cd YouTube-Video-Assistant
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Copy the `.env.example` file to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Add your API keys to the `.env` file:
     ```
     OPENAI_API_KEY=your_openai_api_key
     GROQ_API_KEY=your_groq_api_key
     ```

## Usage

1. **Run the script**:

   ```bash
   python main.py
   ```

2. **Follow the prompts**:

   - Enter the YouTube video URL when prompted.
   - Select the desired options by entering the corresponding numbers separated by commas:
     ```
     1. Audio
     2. Video
     3. Transcription
     4. All
     5. Generate Summary
     6. Chat with Video
     ```

3. **Generate Summary**:

   - If you select the "Generate Summary" option, the script will generate a summary of the video's transcription and save it in the output directory.

4. **Chat with Video**:
   - If you select the "Chat with Video" option, you can interact with the video's content by asking questions. The script will use the selected AI provider to generate responses based on the video's transcription.

## Example

Here's an example of how to use the script:

1. Run the script:

   ```bash
   python main.py
   ```

2. Enter the YouTube video URL:

   ```
   Por favor, introduce el enlace del vídeo de YouTube: https://www.youtube.com/watch?v=dQw4w9WgXcQ
   ```

3. Select the desired options:

   ```
   1. Audio
   2. Video
   3. Transcription
   4. All
   5. Generate Summary
   6. Chat with Video
   Introduce los números de las opciones deseadas separados por comas: 4,5,6
   ```

4. Follow the prompts to generate a summary and chat with the video content.

## Contributing

If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
