from pymongo import MongoClient
from app.config import cluster

client = MongoClient(cluster)
coll_posts = client.db.posts
