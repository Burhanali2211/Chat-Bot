# AI Chatbot using Gemini API

## Description
This is a simple AI-powered chatbot that interacts with users by taking their questions and fetching responses from the Gemini API. The chatbot features a loading animation and a clean user interface.

## Features
- Uses Gemini API for AI-generated responses.
- Loading animation for better user experience.
- CLI-based interactive chatbot.
- Uses `pyfiglet` for a stylish ASCII banner.
- Multi-threading for animation and API requests.

## Requirements
Make sure you have the following installed:
- Python 3.x
- `requests` module
- `pyfiglet` module

You can install missing dependencies using:
```sh
pip install requests pyfiglet
```

## Setup & Usage
1. Clone or download the repository.
2. Open the script and replace `YOUR_GEMINI_API_KEY` with your actual Gemini API key.
3. Run the script using:
   ```sh
   python ai_chat_bot.py
   ```
4. Type your questions and get AI-generated responses.
5. To exit, type `q`.

## API Key Setup
To use the Gemini API, you need an API key from Google AI:
1. Go to [Google AI API Console](https://ai.google.dev/)
2. Generate an API key.
3. Replace `YOUR_GEMINI_API_KEY` in the script.

## Example Usage
```
 _______  _______  _______  _______  _______  _______
|       ||       ||       ||       ||       ||       |
|   _   ||    ___||    ___||    ___||    ___||   _   |
|  | |  ||   |___ |   |___ |   |___ |   |___ |  | |  |
|  |_|  ||    ___||    ___||    ___||    ___||  |_|  |
|       ||   |___ |   |    |   |___ |   |___ |       |
|_______||_______||___|    |_______||_______||_______|

Enter the question to ask:

>>  What is AI?
>>  AI stands for Artificial Intelligence. It refers to the simulation of human intelligence in machines.

>>  q
>>  Bye! Thanks for Using...
```

## License
This project is licensed under the MIT License.
