from communityapp.serializers import BoardLikeSerializer


def save_board_like(user_id, board_id):
    board_like = BoardLikeSerializer(data={
        "user": user_id,
        "board": board_id
    })
    board_like.is_valid(raise_exception=True)
    board_like.save()

    return board_like.data