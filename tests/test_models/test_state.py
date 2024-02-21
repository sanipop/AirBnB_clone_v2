#!/usr/bin/python3
"""script to test state """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ method to trst class state"""

    def __init__(self, *args, **kwargs):
        """ test state constructor method"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ name attr test method"""
        new = self.value()
        self.assertEqual(type(new.name), str)
