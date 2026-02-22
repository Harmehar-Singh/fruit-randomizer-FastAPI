from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import random

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    fruits = ["Apple", "Bannana", "Watermelon"]
    fruit = random.choice(fruits)
    return f"<h1>{fruit}</h1>"

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
