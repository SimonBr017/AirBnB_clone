#!/usr/bin/python3
"""Amenity test class"""

from models import amenity
from models.base_model import BaseModel
import unittest
Amenity = amenity.Amenity


class TestAmenity(unittest.TestCase):
    """Amenity test class"""
    def test_name_attr(self):
        """Test Amenity has attribute"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
