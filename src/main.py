import os
import sys

from fastapi import FastAPI, Depends

from src.routers.rout_cart import router as router_cart
from src.routers.rout_menu import router as router_menu
from src.routers.rout_orders import router as router_orders
from src.verification_authorization import verify_authentication

sys.path.insert(1, os.path.join(sys.path[0], '..'))


app = FastAPI(
    title="Apps ordering food",
    dependencies=[Depends(verify_authentication)]
)

app.include_router(router_cart)
app.include_router(router_menu)
app.include_router(router_orders)
