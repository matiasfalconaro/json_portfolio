import logging
import sys
import os

from pathlib import Path


def setup_logging():
    """Configure application logging based on environment."""
    
    env = os.getenv('ENVIRONMENT', 'development')
    
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    logger = logging.getLogger('portfolio')
    
    if env == 'development':
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    
    logger.propagate = False
    
    file_handler = logging.FileHandler(
        log_dir / 'portfolio.log',
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler(sys.stdout)
    if env == 'development':
        console_handler.setLevel(logging.DEBUG)
    else:
        console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    
    logger.handlers.clear()
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    logging.getLogger('reflex').setLevel(logging.WARNING)
    logging.getLogger('pymongo').setLevel(logging.WARNING)
    
    logger.info(f"Logging configured for {env} environment")
    return logger


logger = setup_logging()


def get_logger(name: str) -> logging.Logger:
    """Get a logger for a specific module."""
    return logging.getLogger(f'portfolio.{name}')
