from flask import Flask
from flask_restful import Resource, Api
from services.utils import read_file
from services.repository import get_movies_data
from services.repository import get_tags_data
from services.repository import get_ratings_data
from services.repository import get_links_data

app = Flask(__name__)
api = Api(app)


class Movies(Resource):
    def get(self):
        return get_movies_data()


class Tags(Resource):
    def get(self):
        return get_tags_data()


class Ratings(Resource):
    def get(self):
        return get_ratings_data()


class Links(Resource):
    def get(self):
        return get_links_data()


api.add_resource(Movies, '/movies')
api.add_resource(Tags, '/tags')
api.add_resource(Ratings, '/ratings')
api.add_resource(Links, '/links')

if __name__ == '__main__':
    app.run(debug=True)
