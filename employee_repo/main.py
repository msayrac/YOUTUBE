from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .routes import employee_routes

app = FastAPI()

#mount the static files directory

app.mount("/static", StaticFiles(directory="./employee_repo/static"), name="static")

# set u templates
templates = Jinja2Templates(directory="./employee_repo/templates")

# include routers
@app.include_router(employee_routes.router)




