from django.test import TestCase

from MM.api_exception import GenericAPIException
from communityapp.models import BoardCategory, Board
from communityapp.services.board_service import get_board, save_board
from userapp.models import User


class TestBoardCategoryService(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBoardCategoryService, self).__init__(*args, **kwargs)
        self.board_category_data = {
            "kind": "Free",
            "description": "free_desc"
        }

        self.board_data = {
            "title": "test_title",
            "content": "test_content"
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
            kind="Notice",
            description='Notice_desc'
        )

        free_category = BoardCategory.objects.create(
            kind="free",
            description='free_desc'
        )
        return [notice_category, free_category]

    def test_get_board(self):
        # give
        categorise = self.make_categories()
        user = self.make_user()
        test_board1 = Board.objects.create(
            user=user,
            category=categorise[0],
            title='test_title',
            content='test_content'
        )

        test_board2 = Board.objects.create(
            user=user,
            category=categorise[1],
            title='test_title',
            content='test_content'
        )

        # when
        target_board = get_board(categorise[0].id, test_board1.id)
        target_boards = get_board(categorise[0].id)
        boards = get_board()

        # expect
        self.assertEqual(target_board["title"], 'test_title')
        self.assertEqual(len(target_boards), 1)
        self.assertEqual(len(boards), 2)

    def test_save_board(self):
        # give
        categorise = self.make_categories()
        user = self.make_user()
        board_data = self.board_data
        board_data['user'] = user.id
        board_data['category'] = categorise[0].id

        # when
        board = save_board(**board_data)

        # expect
        self.assertEqual(board['title'], board_data['title'])