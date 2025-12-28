import lancedb
from constants import VECTOR_DATABASE_PATH, DATA_PATH
from data_models import TranScript
import time

def setup_vector_dabase(path):
    vector_db = lancedb.connect(uri=path)
    vector_db.create_table("YouTube", schema=TranScript, exist_ok=True)

    return vector_db

def ingest_docs_to_vectordb(table):
    for file in DATA_PATH.glob("*.txt"):
        with open(file, 'r', encoding="utf-8") as f:
            content = f.read()
        
        doc_id = file.stem
        table.delete(f"doc_id ='{doc_id}'")

        table.add([
           {
            "doc_id": doc_id,
            "filepath": str(file),
            "filename": file.stem,
            "content": content
           }
        ])

        print(table.to_pandas()["filename"])
        time.sleep(20)

if __name__ == "__main__":
    vector_db = setup_vector_dabase(VECTOR_DATABASE_PATH)
    ingest_docs_to_vectordb(vector_db["YouTube"])
