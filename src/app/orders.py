from typing import Optional
from fastapi import FastAPI, Query
from pydantic import BaseModel

from models import db, get_uid, get_now, FirebaseAdapter, Collection, CollectionMeta


class Order(BaseModel, FirebaseAdapter):
    uid: str = None


app = FastAPI()


@app.get("/")
async def orders_list(
        limit: Optional[int] = Query(10, title="Page size"),
        page: Optional[int] = Query(1, title="Display page")
):
    offset = (page - 1) * limit
    _ref = db.collection("orders").limit(limit).offset(offset)

    return Collection(
        items=[Order.from_firebase(doc) for doc in _ref.stream()],
        meta=CollectionMeta(
            limit=limit,
            page=page
        )
    )


@app.get("/orders/{uid}", response_model=Order)
async def orders_get(uid: str):
    return Order.from_firebase(db.collection("orders").document(uid).get())


@app.post("/orders", response_model=Order, status_code=201)
async def orders_create(item: Order):
    uid = get_uid()
    item.uid = uid
    db.collection("orders").document(uid).set(item.dict(exclude={"id", "uid"}))

    return item


@app.put("/orders/{uid}", response_model=Order)
async def orders_update(uid: str, item: Order):
    item.updated_at = get_now()
    item.uid = uid
    db.collection("orders").document(uid).update(item.dict(exclude={"id", "uid", "created_at"}))

    return item


@app.delete("/orders/{uid}", status_code=204)
async def orders_delete(uid: str):
    db.collection("orders").document(uid).delete()
    return None
