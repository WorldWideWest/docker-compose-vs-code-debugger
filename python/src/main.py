from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_world() -> dict:
    context = {
        "message": "Hello World", 
        "author": "Dzeno",
    }
    return context