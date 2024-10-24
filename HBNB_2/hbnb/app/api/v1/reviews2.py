#!/usr/bin/python3
"""Module pour gérer les avis"""

from flask import Flask, request
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

reviews = []

@api.route('/reviews')
class ReviewList(Resource):
    def get(self):
        return reviews, 200

    def post(self):
        review = request.json
        reviews.append(review)
        return review, 201

@api.route('/reviews/<int:review_id>')
class Review(Resource):
    def get(self, review_id):
        review = next((r for r in reviews if r['id'] == review_id), None)
        if review is None:
            return {'error': 'Avis non trouvé'}, 404
        return review, 200

    def put(self, review_id):
        review = next((r for r in reviews if r['id'] == review_id), None)
        if review is None:
            return {'error': 'Avis non trouvé'}, 404
        new_data = request.json
        review.update(new_data)
        return {'message': 'Avis mis à jour'}, 200

    def delete(self, review_id):
        global reviews
        reviews = [r for r in reviews if r['id'] != review_id]
        return {'message': 'Avis supprimé'}, 200

if __name__ == '__main__':
    app.run(debug=True)
