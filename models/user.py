#!/usr/bin/python3
""" class User - this class inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ class User """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
