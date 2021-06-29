#!/usr/bin/python3
"""
entry point of the command interpreter.
"""
import os
import time
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
import json


class HBNBCommand(cmd.Cmd):
    """
    interpreter command
    """

    prompt = "(hbnb) "
    __classes = ['BaseModel', 'User', 'State', 'City',
                 'Amenity', 'Place', 'Review']
    __commands = ['create', 'all', 'show', 'destroy', 'count']

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
                print(newInstance.id)
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
            print(new_dict[key])
        except Exception as exception:
            print("{}".format(exception.args[0]))

    def do_all(self, args):
        """
            Prints all string representation of all instances
            based or not on the class name.
        """
        try:
            args_list = args.split()
            new_dict = storage.all()
            obj_list = []

            if args_list and args_list[0] not in self.__classes:
                raise NameError("** class doesn't exist **")

            for key, value in new_dict.items():
                if not args_list or args_list[0] == type(value).__name__:
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
                raise ValueError("** attribute name missing **")
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
            print(count)
        except Exception as exception:
            print("{}".format(exception.args[0]))

    def default(self, line):
        """
            Called when command prefix is not recognized in order
            to verify and catch or not the adequate function.
        """
        try:
            args = self.__get_arguments(line)
            if args and args[0] in self.__classes:
                # arg[0]= className, args[1]=command...
                className, command, arguments = args
                if command in self.__commands:
                    arguments = self.__clean_parameter(arguments)
                    if len(arguments) > 0:
                        arguments = "{} {}".format(className, arguments)
                    else:
                        arguments = "{}".format(className)
                    eval("self.do_{}('{}')".format(command, arguments))
                    return
                elif command == 'update':
                    paramet = self.__get_paramet(arguments)
                    id = self.__clean_parameter(paramet[0])
                    if self.__Verif_json(paramet[1]):
                        modpara = paramet[1].replace("'", '"')
                        for att, value in json.loads(modpara).items():
                            args = "{} {} {}".format(id, att, value)
                            fomtCom = self.__fomtCom(className, command, args)
                            eval(fomtCom)
                        return
                    else:
                        arguments = self.__clean_parameter(arguments)
                        if len(arguments) > 0:
                            arguments = "{} {}".format(className, arguments)
                        else:
                            arguments = "{}".format(className)
                        eval("self.do_{}('{}')".format(command, arguments))
                        return
            elif args and not args[0]:
                print("** class name missing **")
            elif args and args[0] not in self.__classes:
                print("** class doesn't exist **")
        except:
            return super().default(line)

    def __get_arguments(self, line):
        regex = "^(.*)\.(.*)\((.*)\)$"
        regex_prog = re.compile(regex)
        res = regex_prog.findall(line)
        return res[0]

    def __clean_parameter(self, parameter):
        parameter = parameter.replace('"', '')
        parameter = parameter.replace(',', ' ')
        parameter = parameter.replace(', ', ' ')
        return parameter

    def __fomtCom(self, className, comm, arg):
        return "self.do_{}(\"{} {}\")".format(comm, className, arg)

    def __Verif_json(self, paramet):
        paramet = paramet.replace("'", '"')
        try:
            json.loads(paramet)
        except ValueError as e:
            return False
        return True

    def __get_paramet(self, line):
        try:
            rgex = "^\"(.*)\"((,? ?)({.*}))$"
            regex_prog = re.compile(rgex)
            res = regex_prog.findall(line)
            parameters = res[0]
            return parameters[0], parameters[3]
        except:
            return '', ''

    def help_EOF(self):
        print("\n\tEOF command to exit the program\n")

    def help_quit(self):
        print("\n\tQuit command to exit the program\n")

    def help_create(self):
        print("\n\tCreates a new instance of <ClassName>, "
              "saves it (to the JSON file) and prints the ID\n")

    def help_show(self):
        print("\n\tPrints the string representation of an "
              "instance based on the className and ID.\n")

    def help_all(self):
        print("\n\tPrints all string representation of all instances "
              "based or not on the className.\n")

    def help_destroy(self):
        print("\n\tDeletes an instance based on the className and ID.\n")

    def help_update(self):
        print("\n\tUpdates an instance based on the className "
              "and ID by adding or updating attribute.\n")

    def help_count(self):
        print("\n\tRetrieve the number of instances of a class.\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
