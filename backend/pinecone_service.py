import pinecone

pinecone.init(api_key="your-pinecone-key", environment="your-env")
index = pinecone.Index("mlb-vectors")

def upsert_vector(id, vector, metadata):
    index.upsert([(id, vector, metadata)])

