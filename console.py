#!/usr/bin/python3
"""
entry point of the command interpreter.
"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """
    interpreter command
    """
    prompt = '(hbnb)'
    
    def do_EOF(self, arg):
        """exit the program"""
        raise SystemExit
    def do_quit(self, arg):
        raise SystemExit
    
    def emptyline(self):
        pass
    
    def help_EOF(self):
        print("EOF command to exit the program\n")
    def help_quit(self):
        print("Quit command to exit the program\n")
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
