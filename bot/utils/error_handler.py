import html
import json
import traceback
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from bot.utils.logger import setup_logger

logger = setup_logger(__name__)

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a telegram message to notify the developer."""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

    # In a real production bot, we might want to alert admins
    # For now, we just reply to the user if possible
    if isinstance(update, Update) and update.effective_message:
        text = "An internal error occurred. Please try again later."
        await update.effective_message.reply_text(text)
