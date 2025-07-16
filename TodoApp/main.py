from fastapi import FastApi
import models
from  database import engine


app=FastApi(
    
)

models.Base.metadata.create_all(bind=engine)

