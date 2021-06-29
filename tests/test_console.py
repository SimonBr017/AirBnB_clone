#!/usr/bin/python3
"""
    Console Tests Module
"""

import unittest
import os
import sys
from console import HBNBCommand
from io import StringIO
from models import storage
from unittest.mock import patch
import re


class ConsoleTest(unittest.TestCase):
    """
        ConsoleTest Class
    """

    __classes = ['BaseModel', 'User', 'State', 'City',
                 'Amenity', 'Place', 'Review']

    def testHelpEOF(self):
        output = "\n\tEOF command to exit the program\n\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(f.getvalue(), output)

    def testHelpEOF(self):
        output = "\n\tQuit command to exit the program\n\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(f.getvalue(), output)

    def testHelpCreate(self):
        output = "\n\tCreates a new instance of <ClassName>, "\
                 "saves it (to the JSON file) and prints the ID\n\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(f.getvalue(), output)

    def testHelpShow(self):
        output = "\n\tPrints the string representation of an "\
                 "instance based on the className and ID.\n\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(f.getvalue(), output)

    def testHelpAll(self):
        output = "\n\tPrints all string representation of all instances "\
                 "based or not on the className.\n\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(f.getvalue(), output)

    def testHelpDestroy(self):
        output = "\n\tDeletes an instance based on the className and ID.\n\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(f.getvalue(), output)

    def testHelpUpdate(self):
        output = "\n\tUpdates an instance based on the className "\
                 "and ID by adding or updating attribute.\n\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(f.getvalue(), output)

    def testHelpCount(self):
        output = "\n\tRetrieve the number of instances of a class.\n\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
            self.assertEqual(f.getvalue(), output)

    def tearDown(self):
        if os.path.exists("file_storage.json"):
            os.remove("file_storage.json")

    def testPrompt(self):
        self.assertEqual("(hbnb) ",
                         HBNBCommand().prompt)

    def testQuit(self):
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("quit")

    def testEOF(self):
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("EOF")

    def testEmptyLine(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue(), "")

    def testDoCreate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Continent")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        for className in self.__classes:
            self.__createObject(className)

    def __createObject(self, className):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count {}".format(className))
        count = int(f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(className))
        id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count {}".format(className))
        self.assertEqual(f.getvalue(), str(count + 1) + "\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy {} {}".format(className, id))

    def testDoCount(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Continent")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count User")
            self.assertEqual(f.getvalue(), "2\n")

        for className in self.__classes:
            self.__countObjectDot(className)

    def __countObjectDot(self, className):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("{}.count()".format(className))
        count = int(f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(className))
        id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("{}.count()".format(className))
        self.assertEqual(f.getvalue(), str(count + 1) + "\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy {} {}".format(className, id))

    def testDoShow(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Continent")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User ID")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

        for className in self.__classes:
            self.__showObjectDot(className)

    def __showObjectDot(self, className):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(className))
        id = f.getvalue().strip()
        obj = storage.all()["{}.{}".format(className, id)]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("{}.show(\"{}\")".format(className, id))
            self.assertEqual(obj.__str__(), f.getvalue().strip())

    def testDoAll(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Continent")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

            for className in self.__classes:
                self.__allObjectSpace(className)
                self.__allObjectDot(className)

    def __allObjectSpace(self, className):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(className))
        id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all {}".format(className))
            self.assertIn("{}".format(className), f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy {} {}".format(className, id))

    def __allObjectDot(self, className):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(className))
        id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("{}.all()".format(className))
            self.assertIn("{}".format(className), f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy {} {}".format(className, id))

    def testDoDestroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Continent")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User ID")
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        id = self.__getUuid4(f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User {}".format(id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User {}".format(id))
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User {}".format(id))
            self.assertEqual(f.getvalue(), "** no instance found **\n")

        for className in self.__classes:
            self.__destroyObjectDot(className)

    def __destroyObjectDot(self, className):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(className))
        id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("{}.destroy(\"{}\")".format(className, id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User {}".format(id))
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("{}.destroy(\"{}\")".format(className, id))
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def testDoUpdate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Continent")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User ID")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

        for className in self.__classes:
            self.__updateObjectDot(className)

    def __updateObjectDot(self, className):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(className))
        id = f.getvalue().strip()
        obj = storage.all()["{}.{}".format(className, id)]
        attrName = "first_name"
        strValue = "John"
        self.assertNotIn(attrName, obj.__dict__.keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("{}.update(\"{}\", \"{}\", \"{}\")"
                                 .format(className, id, attrName, strValue))
        obj = storage.all()["{}.{}".format(className, id)]
        self.assertIn(attrName, obj.__dict__.keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("{}.show(\"{}\")".format(className, id))
            self.assertEqual(obj.__str__(), f.getvalue().strip())

    def __getUuid4(self, string):
        regex = "([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-"\
                "[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})"
        regex_prog = re.compile(regex)
        res = regex_prog.findall(string)
        return res[0]
