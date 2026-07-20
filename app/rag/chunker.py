def create_chunks(records):
    chunks = []

    for record in records:
        chunk = ""

        for key, value in record.items():
            chunk += f"{key}: {value}\n"

        chunks.append(chunk.strip())

    return chunks



    