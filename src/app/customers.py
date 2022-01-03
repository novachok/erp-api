from datetime import datetime
from typing import Optional
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

from models import db, get_uid, get_now, FirebaseAdapter, Collection, CollectionMeta


class Customer(BaseModel, FirebaseAdapter):
    uid: str = None
    name: str
    phone: str = None
    notes: str = None
    contact: str = None
    email: str = None
    created_at: datetime = Field(default_factory=get_now, alias="createdAt")
    updated_at: datetime = Field(default_factory=get_now, alias="updatedAt")


app = FastAPI()


@app.get("/")
async def customers_list(
        limit: Optional[int] = Query(10, title="Page size"),
        page: Optional[int] = Query(1, title="Display page")
):
    offset = (page - 1) * limit
    _ref = db.collection("customers").limit(limit).offset(offset)

    return Collection(
        items=[Customer.from_firebase(doc) for doc in _ref.stream()],
        meta=CollectionMeta(
            limit=limit,
            page=page
        )
    )


@app.post("/", response_model=Customer, status_code=201)
async def customers_create(item: Customer):
    uid = get_uid()
    item.uid = uid
    db.collection("customers").document(uid).set(item.dict(exclude={"id", "uid"}))

    return item


@app.put("/{uid}", response_model=Customer)
async def customers_update(uid: str, item: Customer):
    item.updated_at = get_now()
    item.uid = uid
    db.collection("customers").document(uid).update(item.dict(exclude={"id", "uid", "created_at"}))

    return item


@app.get("/{uid}", response_model=Customer)
async def customers_get(uid: str):
    return Customer.from_firebase(db.collection("customers").document(uid).get())


@app.delete("/{uid}", status_code=204)
async def customers_delete(uid: str):
    db.collection("customers").document(uid).delete()
    return None
