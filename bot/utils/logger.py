import logging
import sys

def setup_logger(name: str) -> logging.Logger:
    """
    Sets up a structured logger.
    In production, this could be enhanced to output JSON.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        # Detailed format for debugging
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
