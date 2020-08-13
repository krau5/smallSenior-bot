from .main import coll_posts


async def pull_id(c, _type):
    coll_posts.update_one(
        {'post_id': c.message.message_id},
        {'$pull':  {f'marks.{_type}': c.from_user.id}}
    )


async def push_id(c, _type):
    coll_posts.update_one(
        {'post_id': c.message.message_id},
        {'$addToSet': {f'marks.{_type}': c.from_user.id}}
    )


async def check_id(user_id, post_id):
    found_post = coll_posts.find_one({
        'post_id': post_id
    }, {'_id': 0})

    likes = found_post['marks']['likes']
    dlikes = found_post['marks']['dlikes']

    if (user_id not in likes) and (user_id not in dlikes):
        return None
    elif user_id in likes:
        return 1
    return False
