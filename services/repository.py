from services.utils import read_file
from models.Movie import Movie
from models.Tag import Tag
from models.Rating import Rating
from models.Link import Link


def get_movies_data():
    movies = []
    file = read_file("data/movies.csv")
    for row in file:
        movies.append(Movie(row[0], row[1], row[2]).__dict__)
    return movies


def get_tags_data():
    tags = []
    file = read_file("data/tags.csv")
    for row in file:
        tags.append(Tag(row[0], row[1], row[2], row[3]).__dict__)
    return tags


def get_ratings_data():
    ratings = []
    file = read_file("data/ratings.csv")
    for row in file:
        ratings.append(Rating(row[0], row[1], row[2], row[3]).__dict__)
    return ratings


def get_links_data():
    links = []
    file = read_file("data/links.csv")
    for row in file:
        links.append(Link(row[0], row[1], row[2]).__dict__)
    return links
