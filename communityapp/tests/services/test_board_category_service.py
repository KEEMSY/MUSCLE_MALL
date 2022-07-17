from django.test import TestCase

from MM.api_exception import GenericAPIException
from communityapp.models import BoardCategory
from communityapp.services.board_category_service import get_board_category, save_board_category, edit_board_category, \
    delete_board_category


class TestBoardCategoryService(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBoardCategoryService, self).__init__(*args, **kwargs)
        self.board_data = {
            "kind": "free",
            "description": "free_desc"
        }

        self.board_update_data = {
            "kind": "notice",
            "description": "update_desc"
        }

    def make_categories(self):
        notice_category = BoardCategory.objects.create(
            kind="notice",
            description='notice_desc'
        )

        free_category = BoardCategory.objects.create(
            kind="free",
            description='free_desc'
        )
        return [notice_category, free_category]

    def test_get_board_category_when_no_category_id(self):
        # give
        category = self.make_categories()[0]

        # when
        get_category = get_board_category(category.id)

        # expect
        self.assertEqual(category.description, get_category["description"])

    def test_get_board_category_when_category_id_is_existed(self):
        # give
        category = self.make_categories()[0]

        # when
        get_category = get_board_category(category.id)

        # expect
        self.assertEqual(category.description, get_category["description"])

    def test_get_board_when_no_category(self):
        # expect
        with self.assertRaises(GenericAPIException):
            get_board_category(999)

    def test_save_board_category(self):
        # when
        board_category = save_board_category(**self.board_data)

        # expect
        self.assertEqual(board_category["kind"], self.board_data["kind"])

    def test_edit_board_category(self):
        # give
        board_category = self.make_categories()[1].id

        # when
        update_category = edit_board_category(board_category, **self.board_update_data)

        # expect
        self.assertEqual(update_category["kind"], self.board_update_data["kind"])
        self.assertEqual(update_category["description"], self.board_update_data["description"])

    def test_delete_board_category(self):
        # give
        board_category = self.make_categories()[1].id

        # when
        delete_board_category(board_category)

        # expect
        with self.assertRaises(BoardCategory.DoesNotExist):
            BoardCategory.objects.get(id=board_category)