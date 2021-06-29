#!/usr/bin/python3
"""module test classes"""

from models import amenity
from models.base_model import BaseModel
from models import state
import unittest
Amenity = amenity.Amenity
State = state.State


class TestAmenity(unittest.TestCase):
    """Amenity test class"""
    def testName(self):
        """Test Amenity has attribute"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")


class TestState(unittest.TestCase):
    """State test class"""
    def testName(self):
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")
