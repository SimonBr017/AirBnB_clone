#!/usr/bin/python3
"""
    Review module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        Review class
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
            Constructor Method
        """
        super().__init__(*args, **kwargs)
