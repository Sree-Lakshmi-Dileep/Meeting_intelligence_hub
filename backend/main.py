from fastapi import FastAPI
from analyzer import analyze_transcript

app = FastAPI()


@app.get("/")
def home():
    return {
        "message":"API running"
    }


@app.post("/analyze")
def analyze(text:str):

    result = analyze_transcript(text)

    return result