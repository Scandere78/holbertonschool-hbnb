from app.models.base_model import BaseModel

class Places(BaseModel):

    """
    A class to represent a Place.
    
    Attributes:
    -----------
    title : str
        The title of the place. Required, maximum length of 100 characters.
    description : str
        Detailed description of the place. Optional.
    price : float
        The price per night for the place. Must be a positive value.
    latitude : float
        Latitude coordinate for the place location. Must be within the range of -90.0 to 90.0.
    longitude : float
        Longitude coordinate for the place location. Must be within the range of -180.0 to 180.0.
    owner_id : str
        ID of the user who owns the place.
    created_at : datetime
        Timestamp when the place is created.
    updated_at : datetime
        Timestamp when the place is last updated.
    """
    
    def __init__(self, title:str, description:str, price:float, latitude:float, longitude:float, owner_id:str, place_id:str, id, created_at, updated_at):
        super().__init__(id, created_at, updated_at)
        self.place_id = place_id
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id


        if not (1 <= len(title) <= 100):
            raise ValueError('Title length must be between 1 and 100 characters.')
        if not isinstance(price, float) or price < 0:
            raise ValueError('Price must be a positive float value.')
        if not isinstance(latitude, float) or latitude > 90 or latitude < -90:
            raise ValueError('Latitude must be a float within the range -90.0 to 90.0.')
        if not isinstance(longitude, float) or longitude > 180 or longitude < -180:
            raise ValueError('Longitude must be a float within the range -180.0 to 180.0.')
