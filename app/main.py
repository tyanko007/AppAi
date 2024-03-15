#coding : utf-8

import fastapi as FastAPI

app = FastAPI()

@api.get("/")
async def root():
    return {"message": "Hello World"}