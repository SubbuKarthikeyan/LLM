from sentence_transformers import SentenceTransformer
from app.rag.vectordb import VectorDB


class Retriever:

    def __init__(self):
        # Load the same embedding model used while indexing
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        # Connect to the existing ChromaDB
        self.db = VectorDB()

    def retrieve(self, question, top_k=3):

        print("\nRetriever Started")
        print("Question:", question)

        # Convert the user question into an embedding
        question_embedding = self.model.encode(question)

        print("Embedding Created")

        # Search the vector database
        results = self.db.collection.query(
            query_embeddings=[question_embedding.tolist()],
            n_results=top_k
        )

        print("Query Executed")
        print(results)

        # Return only the retrieved documents
        return results["documents"][0]

