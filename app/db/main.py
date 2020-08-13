from pymongo import MongoClient
from config import cluster

client = MongoClient(cluster)
coll_posts = client.db.posts
