import os

from pymongo import MongoClient, errors
from dotenv import load_dotenv


load_dotenv()
MONGO_USER = os.getenv("MONGO_USER", "user_placeholder")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "pass_placeholder")
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")
DB_NAME = os.getenv("MONGO_DB", "portfolio_db")
MONGO_URI = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{DB_NAME}?authSource=admin"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]


def _ensure_index(collection, field, unique=False):
    """
    Private helper to create an index if it does not already exist.
    """
    existing_indexes = [idx["key"][0][0] for idx in db[collection].list_indexes()]
    if field not in existing_indexes:
        try:
            db[collection].create_index(field, unique=unique)
            print(f"Index created on '{collection}.{field}', unique={unique}")
        except errors.OperationFailure as e:
            print(f"Failed to create index on '{collection}.{field}': {e}")
    else:
        print(f"Index already exists on '{collection}.{field}'")


def init_collections():
    """
    Initialize all necessary collections and their indexes.
    Can be executed multiple times without errors.
    """
    collections = {
        "basics": [("email", True)],
        "work": [("name", False)],
        "education": [],
        "certificates": [],
        "skills": [],
        "languages": [],
        "interests": [],
        "references": [],
        "projects": [("name", False)]
    }

    for col_name, indexes in collections.items():
        if col_name not in db.list_collection_names():
            db.create_collection(col_name)
            print(f"Collection created: {col_name}")
        else:
            print(f"Collection already exists: {col_name}")

        for field, unique in indexes:
            _ensure_index(col_name, field, unique)

    print("All collections initialized with indexes!")


if __name__ == "__main__":
    init_collections()
