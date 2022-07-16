from fastapi import FastAPI
from database import engine
import models
from routers import main, building_mgmt, facility_mgmt, login, graphql

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(login.router)
app.include_router(main.router)
app.include_router(graphql.router)
app.include_router(building_mgmt.router)
app.include_router(facility_mgmt.router)