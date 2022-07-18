from django.test import TestCase

from communityapp.models import BoardCategory, Board, Comment
from communityapp.services.comment_service import get_comment, save_comment, edit_comment, delete_comment
from userapp.models import User


class TestCommentService(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCommentService, self).__init__(*args, **kwargs)

        self.board_data = {
            "title": "test_title",
            "content": "test_content",
            "user": None,
            "category": None,
        }

        self.comment_data = {
            "user": None,
            "board": None,
            "content": "test_content"
        }

        self.updtate_comment_data = {
            "content": "update_content"
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

    def test_get_comment(self):
        # give
        user = self.make_user()
        board_category = self.make_categories()[0]
        self.board_data['user'] = user
        self.board_data['category'] = board_category
        board = self.make_board(**self.board_data)

        new_comment = Comment.objects.create(
            user=user,
            board=board,
            content='test_content'
        )

        new_comment2 = Comment.objects.create(
            user=user,
            board=board,
            content='test_content'
        )

        info = {
            "board": board.id,
            "comment": new_comment.id
        }

        # when
        expected_comment = get_comment(info)

        info["comment"] = None
        expected_comments = get_comment(info)

        # expect
        self.assertEqual(expected_comment['content'], 'test_content')
        self.assertEqual(len(expected_comments), 2)

    def test_save_comment(self):
        # given
        user = self.make_user()
        board_category = self.make_categories()[0]
        self.board_data['user'] = user
        self.board_data['category'] = board_category
        board = self.make_board(**self.board_data)

        self.comment_data['board'] = board.id
        self.comment_data['user'] = user.id

        # when
        comment = save_comment(**self.comment_data)

        # expect
        self.assertEqual(comment['content'], self.board_data['content'])

    def test_edit_comment(self):
        # give
        user = self.make_user()
        board_category = self.make_categories()[0]
        self.board_data['user'] = user
        self.board_data['category'] = board_category
        board = Board.objects.create(**self.board_data)

        self.comment_data['board'] = board
        self.comment_data['user'] = user
        comment = Comment.objects.create(**self.comment_data)

        self.updtate_comment_data['user'] = user.id
        self.updtate_comment_data['board'] = board.id

        # when
        update_comment = edit_comment(**self.updtate_comment_data)

        # expect
        self.assertEqual(update_comment['content'], self.updtate_comment_data['content'])

    def test_delete_comment(self):
        # give
        user = self.make_user()
        board_category = self.make_categories()[0]
        self.board_data['user'] = user
        self.board_data['category'] = board_category
        board = Board.objects.create(**self.board_data)

        self.comment_data['board'] = board
        self.comment_data['user'] = user
        comment = Comment.objects.create(**self.comment_data)

        # when
        delete_comment(comment.id)

        # expect
        with self.assertRaises(Comment.DoesNotExist):
            Comment.objects.get(board_id=self.comment_data['board'], user_id=self.comment_data['user'])