# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from ADHD_Summariser import summarize as summarize_adhd
from ASD_Summariser import summarize as summarize_autism
from Dyslexia_Summariser import summarize as summarize_dyslexia
from Anxiety_Summariser import summarize as summarize_anxiety
from General_Summariser import summarize as summarize_general

app = FastAPI()


class SummarizationRequest(BaseModel):
    text: str


@app.post("/summarize/adhd")
async def handle_summarize_adhd(request: SummarizationRequest):
    return {"summary": summarize_adhd(request.text)}


@app.post("/summarize/autism")
async def handle_summarize_autism(request: SummarizationRequest):
    return {"summary": summarize_autism(request.text)}


@app.post("/summarize/dyslexia")
async def handle_summarize_dyslexia(request: SummarizationRequest):
    return {"summary": summarize_dyslexia(request.text)}

"""
@app.post("/summarize/anxiety")
async def handle_summarize_anxiety(request: SummarizationRequest):
    return {"summary": summarize_anxiety(request.text)}

"""


@app.post("/summarize/general")
async def handle_summarize_general(request: SummarizationRequest):
    return {"summary": summarize_general(request.text)}  # New endpoint for general summarization


# CORS Middleware integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)
