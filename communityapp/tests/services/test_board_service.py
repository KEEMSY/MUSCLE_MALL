from django.test import TestCase

from MM.api_exception import GenericAPIException
from communityapp.models import BoardCategory
from communityapp.services.board_service import get_board_category


class TestBoardCategory(TestCase):
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