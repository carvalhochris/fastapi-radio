from fastapi import FastAPI
from fastapi.responses import StreamingResponse

one = "one.mp3"
two = "two.mp3"
three = "three.mp3"

app = FastAPI()

def stitcher():
    with open(one, mode="rb") as file_like:
        yield from file_like
    with open(two, mode="rb") as file_like:
        yield from file_like
    with open(three, mode="rb") as file_like:
        yield from file_like

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/station")
async def station():
    stitcher()
    return StreamingResponse(stitcher(), media_type="audio/mp3")
