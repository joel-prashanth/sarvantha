from fastapi import FastAPI

app = FastAPI(title = "Sarvantha Auth")

@app.get("/health")
def health():
    return {"status": "ok", "service": "auth"}