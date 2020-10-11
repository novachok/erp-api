from typing import List
from abc import ABC, abstractmethod
from google.cloud import firestore
from .entity import AbstractEntity, Order
import logging


class AbstractRepository(ABC):
    COLLECTION_NAME = None

    def __init__(self):
        self.__client = firestore.Client()

    @abstractmethod
    def find(self) -> List[AbstractEntity]:
        pass

    @abstractmethod
    def find_by_id(self, uuid: str) -> AbstractEntity:
        pass

    @abstractmethod
    def save(self, entity: AbstractEntity):
        data = entity.to_dict()
        del(data['uuid'])
        data.update({'updatedAt': firestore.SERVER_TIMESTAMP})
        if not data.get('createdAt', None):
            data.update({'createdAt': firestore.SERVER_TIMESTAMP})

        uuid = entity.uuid

        res = self.__client.collection(self.COLLECTION_NAME).document(uuid).set(data, merge=True)
        return res.transform_results
        logging.info(str(res.transform_results))
        doc_ref = self.__client.collection(self.COLLECTION_NAME).document(uuid)
        doc = doc_ref.get()
        entity.populate(doc.to_dict())
        return entity

    @abstractmethod
    def delete(self, uuid: str):
        pass


class OrderRepository(AbstractRepository):
    COLLECTION_NAME = u'orders'

    def find(self) -> List[Order]:
        pass

    def find_by_id(self, uuid: str) -> Order:
        pass

    def save(self, entity: Order):
        return super().save(entity)

    def delete(self, uuid: str):
        pass
