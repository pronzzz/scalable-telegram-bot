from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = (
        "Here are the available commands:\n\n"
        "/start - Welcome message\n"
        "/hello - Health check (Hello World)\n"
        "/help - List commands"
    )
    await update.message.reply_text(help_text)
