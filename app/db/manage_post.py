from typing import NoReturn

from .main import coll_posts


async def insert_post(post_id: int) -> NoReturn:
    coll_posts.insert_one({
        'post_id': post_id,
        'marks': {
            'likes': [],
            'dislikes': []
        },
        'likes': 0,
        'dislikes': 0
    })
