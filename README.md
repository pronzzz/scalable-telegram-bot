# Scalable Telegram Bot

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Telegram](https://img.shields.io/badge/Telegram-Bot%20API-2CA5E0?style=for-the-badge&logo=telegram)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A production-ready, extensible Telegram bot foundation built with `python-telegram-bot`. Designed for scalability, this project goes beyond basic scripts by implementing a clean command routing architecture, stateful conversations, structured logging, and robust error handling.

## 🚀 Features

- **Modular Architecture**: Clean separation of concerns (handlers, state, utils).
- **Stateful Conversations**: Remembers user context across messages (e.g., Onboarding flow).
- **Error Handling**: Graceful failure management and alerting.
- **Health Check**: Built-in `/hello` command for system monitoring.
- **Production Ready**: Configurable environment variables and logging.

## 🛠️ Tech Stack

- **Language**: Python 3.9+
- **Library**: [python-telegram-bot](https://python-telegram-bot.org/) (Async)
- **State Management**: In-memory (extensible to Redis/DB)
- **Config**: `python-dotenv`

## 📂 Project Structure

```bash
bot/
 ├── main.py              # Application entry point
 ├── config.py            # Environment configuration
 ├── handlers/            # Command handlers
 │    ├── start.py        # /start
 │    ├── help.py         # /help
 │    └── hello.py        # /hello (Health check)
 ├── state/               # Conversation state management
 │    └── conversation.py # Onboarding flow
 ├── utils/               # Shared utilities
 │    ├── logger.py       # Structured logging
 │    └── error_handler.py# Global error catching
 └── logs/                # Log storage (optional)
```

## 🏁 Getting Started

### Prerequisites

- Python 3.9 or higher
- A Telegram Bot Token from [@BotFather](https://t.me/BotFather)

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/pronzzz/scalable-telegram-bot.git
    cd scalable-telegram-bot
    ```

2.  **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuration**:
    - Create a `.env` file in the root directory.
    - Add your bot token:
      ```env
      TELEGRAM_BOT_TOKEN=your_token_here
      ENVIRONMENT=development
      ```

### Usage

Run the bot in polling mode:

```bash
python bot/main.py
```

Send `/start` to your bot on Telegram to begin!

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for improvements.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
