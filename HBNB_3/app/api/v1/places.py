from flask_restx import Namespace, Resource, fields
from app.services.facade import facade
from flask_jwt_extended import jwt_required, get_jwt_identity


api = Namespace('place', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        user_verification = facade.get_user(current_user["id"])
        if user_verification != None and user_verification.is_admin:
            """Register a new place"""
            # Placeholder for the logic to register a new place
            place_data = api.payload
            try:
                new_place = facade.create_place(place_data)
            except ValueError as error:
                return {'error': str(error)}, 400
            return {'id':new_place.id, 'title':new_place.title, 'description':new_place.description, 'price':new_place.price, 'longitude':new_place.longitude, 'owner_id': new_place.owner_id}, 201
        return({"error": "Unauthorized action"}), 403

    @api.response(200, 'List of place retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        # Placeholder for logic to return a list of all places
        list_of_place = facade.get_all_place()
        return [{'id':place.id, 'title':place.title, 'description':place.description, 'price':place.price, 'longitude':place.longitude, 'owner_id': place.owner_id} for place in list_of_place], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        # Placeholder for the logic to retrieve a place by ID, including associated owner and amenities
        place = facade.get_place(place_id)
        if not place:
            return {'error': "ERROR"}, 400
        return {'id':place.id, 'title':place.title, 'description':place.description, 'price':place.price, 'longitude':place.longitude, 'owner_id': place.owner_id}, 201

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')

    @jwt_required()
    def put(self, place_id):
        """Update a place's information"""
        current_user = get_jwt_identity()
        user_verification = facade.get_user(current_user["id"])
        if user_verification != None and user_verification.is_admin:
            # Placeholder for the logic to update a place by ID
            place_data = api.payload
            try:
                updated_place = facade.update_place(place_id, place_data)
            except ValueError as error:
                return {'error': 'Invalid input data'}, 400
            if not updated_place:
                return{'error': 'Place not found'}, 404
            return {'id': place_id}, 200
        return({"error": "Unauthorized action"}), 403