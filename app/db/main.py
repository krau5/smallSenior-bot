from pymongo import MongoClient
from app.config import settings

client = MongoClient(settings.MONGODB_CONNECTION_STRING)
coll_posts = client.db.posts
