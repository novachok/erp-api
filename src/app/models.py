from datetime import datetime
from uuid import uuid4
from pydantic import BaseModel
from google.cloud import firestore
from google.cloud.firestore_v1.base_document import DocumentSnapshot


db = firestore.Client()


def get_uid():
    return str(uuid4().hex)


def get_now():
    return datetime.utcnow()


class FirebaseAdapter:
    @classmethod
    def from_firebase(cls, obj: DocumentSnapshot):
        _ = obj.to_dict()
        _.update({"uid": obj.id})
        return cls(**_)


class CollectionMeta(BaseModel):
    limit: int = 10
    page: int = 1


class Collection(BaseModel):
    items: list
    meta: CollectionMeta
