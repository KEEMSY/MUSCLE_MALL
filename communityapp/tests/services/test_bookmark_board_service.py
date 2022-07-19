from django.test import TestCase

from MM.api_exception import GenericAPIException
from communityapp.models import BoardCategory, Board, BoardBookmark
from communityapp.services.bookmark_board_service import save_board_bookmark, delete_board_bookmark
from userapp.models import User


class TestBoardBookmarkTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBoardBookmarkTest, self).__init__(*args, **kwargs)

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

    def test_save_board_bookmark(self):
        # give
        user = self.make_user()
        board_category = self.make_categories()[0]
        self.board_data['user'] = user
        self.board_data['category'] = board_category
        board = self.make_board(**self.board_data)

        # when
        board_bookmark = save_board_bookmark(user.id, board.id)

        # expect
        self.assertEqual(user.id, board_bookmark["user"])
        self.assertEqual(board.id, board_bookmark["board"])

    def test_save_board_bookmark_only_once(self):
        # give
        user = self.make_user()
        board_category = self.make_categories()[0]
        self.board_data['user'] = user
        self.board_data['category'] = board_category
        board = self.make_board(**self.board_data)

        # when
        board_bookmark = save_board_bookmark(user.id, board.id)

        # expect
        with self.assertRaises(GenericAPIException):
            board_bookmark2 = save_board_bookmark(user.id, board.id)

    def test_save_board_bookmark_when_board_does_not_exist(self):
        # give
        user = self.make_user()
        board_id = 9999

        # expect
        with self.assertRaises(GenericAPIException):
            board_like = save_board_bookmark(user.id, board_id)

    def test_delete_board_bookmark(self):
        # give
        user = self.make_user()
        board_category = self.make_categories()[0]
        self.board_data['user'] = user
        self.board_data['category'] = board_category
        board = self.make_board(**self.board_data)

        board_bookmark = BoardBookmark.objects.create(user=user, board=board)

        # when
        delete_board_bookmark(user.id, board.id)

        # expect
        with self.assertRaises(BoardBookmark.DoesNotExist):
            BoardBookmark.objects.get(id=board_bookmark.id)

    def test_delete_board_bookmark_when_board_does_not_exist(self):
        # give
        user = self.make_user()
        board_id = 9999

        # expect
        with self.assertRaises(GenericAPIException):
            board_like = delete_board_bookmark(user.id, board_id)

    def test_delete_board_bookmark_when_bookmark_does_not_exist(self):
        # give
        user = self.make_user()
        board_category = self.make_categories()[0]
        self.board_data['user'] = user
        self.board_data['category'] = board_category
        board = self.make_board(**self.board_data)

        # expect
        with self.assertRaises(GenericAPIException):
            board_like = delete_board_bookmark(user.id, board.id)