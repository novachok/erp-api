from datetime import datetime
from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel, Field

from models import db, FirebaseAdapter, Collection, CollectionMeta


class Currency(Enum):
    UAH = "UAH"
    USD = "USD"
    EUR = "EUR"
    

class Account(BaseModel, FirebaseAdapter):
    uid: str = None
    name: str
    iban: str
    currency: Currency
    is_default: bool = Field(False, alias="isDefault")
    created_at: datetime = Field(datetime.utcnow(), alias="createdAt")
    updated_at: datetime = Field(datetime.utcnow(), alias="updatedAt")


app = FastAPI()


@app.get("/")
async def accounts_list():
    _ref = db.collection("accounts")

    return Collection(
        items=[Account.from_firebase(doc) for doc in _ref.stream()],
        meta=CollectionMeta()
    )
