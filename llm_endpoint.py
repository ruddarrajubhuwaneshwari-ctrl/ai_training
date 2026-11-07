from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, status
from google import genai
from google.genai import types
from pydantic import BaseModel, Field


load_dotenv()
client = genai.Client()

app = FastAPI(title="LLM Extraction microservice")
# From the resume summary available. Extract Name, exp, skills of the employee

class ExtractedResponse(BaseModel):
    name:str
    exp:int 
    skills:list[str]

class ExtractionRequest(BaseModel):
    resume_summary: str 
    temperature: float 

@app.get("/")
def disp():
    return {"greetings" : "Hello! This is a LLM extraction microservice."}


@app.post("/extract", response_model=ExtractedResponse, status_code=status.HTTP_200_OK)
async def extract_info(payload:ExtractionRequest):
    response = await client.aio.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=f"Extract structured details from: {payload.resume_summary}",
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ExtractedResponse,
            temperature=payload.temperature,
        ),
    )
    return ExtractedResponse.model_validate_json(response.text)

