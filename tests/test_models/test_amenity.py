#!/usr/bin/python3
"""module test classes"""

from models import amenity
from models.base_model import BaseModel
import unittest
Amenity = amenity.Amenity


class TestAmenity(unittest.TestCase):
    """Amenity test class"""
    def testName(self):
        """Test Amenity has attribute"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
