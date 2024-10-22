from app.persistence.repository import InMemoryRepository
from app.models.user import User

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()

    #User Facade
    def create_user(self, user_data: dict) -> User:
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id: str) -> User:
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email: str) -> User:
        return self.user_repo.get_by_attribute('email', email)
    
    def get_all_user(self):
        return list(self.user_repo.get_all())
