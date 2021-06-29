#!/usr/bin/python3
"""State test class"""
from models.base_model import BaseModel
from models import state
import unittest
State = state.State

class TestState(unittest.TestCase):
    """State test class"""
    def testName(self):
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")
