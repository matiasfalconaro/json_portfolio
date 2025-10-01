#!/usr/bin/env python3
"""
Script to create an admin user for the portfolio application.
Usage: python scripts/create_admin_user.py
"""
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.repository import (create_user,
                                 get_user)
from database.db import init_collections
from portfolio.config import get_logger

logger = get_logger(__name__)


def main():
    """Create an admin user."""
    logger.info("=" * 50)
    logger.info("Portfolio Admin User Creation")
    logger.info("=" * 50)

    logger.info("Initializing database collections...")
    try:
        init_collections()
        logger.info("Database collections initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize database collections: {e}")
        return

    username = input("\nEnter admin username: ").strip()

    if not username:
        logger.error("Username cannot be empty!")
        return

    existing_user = get_user(username)
    if existing_user:
        logger.warning(f"User '{username}' already exists!")
        return

    password = input("Enter admin password: ").strip()

    if not password:
        logger.error("Password cannot be empty!")
        return

    if len(password) < 6:
        logger.error("Password must be at least 6 characters long!")
        return

    password_confirm = input("Confirm password: ").strip()

    if password != password_confirm:
        logger.error("Passwords do not match!")
        return

    logger.info(f"Creating admin user '{username}'...")
    user = create_user(username, password)

    if user:
        logger.info(f"Admin user '{username}' created successfully!")
        logger.info("You can now login with these credentials.")
    else:
        logger.error("Failed to create admin user. Check logs for details.")


if __name__ == "__main__":
    main()
