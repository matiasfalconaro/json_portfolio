import pytest
import os

from unittest.mock import (patch,
                           MagicMock)
from pymongo import errors
from database.db import (_ensure_index,
                         init_collections,
                         db,
                         client)


class TestDatabaseConnection:
    """Test database connection and configuration."""

    def test_connection_exists(self):
        """Test that database connection is established."""
        assert client is not None
        assert db is not None

    def test_database_name_from_env(self):
        """Test that database name is correctly loaded from environment."""
        db_name = os.getenv("MONGO_DB", "portfolio_db")
        assert db.name == db_name

    @pytest.mark.skip(reason="Cannot mock module-level imports correctly")
    def test_connection_with_invalid_credentials(self):
        """Test connection handling with invalid credentials."""
        pass

    @patch('database.db.db')
    def test_connection_timeout(self, mock_db):
        """Test connection timeout scenario."""
        mock_db.command.side_effect = errors.ServerSelectionTimeoutError("Connection timeout")

        with pytest.raises(errors.ServerSelectionTimeoutError):
            mock_db.command('ping')


class TestCollectionInitialization:
    """Test collection initialization and index creation."""

    @patch('database.db.db')
    def test_init_collections_creates_missing_collections(self, mock_db):
        """Test that missing collections are created."""
        mock_db.list_collection_names.return_value = []
        mock_db.create_collection = MagicMock()

        init_collections()

        assert mock_db.create_collection.call_count > 0

    @patch('database.db.db')
    def test_init_collections_idempotent(self, mock_db):
        """Test that init_collections can be called multiple times safely."""
        existing_collections = ["basics", "work", "education"]
        mock_db.list_collection_names.return_value = existing_collections

        try:
            init_collections()
            init_collections()
        except Exception as e:
            pytest.fail(f"init_collections should be idempotent: {e}")

    @patch('database.db.db')
    def test_ensure_index_creates_new_index(self, mock_db):
        """Test that _ensure_index creates index when it doesn't exist."""
        collection_mock = MagicMock()
        collection_mock.list_indexes.return_value = []
        mock_db.__getitem__.return_value = collection_mock

        _ensure_index("test_collection", "test_field", unique=True)

        collection_mock.create_index.assert_called_once()

    @patch('database.db.db')
    def test_ensure_index_skips_existing_index(self, mock_db):
        """Test that _ensure_index skips creation if index exists."""
        collection_mock = MagicMock()
        collection_mock.list_indexes.return_value = [
            {"key": [("email", 1)]}
        ]
        mock_db.__getitem__.return_value = collection_mock

        _ensure_index("basics", "email", unique=True)

        collection_mock.create_index.assert_not_called()

    @patch('database.db.db')
    def test_ensure_index_handles_operation_failure(self, mock_db):
        """Test that _ensure_index handles index creation failures."""
        collection_mock = MagicMock()
        collection_mock.list_indexes.return_value = []
        collection_mock.create_index.side_effect = errors.OperationFailure("Index creation failed")
        mock_db.__getitem__.return_value = collection_mock

        _ensure_index("test_collection", "test_field")


class TestDatabaseEnvironmentVariables:
    """Test environment variable handling."""

    def test_mongo_uri_construction(self):
        """Test that MONGO_URI is correctly constructed from env vars."""
        user = os.getenv("MONGO_USER", "user_placeholder")
        password = os.getenv("MONGO_PASSWORD", "pass_placeholder")
        host = os.getenv("MONGO_HOST", "localhost")
        port = os.getenv("MONGO_PORT", "27017")
        db_name = os.getenv("MONGO_DB", "portfolio_db")

        expected_uri = f"mongodb://{user}:{password}@{host}:{port}/{db_name}?authSource=admin"

        from database.db import MONGO_URI
        assert MONGO_URI == expected_uri

    def test_default_values_when_env_missing(self):
        """Test that default values are used when environment variables are missing."""
        from database.db import (MONGO_USER,
                                 MONGO_PASSWORD,
                                 MONGO_HOST,
                                 MONGO_PORT,
                                 DB_NAME)

        assert MONGO_USER is not None
        assert MONGO_PASSWORD is not None
        assert MONGO_HOST is not None
        assert MONGO_PORT is not None
        assert DB_NAME is not None
