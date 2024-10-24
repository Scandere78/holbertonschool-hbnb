from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

facade = HBnBFacade()

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        amenity_data =  api.payload
        # Placeholder for the logic to register a new amenity
        existing_amenity = facade.get_all_amenities()
        for i in existing_amenity:
            if i.name == amenity_data['name']:
                return {'error': f'{amenity_data["name"]} already registered'}, 400
        new_amenity = facade.create_amenity(amenity_data)
        return {'id':new_amenity.id, 'name':new_amenity.name}, 201
    
    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        _list = []
        all_amenity = facade.get_all_amenities()
        for i in all_amenity:
            return_all = {'id':i.id, 'name':i.name}
            _list.append(return_all)
        return _list


@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        amenity = facade.get_amenity(amenity_id)
        return {'name':amenity.name}

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        amenity_data =  api.payload

        facade.update_amenity(amenity_id, amenity_data)
    
        check_amenity = facade.get_amenity(amenity_id)
        if check_amenity:
            return {'name':check_amenity.name}, 201
        return(404, 'Amenity not found')