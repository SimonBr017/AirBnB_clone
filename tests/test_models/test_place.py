#!/usr/bin/python3
"""Place test class"""

from models import place
from models.base_model import BaseModel
import unittest
Place = place.Place


class TestPlace(unittest.TestCase):
    """Place test class"""
    def tesName(self):
        """Test Place has attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")

    def testCityId(self):
        """Test Place has attr city_id"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")
