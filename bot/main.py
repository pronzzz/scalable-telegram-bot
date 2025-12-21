import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from bot.config import config
from bot.utils.logger import setup_logger
from bot.utils.error_handler import error_handler
from bot.handlers import start_command, help_command, hello_command
from bot.state.conversation import get_conversation_handler

logger = setup_logger(__name__)

def main():
    """
    Main function to start the bot.
    """
    logger.info("Starting bot...")
    
    # Build the application
    application = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()

    # Register Command Handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("hello", hello_command))

    # Register Conversation Handler
    application.add_handler(get_conversation_handler())

    # Register Error Handler
    application.add_error_handler(error_handler)

    # Run the bot
    # In production, you might want to use run_webhook instead of run_polling
    logger.info("Bot is polling...")
    if config.is_production:
        # Placeholder for webhook logic
        logger.warning("Running in production mode but using polling (Update to webhook!)")
        application.run_polling()
    else:
        application.run_polling()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.critical(f"Fatal error: {e}")
