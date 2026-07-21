from fastapi import FastAPI

app = FastAPI(title="three-tier-backend")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
