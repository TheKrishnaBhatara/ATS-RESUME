from fastapi import FastAPI, File, UploadFile
from backend.utils import generate_ai_feedback
import PyPDF2

from backend.resume_parser import extract_skills
from backend.embedding_engine import get_embedding
from backend.ranking_engine import (
    calculate_similarity,
    skill_overlap_score,
    final_ranking_score
)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "ATS Resume Screening API Running"}


@app.post("/rank")
def rank_candidate(resume_text: str, jd_text: str):

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    resume_emb = get_embedding(resume_text)
    jd_emb = get_embedding(jd_text)

    similarity = calculate_similarity(resume_emb, jd_emb)
    skill_score = skill_overlap_score(resume_skills, jd_skills)

    final_score = final_ranking_score(similarity, skill_score)

    final_score_percent = round(final_score * 100, 2)
    similarity_percent = round(similarity * 100, 2)
    skill_score_percent = round(skill_score * 100, 2)

    missing_skills = list(set(jd_skills) - set(resume_skills))

    # 🔥 AI FEEDBACK
    ai_feedback = generate_ai_feedback(resume_text, jd_text)

    return {
        "final_score": final_score_percent,
        "similarity": similarity_percent,
        "skill_score": skill_score_percent,
        "missing_skills": missing_skills[:10],
        "ai_feedback": ai_feedback
    }


@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    text = ""

    pdf_reader = PyPDF2.PdfReader(file.file)

    for page in pdf_reader.pages:
        content = page.extract_text()
        if content:
            text += content

    return {"resume_text": text}
