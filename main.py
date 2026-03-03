import joblib
from pathlib import Path
from fastapi import FastAPI,HTTPException
import pandas as pd
from models import input_features,prediction

app = FastAPI(title='student exam scores prediction service',version = '0.1.0')
# Путь к модели рядом с main.py — не зависит от того, откуда запущен сервер
_model_dir = Path(__file__).resolve().parent
model_path = _model_dir / 'stud_perf_pipeline.pkl'

try:
    model = joblib.load(str(model_path))
    print(f'model loaded sucessfuly from {model_path}')
except FileNotFoundError:
    print(f'Error: model not found at {model_path}')
    model = None
except Exception as e:
    print(f'error loading model:{e}')
    model = None

@app.get('/')
def read_root():
    '''providing basic api information
    '''
    return {'message':'welcome to student scores prediction api'}
@app.post('/predict',response_model=prediction)
async def predict_perfomance(features:input_features):
    '''predicts the exam scores looking at their lifestlyle
    '''
    if model is None:
        raise HTTPException(status_code=503,detail = 'model is not loaded')
    input_data= pd.DataFrame([features.model_dump()]) 
    try:
        y_pred = model.predict(input_data)
        exam_score = float(y_pred[0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")
    return prediction(exam_score=exam_score)
