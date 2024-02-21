#!/usr/bin/python3
"""review class test script """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """test script class """

    def __init__(self, *args, **kwargs):
        """ class const method"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ id attr test"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ user id test method"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """method to test text """
        new = self.value()
        self.assertEqual(type(new.text), str)
