import lancedb
from constants import VECTOR_DATABASE_PATH, DATA_PATH
from data_models import Article

def setup_vector_dabase(path):
    vector_db = lancedb.connect(uri=path)
    vector_db.create_table("YouTube", schema=Article, exist_ok=True)

    return vector_db