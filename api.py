from fastapi import FastAPI
from backend.rag import rag_Agent
from backend.data_models import Prompt

app = FastAPI()

@app.post("/rag/query")
async def query_documentation(query: Prompt):
    result = await rag_Agent.run(query.prompt)

    return result.output