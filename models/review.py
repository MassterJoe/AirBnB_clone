#!/usr/bin/python3
import models
from models.base_model import BaseModel
class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
