#!/usr/bin/python3
"""
entry point of the command interpreter.
"""
import time
from colorama import Fore, Style
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """
    interpreter command
    """

    print(f"{Fore.GREEN}{Style.BRIGHT} ____        ____    ____                                 ____{Style.RESET_ALL}")
    print(f"{Fore.GREEN}|    |      |    |  |    |                               |    |{Style.RESET_ALL}")
    print(f"{Fore.GREEN}|    |      |    |  |    |                               |    |{Style.RESET_ALL}")
    print(f"{Fore.GREEN}|    |      |    |  |    |             {Style.BRIGHT}___{Style.RESET_ALL}{Fore.GREEN}               |    |{Style.RESET_ALL}")
    print(f"{Fore.GREEN}|    |______|    |  |    |            |   | _______      |    |{Style.RESET_ALL}")
    print(f"{Fore.GREEN}|                |  |    |_______     |   |/       \     |    |_______{Style.RESET_ALL}")
    print(f"{Fore.GREEN}|     _______    |  |            \    |      ___    \    |            \ {Style.RESET_ALL}")
    print(f"{Fore.GREEN}|    |      |    |  |      __     \   |     /   \    \   |      __     \ {Style.RESET_ALL}")
    print(f"{Fore.GREEN}|    |      |    |  |     /  \     |  |    |     |    |  |     /  \     |{Style.RESET_ALL}")
    print(f"{Fore.GREEN}|    |      |    |  |     \__/     |  |    |     |    |  |     \__/     |{Style.RESET_ALL}")
    print(f"{Fore.GREEN}|    |      |    |  |             /   |    |     |    |  |             /{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{Style.BRIGHT}|____|      |____|  |____________/    |____|     |____|  |____________/{Style.RESET_ALL}")
    print("\n\n")
    print(f"{Fore.GREEN} *********************************************************************{Style.RESET_ALL}")
    print("                        AirBnB_clone project")
    print("                          The Console V1.0")
    print("                     An Holberton School Project")
    print(f"{Fore.GREEN}{Style.BRIGHT} *********************************************************************{Style.RESET_ALL}")
    time.sleep(1.5)
    print("                                  By:")
    time.sleep(1)
    print(f"{Style.BRIGHT} Nathan LAPEYRE (aka Pebkak)                               Simon BRARD{Style.RESET_ALL}")
    time.sleep(0.5)
    print(f"{Fore.GREEN} *********************************************************************{Style.RESET_ALL}")
    print("                                 2021")
    time.sleep(1)
    print("\n\n")

    prompt = f'{Fore.RED}(hbnb) {Style.RESET_ALL}'
    __classes = ['BaseModel', 'User', 'State', 'City',
                 'Amenity', 'Place', 'Review']
    __commands = ['create', 'all', 'show', 'destroy', 'count', 'update']

    def do_EOF(self, arg):
        """exit the program"""
        raise SystemExit

    def do_quit(self, arg):
        raise SystemExit

    def emptyline(self):
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        try:
            if not args:
                raise NameError("** class name missing **")

            args_list = args.split()

            if args_list[0] not in self.__classes:
                raise NameError("** class doesn't exist **")
            else:
                newInstance = eval(args_list[0])()
                newInstance.save()
                print(f"{Fore.GREEN}", end="")
                print(newInstance.id, end='')
                print(f"{Style.RESET_ALL}")
        except Exception as exception:
            print("{}".format(exception.args[0]))

    def do_show(self, args):
        """
            Prints the string representation of an
            instance based on the class name and id.
        """
        try:
            if not args:
                raise NameError("** class name missing **")

            args_list = args.split()

            if args_list[0] not in self.__classes:
                raise NameError("** class doesn't exist **")
            elif len(args_list) == 1:
                raise ValueError("** instance id missing **")

            new_dict = storage.all()
            key = args_list[0] + "." + args_list[1]

            if key not in new_dict:
                raise ValueError("** no instance found **")
            print(f"{Fore.BLUE}", end="")
            print(new_dict[key], end="")
            print(f"{Style.RESET_ALL}")
        except Exception as exception:
            print("{}".format(exception.args[0]))

    def do_all(self, args):
        """
            Prints all string representation of all instances
            based or not on the class name.
        """
        try:
            args_list = args.split()

            if args_list[0] not in self.__classes:
                raise NameError("** class doesn't exist **")
            new_dict = storage.all()
            obj_list = []

            for key, value in new_dict.items():
                if not args_list[0] or args_list[0] == type(value).__name__:
                    obj_list.append(str(value))
            print(f"{Fore.BLUE}", end="")
            print(obj_list, end="")
            print(f"{Style.RESET_ALL}")
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

            if args_list[0] not in self.__classes:
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

            if args_list[0] not in self.__classes:
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
            if args_list[3][0] != '"':
                args_list[3] = '"' + args_list[3]
            if args_list[3][-1] != '"':
                args_list[3] = args_list[3] + '"'

            if args_list[2] not in ("id", "created_at", "updated_at"):
                setattr(obj, args_list[2], args_list[3][1:-1])
                storage.save()

        except Exception as exception:
            print("{}".format(exception.args[0]))

    def do_count(self, args):
        """
            Retrieve the number of instances of
            a class.
        """
        try:
            count = 0
            if not args:
                raise NameError("** class name missing **")

            args_list = args.split()

            if args_list[0] not in self.__classes:
                raise NameError("** class doesn't exist **")

            new_dict = storage.all()

            for key, value in new_dict.items():
                if not args_list[0] or args_list[0] == type(value).__name__:
                    count += 1
            print(f"{Fore.GREEN}", end="")
            print(count, end="")
            print(f"{Style.RESET_ALL}")
        except Exception as exception:
            print("{}".format(exception.args[0]))

    def default(self, line):
        """
            Called when command prefix is not recognized in order
            to verify and catch or not the adequate function.
        """
        try:
            regex = "^(.*)\.(.*)\((.*)\)$"
            regex_prog = re.compile(regex)
            res = regex_prog.findall(line)
            args = res[0]
            if args and args[0] in self.__classes and len(args) == 3:
                # arg[0]= className, args[1]=command...
                className, command, arguments = args
                if command in self.__commands:
                    arguments = arguments.replace('"', '')
                    arguments = arguments.replace(',', ' ')
                    arguments = arguments.replace(', ', ' ')
                    if len(arguments) > 0:
                        arguments = "{} {}".format(className, arguments)
                    else:
                        arguments ="{}".format(className)
                        
                    print("self.do_{}({})".format(command, arguments))
                    eval("self.do_{}('{}')".format(command, arguments))
                    return

        except:
            return super().default(line)

    def help_EOF(self):
        print(f"{Fore.BLUE}EOF command to exit the program{Style.RESET_ALL}\n")

    def help_quit(self):
        print(f"{Fore.BLUE}Quit command to exit the program{Style.RESET_ALL}\n")

    """
    def help_create(self):
        print("Create command to ")
    def help_show(self):
    def help_all(self):
    def help_destroy(self):
    def help_update(self):
    def help_count(self):
    """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
