import os
import pinecone
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Pinecone with API key and environment from .env
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

if not all([PINECONE_API_KEY, PINECONE_ENVIRONMENT, PINECONE_INDEX]):
    raise ValueError("Pinecone configuration is missing. Check your .env file.")

pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)

# Create or connect to the index
if PINECONE_INDEX not in pinecone.list_indexes():
    pinecone.create_index(PINECONE_INDEX, dimension=768)  # Replace 768 with the actual dimension of your vectors
index = pinecone.Index(PINECONE_INDEX)

def upsert_vector(id: str, vector: list, metadata: dict):
    """
    Upsert a vector into the Pinecone index.

    Args:
        id (str): Unique ID for the vector.
        vector (list): Vector embedding (e.g., from an LLM).
        metadata (dict): Additional metadata for the vector.

    Returns:
        dict: Response from the Pinecone upsert operation.
    """
    try:
        response = index.upsert([(id, vector, metadata)])
        return response
    except Exception as e:
        raise RuntimeError(f"Failed to upsert vector: {str(e)}")

