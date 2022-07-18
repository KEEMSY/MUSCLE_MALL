from django.test import TestCase

from communityapp.models import BoardCategory, Board
from communityapp.services.board_like_service import save_board_like
from userapp.models import User


class TestBoardLikeTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBoardLikeTest, self).__init__(*args, **kwargs)

        self.board_data = {
            "title": "test_title",
            "content": "test_content",
            "user": None,
            "category": None,
        }

    def make_user(self):
        user = User.objects.create(
            username="test_username1",
            email="test@email.com",
            password="1234",
            fullname="test_fullname",
            gender="male",
            approved_user="True"
        )
        return user

    def make_categories(self):
        notice_category = BoardCategory.objects.create(
            kind="notice",
            description='Notice_desc'
        )

        free_category = BoardCategory.objects.create(
            kind="free",
            description='free_desc'
        )
        return [notice_category, free_category]

    def make_board(self, **data):
        board = Board.objects.create(**data)
        return board

    def test_save_board_like(self):
        # give
        user = self.make_user()
        board_category = self.make_categories()[0]
        self.board_data['user'] = user
        self.board_data['category'] = board_category
        board = self.make_board(**self.board_data)

        # when
        board_like = save_board_like(user.id, board.id)

        # expect
        self.assertEqual(user.id, board_like["user"])
        self.assertEqual(board.id, board_like["board"])