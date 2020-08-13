from .manage_id import push_id, pull_id


async def add_mark(c, prev_mark, curr_mark):
    if prev_mark is None:  # no previous mark
        await c.answer("Спасибо за оценку")
        await push_id(c, curr_mark)
    elif prev_mark:  # prev_mark == like
        if curr_mark == "likes":
            await c.answer("Оценка снята")
            await pull_id(c, 'likes')
        else:  # curr_mark == dislike
            await c.answer("Спасибо за оценку")
            await pull_id(c, 'likes')
            await push_id(c, curr_mark)
    else:  # curr_mark == like
        if curr_mark == "likes":
            await c.answer("Спасибо за оценку")
            await pull_id(c, 'dlikes')
            await push_id(c, curr_mark)
        else:
            await c.answer("Оценка снята")
            await pull_id(c, 'dlikes')
