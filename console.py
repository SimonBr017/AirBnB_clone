#!/usr/bin/python3
"""
entry point of the command interpreter.
"""

import cmd
import models


class HBNBCommand(cmd, Cmd):
    """
    interpreter command
    """
    prompt = '(hbnb)'
    
    def call_EOF(self, arg):
        """exit the program"""
        raise SystemExit
    def call_quit(self, arg):
        raise SystemExit
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
