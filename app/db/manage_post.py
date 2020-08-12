from .main import coll_posts


async def insert_post(_id):
    coll_posts.insert_one({
        'post_id': _id,
        'marks': {
            'likes': [],
            'dlikes': []
        }
    })
