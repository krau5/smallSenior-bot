from .main import coll_posts


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


async def calc_likes(c, prev_mark, like, dlike):
    if prev_mark is None:  # no mark
        if c.data == "likes":
            like += 1
        else:
            dlike += 1
    elif not prev_mark:  # previous == dislike
        if c.data == "likes":
            like += 1
            if dlike != 0:
                dlike -= 1
        else:
            if dlike != 0:
                dlike -= 1
    else:  # previous == like
        if c.data == "likes":
            if like != 0:
                like -= 1
        else:
            if like != 0:
                like -= 1
            dlike += 1
    return like, dlike
