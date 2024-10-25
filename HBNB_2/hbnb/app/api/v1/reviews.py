from flask_restx import Namespace, Resource, fields
from app.services.facade import facade

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        review_data = api.payload
        new_reviews = facade.create_review(review_data)
        print(facade.review_repo._storage)
        existing_user = facade.get_user(review_data['user_id'])
        if not existing_user:
            return (400, 'Invalid input data')
        return {'id': new_reviews.id, 'text':new_reviews.text, 'rating':new_reviews.rating, 'user_id':existing_user.id, 'place_id':new_reviews.place_id}


    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        _list = []
        list_all_reviews = facade.get_all_reviews()
        print(facade.review_repo._storage, '\n', list_all_reviews)
        for i in list_all_reviews:
            return_all_reviews = {'id': i.id,
                                  'text':i.text, 
                                  'rating':i.rating, 
                                  'user_id':i.id, 
                                  'place_id':i.place_id}
            _list.append(return_all_reviews)
        print(list_all_reviews)
        return _list, 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        # Placeholder for the logic to retrieve a review by ID
        reviews = facade.get_review(review_id)
        if not reviews:
            return {'error': "ERROR"}, 400
        return {'text':reviews.text, 'rating':reviews.rating, 'user_id':reviews.id, 'place_id':reviews.place_id}, 201

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review's information"""
        # Placeholder for the logic to update a review by ID
        review_data = api.payload

        try:
            updated_reviews = facade.update_review(review_data)
        except ValueError as error:
            return {'Invalid input data'}, 400
        
        if not updated_reviews:
            return {'error': 'Review not found' }, 404
        return {"message": 'Review updated successfully'}, 200

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        # Placeholder for the logic to delete a review
        reviews = facade.get_review(review_id)
        if not reviews:
            return {'error': 'Review not found' }, 400
        facade.delete_review(review_id)
        return {"message":"Review deleted successfully"}

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        # Placeholder for logic to return a list of reviews for a place
        pass