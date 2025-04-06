from fastapi import FastAPI              # ← Import necesario
from controller.abb_controller import abb_route   # o router, según hayas elegido

app = FastAPI()                           # ← FastAPI ya está definido
app.include_router(abb_route)