from pydantic import HttpUrl
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


# post request
# define request body schema

class course(BaseModel):
    name: str
    instructor: str
    price: float
    website : HttpUrl



# get request
@app.get('/')
def read_root():
    return {'Name': 'FastApi'}

@app.get("/details")
def aman():
    return {'name':'Aman','age':'30','address':'Dhaka','skills':['Python','FastApi','SQL','Html/Css']}

@app.get("/details/{name}")
def aman(name):
    return {'name': "aman"}

   