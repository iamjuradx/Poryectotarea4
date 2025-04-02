from fastapi import FastAPI
from controller.abb_controller import abb_route

app = FastAPI()
app.include_router(abb_route)
