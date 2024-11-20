from app.models.base_model import BaseModel
import re

class User(BaseModel):
    def __init__(self, first_name, last_name, email, id, created_at, updated_at, password,is_admin=False, ):
        super().__init__(id, created_at, updated_at)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.password = password
        
        
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


    def hash_password(self, password):
        from app import bcrypt
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        from app import bcrypt
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)
