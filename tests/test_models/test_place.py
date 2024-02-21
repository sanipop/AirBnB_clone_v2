#!/usr/bin/python3
""" script to test class place"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """tester method for olace """

    def __init__(self, *args, **kwargs):
        """ constructor for place"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ tester for city id prop """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ method to test user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ name method tester"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ test descriptor method"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ num room attr tester"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ nub bath tester attr"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ limit guest test method"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ test night price"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ test pos(lat) """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ test pos(lat) """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ amenity id test method """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
