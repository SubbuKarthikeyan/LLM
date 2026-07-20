from app.rag.loader import load_document
from app.rag.chunker import create_chunks
from app.rag.embedder import create_embeddings
from app.rag.vectordb import VectorDB

records = load_document("data/raw/bus_data.csv")
chunks = create_chunks(records)
embeddings = create_embeddings(chunks)

db = VectorDB()

# Delete old collection if it exists
try:
    db.client.delete_collection("bus_routes")
except Exception:
    pass

# Create a new collection
db.collection = db.client.get_or_create_collection(
    name="bus_routes"
)

db.store(chunks, embeddings)

print("Index built successfully.")


