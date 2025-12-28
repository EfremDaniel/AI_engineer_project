from pydantic_ai import Agent
from backend.data_models import RagResponse
from backend.constants import VECTOR_DATABASE_PATH
import lancedb

vector_db = lancedb.connect(uri=VECTOR_DATABASE_PATH)

rag_Agent = Agent(
    model="google-gla:gemini-2.5-flash",
    retries=2,
    system_prompt=(
        """
        You are an expert data engineering YouTuber with a friendly, with a little attitude.
        Answer stricly based on the retrived knowledge, but you can mix in your own expertise to make the answer more coherent",
        "never hallucinate. If you don't know the answer, just say you can't answer the users prompt based on your retrieved knowledge",
        "Make sure to answer short and concise, getting to the point directly, max 6 sentences",

        """
    ),
    output_type=RagResponse,

)

@rag_Agent.tool_plain()
def retrive_top_documents(query: str, k=3) -> str:
    """
    Uses vectors search to find the closest k matching documents to the query
    """

    result = vector_db["YouTube"].search(query=query).limit(k).to_list()
    top_results = result[0]

    return f"""
    Filename: {top_results["filename"]},

    Filepath: {top_results["filepath"]},

    Content: {top_results["content"]}        
    
    """
