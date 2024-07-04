from fastapi import FastAPI
from services.classify_sentence_service import classify_sentence_naive_bayes, classify_sentence_bert
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "http://localhost:4200",
    "http://127.0.0.1:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/classify/{sentence}")
async def classify_sentence(sentence: str, model: str):
    print(sentence)
    print(model)

    if model == "naive_bayes":
        result = classify_sentence_naive_bayes(sentence)
    else:
        result = classify_sentence_bert(sentence)

    return result
