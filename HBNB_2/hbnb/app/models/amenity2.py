from app.models.base_model import BaseModel
from app.models.base_model import User
from app.models.base_model import Places

class Amenity(BaseModel):
    def __init__(self, name):
        super.__init__()
        self.name = name

        if len(name) > 50:
            raise ValueError("The equipment name cannot exceed 50 characters.")
