from fastapi import FastAPI, Request
from pydantic import BaseModel
import pandas as pd
import joblib
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Instancia o FastAPI
app = FastAPI()

print("Carregando o modelo treinado...")
# Carregar o modelo Random Forest treinado
model = joblib.load("./models/random_forest_model.joblib")
print("Modelo carregado com sucesso!")

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# Lista de features esperadas pelo modelo
MODEL_FEATURES = ["likes", "dislikes", "like_dislike_ratio", "comment_count", "views"]

# Classe para validar os dados de entrada
class VideoMetrics(BaseModel):
    views: int
    likes: int
    dislikes: int
    comment_count: int

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict/")
def predict(data: VideoMetrics):
    print("Recebendo dados de entrada...")
    print(data.dict())
    try:
        # Calcula métricas adicionais
        like_dislike_ratio = data.likes / (data.dislikes + 1)  # Evitar divisão por zero

        # Prepara os dados de entrada no formato esperado
        input_data = pd.DataFrame([[
            data.likes,
            data.dislikes,
            like_dislike_ratio,
            data.comment_count,
            data.views
        ]], columns=MODEL_FEATURES)

        print("Fazendo a previsão...")
        print(input_data)

        # Faz a previsão com o modelo Random Forest
        prediction = model.predict(input_data)
        print("prediction", prediction)
        
        # Interpreta a previsão
        result = "Trending" if int(prediction[0]) == 1 else "Não Trending"

        return {
            "result": result,
            "input_data": data.dict(),
            "calculated_metrics": {
                "like_dislike_ratio": like_dislike_ratio
            }
        }
    except Exception as e:
        return {"error": str(e)}
