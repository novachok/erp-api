from fastapi import FastAPI
from accounts import app as accounts
from customers import app as customers
from orders import app as orders


app = FastAPI()


app.mount("/accounts", accounts)
app.mount("/customers", customers)
app.mount("/orders", orders)


@app.get("/status")
async def get_status():
    return {"status": "Ok"}
