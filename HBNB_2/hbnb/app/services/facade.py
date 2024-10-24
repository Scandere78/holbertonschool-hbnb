from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.review import Review

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
#-------------------------------------------------------------------#
#                           USER                                    #
#-------------------------------------------------------------------#
    def create_user(self, user_data: dict) -> User:
        user = User(**user_data,)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id: str) -> User:
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email: str) -> User:
        return self.user_repo.get_by_attribute('email', email)
    
    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        User.validate_request_data(user_data)
        val = self.get_user(user_id)
        if val:
            val.update(user_data)
        return val


#-------------------------------------------------------------------#
#                           AMENITY                                 #
#-------------------------------------------------------------------#

    def create_amenity(self, amenity_data):
        post_amenity = Amenity(**amenity_data)
        self.amenity_repo.add(post_amenity)
        return post_amenity

    def get_amenity(self, amenity_id:str) -> Amenity:
        return self.amenity_repo.get(amenity_id)
        
    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        return self.amenity_repo.update(amenity_id, amenity_data)
    

#-------------------------------------------------------------------#
#                           review                                  #
#-------------------------------------------------------------------#

    def create_review(self, review_data):
        post_review = Review(**review_data)
        self.review_repo.add(post_review)
        return post_review
        # Placeholder for logic to create a review, including validation for user_id, place_id, and rating


    def get_review(self, review_id):
        return self.amenity_repo.get(review_id)

    def get_all_reviews(self):
        return self.amenity_repo.get_all()

    def get_reviews_by_place(self, place_id):
        # Placeholder for logic to retrieve all reviews for a specific place
        return self.amenity_repo.get(place_id)

    def update_review(self, review_id, review_data):
        # Placeholder for logic to update a review
        return self.amenity_repo.update(review_id, review_data)

    def delete_review(self, review_id):
        # Placeholder for logic to delete a review
        return self.amenity_repo.delete(review_id)

