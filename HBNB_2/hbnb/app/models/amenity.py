from models import BaseModel


class Amenity(BaseModel):
    def __init__(self, name, created_at, updated_at):
        super.__init__()
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at