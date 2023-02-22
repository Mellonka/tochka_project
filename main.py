from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    return HTMLResponse('<h1>Hello world!</h1>')


@app.get("/echo")
async def echo_get(request: Request):
    return request.headers


@app.get("/hello")
async def hello():
    return "Hello"


@app.post("/echo")
async def echo_post(request: Request):
    return await request.json()
