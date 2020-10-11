from abc import ABC, abstractmethod


class AbstractEntity(ABC):
    __slots__ = ["uuid"]

    def __init__(self):
        self.uuid = None

    def populate(self, data: dict):
        for k, value in data.items():
            if k in self.__slots__:
                setattr(self, k, value)

    def to_dict(self):
        data = {}

        for k in self.__slots__:
            data.update({k: getattr(self, k, None)})

        return data


class Order(AbstractEntity):
    def __init__(self):
        super().__init__()
        self.__slots__ = super().__slots__ + ['title', 'contact', 'email', 'phone', 'notes', 'createdAt', 'updatedAt']
