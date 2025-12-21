from telegram import Update
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    ContextTypes,
    ConversationHandler,
    filters,
)
from bot.utils.logger import setup_logger

logger = setup_logger(__name__)

# Define states
NAME, AGE = range(2)

async def start_conversation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and asks the user for their name."""
    logger.info("Starting conversation with user %s", update.effective_user.id)
    await update.message.reply_text(
        "Let's get to know you! What's your name?\n"
        "Send /cancel to stop talking to me."
    )
    return NAME

async def receive_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the name and asks for age."""
    user = update.effective_user
    name = update.message.text
    context.user_data["name"] = name
    logger.info("User %s name: %s", user.id, name)
    
    await update.message.reply_text(
        f"Nice to meet you, {name}! How old are you?"
    )
    return AGE

async def receive_age(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the age and ends the conversation."""
    user = update.effective_user
    age = update.message.text
    context.user_data["age"] = age
    logger.info("User %s age: %s", user.id, age)
    
    name = context.user_data["name"]
    await update.message.reply_text(
        f"Contents noted! Name: {name}, Age: {age}.\n"
        "Conversation finished."
    )
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.effective_user
    logger.info("User %s canceled the conversation.", user.id)
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.",
    )
    return ConversationHandler.END

def get_conversation_handler():
    """Returns the ConversationHandler object."""
    return ConversationHandler(
        entry_points=[CommandHandler("onboard", start_conversation)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_name)],
            AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_age)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
