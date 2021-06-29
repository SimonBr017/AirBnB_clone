#!/usr/bin/python3
"""
Test User class
"""
from models import user
from models.base_model import BaseModel
import unittest
User = user.User

class TestUser(unittest.TestCase):
    """Test User class"""
    def testEmail(self):
        """Test User email attributes"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")
        
    def testPassword(self):
        """Test User password attributes"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")
    
    def testFirstName(self):
        """Test User first_name attributes"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")
    
    def testLastName(self):
        """Test User last_name attributes"""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")
