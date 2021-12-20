from fastapi import FastAPI
from google.cloud import firestore


app = FastAPI()
db = firestore.Client()


@app.get("/")
def index():
    customers_ref = db.collection(u'customers')
    docs = customers_ref.stream()

    return [doc.to_dict() for doc in docs]


@app.get("/status")
def get_status():
    return {"status": "Ok"}
