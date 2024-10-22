from app.persistence.repository import InMemoryRepository
from app.models.user import User

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()

    def create_user(self, user_data: dict) -> User:
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id: str) -> User:
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email: str) -> User:
        return self.user_repo.get_by_attribute('email', email)
    
    def create_amenity(self, amenity_data):
        # Placeholder for logic to create an amenity
        amenity = Amenity(**amenity_data, id=str(uuid.uuid4()))
        Amenity.validate_request_data(amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
         # Placeholder for logic to retrieve an amenity by ID
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        # Placeholder for logic to retrieve all amenities
        return list(self.amenity_repo.get_all())

    def update_amenity(self, amenity_id, amenity_data):
         # Placeholder for logic to update an amenity
        Amenity.validate_request_data(amenity_data)
        obj = self.get_amenity(amenity_id)
        if obj:
            obj.update(amenity_data)
        return obj
