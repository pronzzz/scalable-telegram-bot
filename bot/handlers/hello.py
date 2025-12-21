from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.logger import setup_logger

logger = setup_logger(__name__)

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responds with 'Hello, World' as a system health check."""
    logger.info("Health check (/hello) triggered.")
    await update.message.reply_text("Hello, World!")
