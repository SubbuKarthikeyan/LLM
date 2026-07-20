import os
import pandas as pd
from pypdf import PdfReader


def load_document(file_path: str):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".csv":
        return load_csv(file_path)

    elif extension == ".pdf":
        return load_pdf(file_path)

    elif extension == ".txt":
        return load_txt(file_path)

    else:
        raise ValueError(f"Unsupported file type: {extension}")


def load_csv(file_path: str):

    df = pd.read_csv(file_path)

    return df.to_dict(orient="records")


def load_pdf(file_path: str):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


def load_txt(file_path: str):

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


