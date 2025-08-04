from fastapi import FastAPI
# from app.api.v1.routers import wine 


app = FastAPI(
    title="Wine Service",
    description="Микросервис для управления каталогом вин, вдохновленный Vivino",
    version="1.0.0"
)

# app.include_router(wine.router, prefix="/api/v1", tags=["wines"])
# app.include_router(search.router, prefix="/api/v1", tags=["search"]) # Закомментируем

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "wine-service"}