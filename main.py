import os
import json
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    time: int

app = FastAPI()

@app.get("/")
async def root():
    return "Main Page"

@app.get("/get")
async def root():
    return {"message": "This is GET request"}

@app.post("/post")
async def root():
    return {"message": "This is POST request"}

@app.post("/start")
async def root(item: Item):
    result = dict(item)
    with open('output.json', 'w') as fw:
        json.dump(result, fw)

    result['time'] = str(result['time'])
    return result

@app.post("/background")
async def root():
    with open('output.json', 'r') as fr:
        t = json.load(fr)
    t['time'] = str(t['time'])
    return t