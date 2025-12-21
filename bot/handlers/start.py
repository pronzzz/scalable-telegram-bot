from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.logger import setup_logger

logger = setup_logger(__name__)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the command /start is issued."""
    user = update.effective_user
    logger.info(f"User {user.id} started the bot.")
    
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! I am a scalable Python Telegram Bot. "
        "I can help you with simple tasks. Try /help to see what I can do.",
    )
