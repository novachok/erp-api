import json
from flask import make_response
from connexion import NoContent
from lib.repository import OrderRepository
from lib.entity import Order
from lib.encoder import JSONEncoder


def search():
    pass


def post(body):
    try:
        order = Order()
        order.populate(body)

        repository = OrderRepository()
        order = repository.save(order)

        return make_response(
            json.dumps(order, cls=JSONEncoder), 201
        )

    except Exception as e:
        return make_response(
            str(e), 500
        )


def get():
    pass


def put():
    pass


def delete():
    return NoContent, 204
