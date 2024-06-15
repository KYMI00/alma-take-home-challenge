from fastapi import FastAPI, UploadFile, HTTPException, status, File
from fastapi.responses import JSONResponse
import logging
from assessment import Assesor  # Assuming this is your custom module for scoring

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    return {"message": "Welcome to the CV Scoring API!"}
@app.post("/score-cv/")
async def score_cv(cv_file: UploadFile = File(...)):
    if cv_file.content_type != 'application/pdf':
        logger.error(f"Unsupported file type: {cv_file.content_type}")
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail="Unsupported file format. Please upload a PDF.")
    
    try:
        assessor = Assesor(cv_file)
        await assessor.run_parallel_responses()  # Assuming this processes the PDF and analyzes it
        awards_score, memberships_score = await assessor.calculate_final_score()
        return JSONResponse(content={
            "awards_score": awards_score,
            "memberships_score": memberships_score
        })
    except Exception as e:
        logger.exception("Failed to process CV")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)