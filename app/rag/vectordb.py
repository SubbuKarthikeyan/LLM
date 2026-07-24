import chromadb


class VectorDB:

    def __init__(self):

        # Open or create the database
        self.client = chromadb.PersistentClient(
            path="data/vector_db"
        )

        # Open or create a collection
        self.collection = self.client.get_or_create_collection(
            name="bus_routes"
        )

    def store(self, chunks, embeddings):

        ids = []

        for i in range(len(chunks)):
            ids.append(str(i))

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings.tolist()
        )

        print(f"{len(chunks)} chunks stored successfully.")

    def get_all(self):

        return self.collection.get(
            include=["documents", "embeddings"]
        )

    def clear(self):
        try:
            self.client.delete_collection("bus_routes")
            self.collection = self.client.get_or_create_collection(
                name="bus_routes"
            )
            print("Collection cleared.")
        except Exception as e:
            print("Failed to clear collection:", e)