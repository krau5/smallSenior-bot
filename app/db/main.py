from pymongo.collection import Collection
from pymongo import MongoClient
from app.config import settings

client: MongoClient = MongoClient(settings.MONGODB_CONNECTION_STRING)
coll_posts: Collection = client.db.posts
