#!/usr/bin/python3
"""City test class"""
from models import city
from models.base_model import BaseModel
import unittest
City = city.City


class TestCity(unittest.TestCase):
    """City test class"""
    def testName(self):
        """Test city has attribute"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")
