# Text-to-Image Telegram Bot

This Telegram bot allows users to generate images based on prompts using an AI model. Users can send prompts to the bot, and it will generate an image corresponding to the prompt and send it back to the user.

## Prerequisites

Before running the bot, ensure you have the following:

- Python 3.x installed on your system
- Telegram API token. You can obtain this by creating a bot on Telegram and obtaining the API token.
- RapidAPI key for accessing the Text-to-Image API. You can obtain this from the RapidAPI website.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/prakhardoneria/stable-diffusion-bot-telegram.git
    ```

2. Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

3. Set the environment variables:

    ```
    export TELEGRAM_API_TOKEN="your_telegram_api_token"
    export RAPIDAPI_KEY="your_rapidapi_key"
    ```

4. Run the bot script:

    ```
    python bot.py
    ```

## Usage

Once the bot is running, users can interact with it by sending messages to the bot on Telegram. The following commands are supported:

- `/start`: Initiates the bot and provides instructions on how to use it.
- `/ai <prompt>`: Generates an image based on the provided prompt. Replace `<prompt>` with your desired text.

Don't forget to subscribe to the Text-to-Image Stable AI API on RapidAPI to unlock advanced features and support the development of the service: [Subscribe here](https://rapidapi.com/yashdoneria/api/text-to-image-stable-ai).

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

Also, consider subscribing to the Text-to-Image Stable AI API on RapidAPI to support the project and gain access to additional features: [Subscribe here](https://rapidapi.com/yashdoneria/api/text-to-image-stable-ai).
