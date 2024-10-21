from models import BaseModel
from place import Place
from user import User

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = self.validate_text(text)
        self.rating = self.validate_rating(rating)
        self.place = self.validate_place(place)
        self.user = self.validate_user(user)

    def validate_text(self, text):
        if not text or not isinstance(text, str):
            raise ValueError("The review text is required and must be a valid string")
        return text

    def validate_rating(self, rating):
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError("The rating must be a integer between 1 and 5.")
        return rating

    def validate_place(self, place):
        if not isinstance(place, Place):
            raise ValueError("the place must be a valid instance of Place.")
        return place

    def validate_user(self, user):
        if not isinstance(user, User):
            raise ValueError("The user must be a valid instance of User.")
        return user

    
    def update(self, data):
        if 'rating' in data:
            self.rating = self.validate_rating(data['rating'])
        super().update(data)