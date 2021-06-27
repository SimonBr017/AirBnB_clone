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
from colorama import Fore, Style
import re


class ConsoleTest(unittest.TestCase):
    """
        ConsoleTest Class
    """

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

    def createConsole(self):
        return HBNBCommand()

    def testPrompt(self):
        self.assertEqual(f'{Fore.RED}(hbnb) {Style.RESET_ALL}', 
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
        self.assertEqual(len(storage.all()), 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        self.assertEqual(len(storage.all()), 1)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        self.assertEqual(len(storage.all()), 2)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        self.assertEqual(len(storage.all()), 3)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
        self.assertEqual(len(storage.all()), 4)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        self.assertEqual(len(storage.all()), 5)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        self.assertEqual(len(storage.all()), 6)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        self.assertEqual(len(storage.all()), 7)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Review")
            self.assertEqual(f.getvalue(), f"{Fore.GREEN}1{Style.RESET_ALL}\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        self.assertEqual(len(storage.all()), 8)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Review")
            self.assertEqual(f.getvalue(), f"{Fore.GREEN}2{Style.RESET_ALL}\n")

    def testDoCount(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Continent")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count User")
            self.assertEqual(f.getvalue(), f"{Fore.GREEN}0{Style.RESET_ALL}\n")
    
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

    def testDoAll(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Continent")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
    
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

    def __getUuid4(self, string):
        regex = "([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-"\
                "[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})"
        regex_prog = re.compile(regex)
        res = regex_prog.findall(string)
        return res[0]