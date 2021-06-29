#!/usr/bin/python3
"""Review test class"""

from models import review
from models.base_model import BaseModel
import unittest
Review = review.Review

class TestReview(unittest.TestCase):
    """Review test class"""
    def testName(self):
        """Teste Review has attributes"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")
