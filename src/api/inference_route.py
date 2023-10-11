from fastapi import APIRouter

from src.api.schemas import Resume
from src.models.random_forest_model import RandomForestModel
from src.constants import RANDOM_FOREST_PIPELINE_PATH
from src.api.db import Prediction, SessionLocal

model = RandomForestModel()
model.load(RANDOM_FOREST_PIPELINE_PATH)

inference_router = APIRouter()

@inference_router.post("/inference")
def run_inference(resume: Resume):
    prediction = model.predict([resume.text])
    return prediction.tolist()[0]

@inference_router.post("/save")
def run_save(resume: Resume, prediction: str):
    db = SessionLocal()
    db_prediction = Prediction(resume=resume.text, prediction=prediction)
    db.add(db_prediction)
    db.commit()
    predictions = db.query(Prediction).all()
    db.close()
    return predictions