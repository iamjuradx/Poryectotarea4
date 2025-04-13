from fastapi import FastAPI
from controller.abb_controller import router as pet_router

app = FastAPI()
app.include_router(pet_router)

# Optional: run via `python main.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)