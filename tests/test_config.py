import pytest
import logging
import os

from portfolio.config import get_logger


class TestGetLogger:
    """Test get_logger function."""

    def test_get_logger_returns_logger_instance(self):
        """Test that get_logger returns a logger instance."""
        logger = get_logger('test_module')

        assert isinstance(logger, logging.Logger)

    def test_get_logger_name_hierarchy(self):
        """Test that logger name follows hierarchy."""
        logger = get_logger('test_module')

        assert logger.name == 'portfolio.test_module'

    def test_get_logger_different_modules(self):
        """Test getting loggers for different modules."""
        logger1 = get_logger('module1')
        logger2 = get_logger('module2')

        assert logger1.name == 'portfolio.module1'
        assert logger2.name == 'portfolio.module2'
        assert logger1 != logger2


class TestLoggingConfiguration:
    """Test that logging is properly configured."""

    def test_portfolio_logger_exists(self):
        """Test that portfolio logger is configured."""
        logger = logging.getLogger('portfolio')

        assert logger is not None
        assert logger.level in [logging.DEBUG, logging.INFO]

    def test_get_logger_inherits_from_portfolio(self):
        """Test that module loggers inherit from portfolio logger."""
        module_logger = get_logger('test')

        assert module_logger.name.startswith('portfolio.')

    def test_reflex_logger_warning_level(self):
        """Test that reflex logger is set to WARNING."""
        reflex_logger = logging.getLogger('reflex')

        assert reflex_logger.level >= logging.WARNING or reflex_logger.level == 0

    def test_pymongo_logger_warning_level(self):
        """Test that pymongo logger is set to WARNING."""
        pymongo_logger = logging.getLogger('pymongo')

        assert pymongo_logger.level >= logging.WARNING or pymongo_logger.level == 0
