from fastapi import FastAPI
from pydantic import BaseModel
import sys
import os
from src.predict import predict_text 
from src.preprocess import clean_text
from src.patterns import detect_patterns

sys.path.append(os.path.abspath("../src"))
from src.predict import predict_text 

app = FastAPI(title="Scam Pattern Detector")

class Request(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message":"Scam detector API running"}

@app.post("/detect")
def detect(req: Request):
    return predict_text(req.text)