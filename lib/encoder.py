import json
from abc import ABC, abstractmethod
from .entity import AbstractEntity, Order


class AbstractEncoder(ABC):
    @abstractmethod
    def to_entity(self) -> AbstractEntity:
        pass


class OrderEncoder(json.JSONEncoder):
    def default(self, o: AbstractEntity):
        if isinstance(o, Order):
            return o.to_dict()

        return super().default(o)


class JSONEncoder(OrderEncoder):
    def default(self, o: AbstractEntity):
        for cls in JSONEncoder.__bases__:
            try:
                return cls().default(o)
            except TypeError:
                continue

        raise TypeError(f'Object of type {o.__class__.__name__} is not JSON serializable')
