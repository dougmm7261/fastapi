from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/echo")
async def echo(body: dict):
    return {"you_sent": body}
