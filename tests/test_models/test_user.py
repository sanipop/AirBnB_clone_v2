#!/usr/bin/python3
""" script to test user """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ user class tester"""

    def __init__(self, *args, **kwargs):
        """ user class cons tester"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ first name attr tester"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ last name attr tester"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ email attr tester"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ passwors attr name tester"""
        new = self.value()
        self.assertEqual(type(new.password), str)
