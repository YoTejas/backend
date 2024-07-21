from .base import BaseModel
from django.db import models


class Floor(BaseModel):
    floor = models.CharField(max_length=255)
    rank = models.IntegerField(
        help_text="0 for ground floor, 1 for first floor and so on and -1 for basement, -2 for lower basement and so on",
        unique=True
    )

    def __str__(self):
        return f"{self.floor} - {self.rank}"
