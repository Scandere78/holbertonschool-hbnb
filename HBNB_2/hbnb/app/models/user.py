from app.models.base_model import BaseModel
import re

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

        if not (1 <= len(first_name) <= 50):
            raise ValueError("first_name must be between 1 and 50 characters")
        if not (1 <= len(last_name) <= 50):
            raise ValueError("last_name must be between 1 and 50 characters")
        if not self._is_valid_email(email):
            raise ValueError("Invalid email format")

    @staticmethod
    def _is_valid_email(email):
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        return re.match(email_regex, email) is not None