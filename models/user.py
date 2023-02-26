#!/usr/bin/python3
import models
from models.base_model import BaseModel
class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
