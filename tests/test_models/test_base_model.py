#!/usr/bin/python3
""" script for test base model"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import pycodestyle


class test_basemodel(unittest.TestCase):
    """ test class for basemodel"""

    def __init__(self, *args, **kwargs):
        """ constructor of basemodel test"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel
    """
    A class to the pycodestyle"""
    def test_pycodestyle(self):
        """
        method to test pycodestyle format
        """
        pycostyle = pycodestyle.StyleGuide(quiet=True)
        result = pycostyle.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def setUp(self):
        """test method to setup """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ methid to test defult"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ function to test keyword """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """test keyword init """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ method to Test save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ method to test str """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ method to test dict conv"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ method to testnone  keyword """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    # def test_kwargs_one(self):
    #     """ """
    #     n = {'Name': 'test'}
    #     with self.assertRaises(KeyError):
    #         new = self.value(**n)

    def test_id(self):
        """ method to test id"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ method to test created at """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ method to test update"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_uuid(self):
        """
        method of Testin UUID
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        instance3 = BaseModel()
        list_instances = [instance1, instance2,
                          instance3]
        for instance in list_instances:
            ins_uuid = instance.id
            with self.subTest(uuid=ins_uuid):
                self.assertIs(type(ins_uuid), str)
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertNotEqual(instance1.id, instance3.id)
        self.assertNotEqual(instance2.id, instance3.id)

    def test_str_method(self):
        """method to test str"""
        instance6 = BaseModel()
        string_output = "[BaseModel] ({}) {}".format(instance6.id,
                                                     instance6.__dict__)
        self.assertEqual(string_output, str(instance6))


class TestCodeFormat(unittest.TestCase):
    """
    Class to test code format"""
    def test_pycodestyle(self):
        """
        Tester method for codeformat
        """
        pycostyle = pycodestyle.StyleGuide(quiet=True)
        result = pycostyle.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class Test_docstrings(unittest.TestCase):
    """method for Testing docstrings"""
    @classmethod
    def setup_class(self):
        """
        inspect.getmembers(object, [predicate])
        Return all the members of an object in a list of (name, value)
        pairs sorted by name
        only members for which the predicate returns a true value are included
        """
        self.obj_members(BaseModel, inspect.isfunction)


class TestBaseModel(unittest.TestCase):
    """class to test base model"""

    @classmethod
    def setUpClass(cls):
        """method to setup class"""
        cls.base = BaseModel()
        cls.base.name = "Kev"
        cls.base.num = 20

    @classmethod
    def teardown(cls):
        """methid to delete class"""
        del cls.base

    def tearDown(self):
        """method to remove a file"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """pycodestyle methid to test basemodl"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_BaseModel(self):
        """method to test docstring"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """method to test base model method """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """method to test nase model init"""
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_save_BaesModel(self):
        """method to test the save method"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_BaseModel(self):
        """method to test dictionary"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
