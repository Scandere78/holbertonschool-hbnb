from app.models.base_model import BaseModel


class Amenity(BaseModel):
    def __init__(self, id, name, created_at, updated_at):
        super().__init__(id, created_at, updated_at)
        self.name = name
