#!/usr/bin/python3
"""
entry point of the command interpreter.
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    interpreter command
    """
    prompt = '(hbnb)'
    classe = ['BaseModel']
    
    def do_EOF(self, arg):
        """exit the program"""
        raise SystemExit
    def do_quit(self, arg):
        raise SystemExit
    
    def emptyline(self):
        pass
    
    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
        elif arg not in self.classe:
            print("** class doesn't exist **")
        else:
            newInstance = eval(arg)()
            newInstance.save()
            print(newInstance.id)
                    
    def help_EOF(self):
        print("EOF command to exit the program\n")
    def help_quit(self):
        print("Quit command to exit the program\n")
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
