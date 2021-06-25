#!/usr/bin/python3
"""
entry point of the command interpreter.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    interpreter command
    """
    prompt = '(hbnb) '
    classe = ['BaseModel', 'User', 'State', 'City',
              'Amenity', 'Place', 'Review']

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

    def do_show(self, args):
        """
            Prints the string representation of an
            instance based on the class name and id.
        """
        try:
            if not args:
                raise NameError("** class name missing **")

            args_list = args.split()

            if args_list[0] not in self.classe:
                raise NameError("** class doesn't exist **")
            elif len(args_list) == 1:
                raise ValueError("** instance id missing **")

            new_dict = storage.all()
            key = args_list[0] + "." + args_list[1]

            if key not in new_dict:
                raise ValueError("** no instance found **")

            print(new_dict[key])

        except Exception as exception:
            print("{}".format(exception.args[0]))

    def do_all(self, arg):
        """
            Prints all string representation of all instances
            based or not on the class name.
        """
        try:
            if arg is None or arg not in self.classe:
                raise NameError("** class doesn't exist **")
            new_dict = storage.all()
            obj_list = []

            for key, value in new_dict.items():
                if not arg or arg == type(value).__name__:
                    obj_list.append(str(value))

            print(obj_list)
        except Exception as exception:
            print("{}".format(exception.args[0]))

    def do_destroy(self, args):
        """
            Deletes an instance based on the class name
            and id.
        """
        try:
            if not args:
                raise NameError("** class name missing **")

            args_list = args.split()

            if args_list[0] not in self.classe:
                raise NameError("** class doesn't exist **")
            elif len(args_list) == 1:
                raise ValueError("** instance id missing **")

            new_dict = storage.all()
            key = args_list[0] + "." + args_list[1]

            if key not in new_dict:
                raise ValueError("** no instance found **")

            del new_dict[key]
            storage.save()
        except Exception as exception:
            print("{}".format(exception.args[0]))

    def do_update(self, args):
        """
            Updates an instance based on the class name
            and id by adding or updating attribute.
        """
        try:
            if not args:
                raise NameError("** class name missing **")

            args_list = args.split()

            if args_list[0] not in self.classe:
                raise NameError("** class doesn't exist **")
            if len(args_list) == 1:
                raise ValueError("** instance id missing **")

            new_dict = storage.all()
            key = args_list[0] + "." + args_list[1]

            if key not in new_dict:
                raise ValueError("** no instance found **")

            obj = new_dict[key]

            if len(args_list) == 2:
                raise ValueError("** attribute name found **")
            if len(args_list) == 3:
                raise ValueError("** value missing **")

            if args_list[2] not in ("id", "created_at", "updated_at"):
                setattr(obj, args_list[2], args_list[3][1:-1])
                storage.save()

        except Exception as exception:
            print("{}".format(exception.args[0]))

    def help_EOF(self):
        print("EOF command to exit the program\n")

    def help_quit(self):
        print("Quit command to exit the program\n")

    """
    def help_create(self):
        print("Create command to ")
    def help_show(self):
    def help_all(self):
    def help_destroy(self):
    def help_update(self):
    """

if __name__ == '__main__':
    HBNBCommand().cmdloop()
