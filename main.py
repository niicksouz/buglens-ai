from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from pathlib import Path

from dotenv import load_dotenv
from google import genai

from google.genai.errors import ServerError

import joblib

load_dotenv(Path(__file__).parent / ".env")
client = genai.Client()

app = FastAPI(title="BugLens AI")

model_path = Path(__file__).parent / "buglens_model.joblib"
model = joblib.load(model_path)

class BugReport(BaseModel):
    description: str


@app.get("/")
def home():
    return {"message": "BugLens AI está no ar"}



@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/analyze")
def analyze_bug(report: BugReport):
    category = model.predict([report.description])[0]

    try:
        gemini_response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=(
                "Analise este relato de bug e responda em português. "
                "Inclua um resumo, uma hipótese identificada como hipótese "
                "e 3 passos para investigar. Não invente dados ausentes.\n\n"
                f"Relato: {report.description}"
            ),
        )
    except ServerError as erro:
        raise HTTPException(
            status_code=503,
            detail="O Gemini está temporariamente indisponível. Tente novamente em instantes.",
        ) from erro

    return {
        "received": report.description,
        "category": category,
        "investigation": gemini_response.text,
    }