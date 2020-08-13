from .main import coll_posts


async def insert_post(_id):
    coll_posts.insert_one({
        'post_id': _id,
        'marks': {
            'likes': [],
            'dlikes': []
        },
        'likes': 0,
        'dlikes': 0
    })


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


async def add_mark(c, prev_mark, curr_mark):
    if prev_mark is None:  # no mark
        coll_posts.update_one(
            {'post_id': c.message.message_id},
            {'$addToSet': {f'marks.{curr_mark}': c.from_user.id}}
        )
        await c.answer("Спасибо за оценку")
    elif prev_mark:  # like
        if curr_mark == "likes":
            coll_posts.update_one(
                {'post_id': c.message.message_id},
                {'$pull':  {'marks.likes': c.from_user.id}}
            )
            await c.answer("Оценка снята")
        else:  # curr == dislike
            coll_posts.update_one(
                {'post_id': c.message.message_id},
                {'$pull':  {'marks.likes': c.from_user.id}}
            )
            coll_posts.update_one(
                {'post_id': c.message.message_id},
                {'$addToSet': {f'marks.{curr_mark}': c.from_user.id}}
            )
            await c.answer("Спасибо за оценку")
    else:  # dlike
        if curr_mark == "likes":
            coll_posts.update_one(
                {'post_id': c.message.message_id},
                {'$pull':  {'marks.dlikes': c.from_user.id}}
            )
            coll_posts.update_one(
                {'post_id': c.message.message_id},
                {'$addToSet': {f'marks.{curr_mark}': c.from_user.id}}
            )
            await c.answer("Спасибо за оценку")
        else:
            coll_posts.update_one(
                {'post_id': c.message.message_id},
                {'$pull':  {'marks.dlikes': c.from_user.id}}
            )
            await c.answer("Оценка снята")


async def get_likes(post_id):
    info = coll_posts.find_one({'post_id': post_id})
    final_info = [info['likes'], info['dlikes']]
    return final_info


async def update_likes(post_id, likes, dlikes):
    coll_posts.update_one(
        {'post_id': post_id},
        {'$set': {
            'likes': likes,
            'dlikes': dlikes
        }}
    )
