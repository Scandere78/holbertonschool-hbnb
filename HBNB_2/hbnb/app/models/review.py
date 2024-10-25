from app.models.base_model import BaseModel
from app.models.user import User
from app.models.place import Places


class Review(BaseModel):
    def __init__(self, id, text, rating, place_id, user_id, created_at, updated_at):
        super().__init__(id, created_at, updated_at)
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id

    
        if not text or not isinstance(text, str):
            raise ValueError("The review text is required and must be a valid string")
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError("The rating must be a integer between 1 and 5.")
        if not isinstance(place_id, str):
            raise ValueError("the place must be a valid instance of Place.")
        if not isinstance(user_id, str):
            raise ValueError("The user must be a valid instance of User.")