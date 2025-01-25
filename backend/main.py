from fastapi import FastAPI
from app.routes import mlb_routes, llm_routes, pinecone_routes

app = FastAPI()

app.include_router(mlb_routes.router, prefix="/api/mlb", tags=["MLB"])
app.include_router(llm_routes.router, prefix="/api/llm", tags=["LLM"])
app.include_router(pinecone_routes.router, prefix="/api/pinecone", tags=["Pinecone"])

@app.get("/")
def root():
    return {"message": "Welcome to the MLB Fan Engagement API"}
