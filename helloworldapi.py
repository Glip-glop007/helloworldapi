from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def func():
    return {"message":"hello world!"}

# This is just a comment to test something