#!/usr/bin/python3
"""
entry point of the command interpreter.
"""
import os
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
import json


class HBNBCommand(cmd.Cmd):
    """
    interpreter command
    """

    print(f"{Fore.GREEN}{Style.BRIGHT} ____        ____    ____                                 ____{Style.RESET_ALL}")
    time.sleep(0.1)
    print(f"{Fore.GREEN}|    |      |    |  |    |                               |    |{Style.RESET_ALL}")
    time.sleep(0.1)
    print(f"{Fore.GREEN}|    |      |    |  |    |                               |    |{Style.RESET_ALL}")
    time.sleep(0.1)
    print(f"{Fore.GREEN}|    |      |    |  |    |             {Style.BRIGHT}___{Style.RESET_ALL}{Fore.GREEN}               |    |{Style.RESET_ALL}")
    time.sleep(0.1)
    print(f"{Fore.GREEN}|    |______|    |  |    |            |   | _______      |    |{Style.RESET_ALL}")
    time.sleep(0.1)
    print(f"{Fore.GREEN}|                |  |    |_______     |   |/       \     |    |_______{Style.RESET_ALL}")
    time.sleep(0.1)
    print(f"{Fore.GREEN}|     _______    |  |            \    |      ___    \    |            \ {Style.RESET_ALL}")
    time.sleep(0.1)
    print(f"{Fore.GREEN}|    |      |    |  |      __     \   |     /   \    \   |      __     \ {Style.RESET_ALL}")
    time.sleep(0.1)
    print(f"{Fore.GREEN}|    |      |    |  |     /  \     |  |    |     |    |  |     /  \     |{Style.RESET_ALL}")
    time.sleep(0.1)
    print(f"{Fore.GREEN}|    |      |    |  |     \__/     |  |    |     |    |  |     \__/     |{Style.RESET_ALL}")
    time.sleep(0.1)
    print(f"{Fore.GREEN}|    |      |    |  |             /   |    |     |    |  |             /{Style.RESET_ALL}")
    time.sleep(0.1)
    print(f"{Fore.GREEN}{Style.BRIGHT}|____|      |____|  |____________/    |____|     |____|  |____________/{Style.RESET_ALL}")
    time.sleep(1.5)
    print("\n\n")
    print(f"{Fore.GREEN} *********************************************************************{Style.RESET_ALL}")
    print("                        AirBnB_clone project")
    print("                          The Console V1.0")
    print("                     An Holberton School Project")
    print(f"{Fore.GREEN}{Style.BRIGHT} *********************************************************************{Style.RESET_ALL}")
    print("                                  By:")
    print(f"{Style.BRIGHT} Nathan LAPEYRE (aka Pebkak)                               Simon BRARD{Style.RESET_ALL}")
    print(f"{Fore.GREEN} *********************************************************************{Style.RESET_ALL}")
    print("                                 2021")
    print("\n\n")

    prompt = f'{Fore.RED}(hbnb) {Style.RESET_ALL}'
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
    
    def do_super(self, arg):
        """
        play super mario theme
        """
        print(f"{Fore.RED}\n")
        print ("                   yyyyyyyyy")
        time.sleep(0.1)
        print ("                 yy         yyy ")
        time.sleep(0.1)
        print ("              yyy   yyyyyyyy   yyy ")
        time.sleep(0.1)
        print ("            yyy   yy       yy    yy ")
        time.sleep(0.1)
        print ("          yyy     y MMM MMM y      yy ")
        time.sleep(0.1)
        print ("        yyy      y  MMMMMMM  y       y ")
        time.sleep(0.1)
        print ("       yyy     yyy  MM M MM  y       yy ")
        time.sleep(0.1)
        print ("     yyy      yyyy  MM M MM y  yyy     y ")
        time.sleep(0.1)
        print ("    yy      yyyyyyy MM   MM y  yyyyyy   y ")
        time.sleep(0.1)
        print ("   yy     yyyyy   y         y    yyyyyy  yy ")
        time.sleep(0.1)
        print ("  y      yyyyyy    yyyyyyyyy      yyyyy   y ")
        time.sleep(0.1)
        print (" y      yyy      @@@ yyyyyy @@@     yyyy   y ")
        time.sleep(0.1)
        print (" y   yyyyy      @   @      @   @    yyyyyy  y ")
        time.sleep(0.1)       
        print ("  yyyyy         @ OO @    @ OO @     yyyyyyy ")
        time.sleep(0.1)
        print ("  @@            @ O  @    @  O @      yy @@ ")
        time.sleep(0.1)
        print (" @  @            @  ********  @         @  @ ")
        time.sleep(0.1)
        print ("@    @            @*        *@         @    @ ")
        time.sleep(0.1)
        print ("@  @ @            *          *         @ @  @ ")
        time.sleep(0.1)
        print ("@  @@@    ####    *          *   ###   @@@  @ ")
        time.sleep(0.1)
        print (" @   @     #####   *        *  ####    @   @ ")
        time.sleep(0.1)
        print (" @@          ###### *      * ######       @@ ")
        time.sleep(0.1)
        print ("  @@@        #######********######       @@ ")
        time.sleep(0.1)
        print ("    @@@       ##################     @@@@ ")
        time.sleep(0.1)
        print ("      @@          ############         @@ ")
        time.sleep(0.1)
        print ("        @@           AAAAAA          @@ ")
        time.sleep(0.1)
        print ("         @@         AAAAAAAA        @@ ")
        time.sleep(0.1)
        print ("           @@@       AAAAAA      @@@ ")
        time.sleep(0.1)
        print ("              @@      AAAA      @@ ")
        time.sleep(0.1)
        print ("                @@            @@ ")
        time.sleep(0.1)
        print ("                 @@@@@@@@@@@@@ ")
        time.sleep(0.1)
        print(f"{Style.RESET_ALL}\n")
        self.__Beep(480,200)
        self.__Beep(1568,200)
        self.__Beep(1568,200)
        self.__Beep(1568,200)
        self.__Beep(740,200)
        self.__Beep(784,200)
        self.__Beep(784,200)
        self.__Beep(784,200)
        self.__Beep(370,200)
        self.__Beep(392,200)
        self.__Beep(370,200)
        self.__Beep(392,200)
        self.__Beep(392,400)
        self.__Beep(196,400)
        self.__Beep(740,200)
        self.__Beep(784,200)
        self.__Beep(784,200)
        self.__Beep(740,200)
        self.__Beep(784,200)
        self.__Beep(784,200)
        self.__Beep(740,200)
        self.__Beep(84,200)
        self.__Beep(880,200)
        self.__Beep(831,200)
        self.__Beep(880,200)
        self.__Beep(988,400)
        self.__Beep(880,200)
        self.__Beep(784,200)
        self.__Beep(699,200)
        self.__Beep(740,200)
        self.__Beep(784,200)
        self.__Beep(784,200)
        self.__Beep(740,200)
        self.__Beep(784,200)
        self.__Beep(784,200)
        self.__Beep(740,200)
        self.__Beep(784,200)
        self.__Beep(880,200)
        self.__Beep(830,200)
        self.__Beep(880,200)
        self.__Beep(988,400)
        time.sleep(200/1000)
        self.__Beep(740,200)
        self.__Beep(784,200)
        self.__Beep(784,200)
        self.__Beep(740,200)
        self.__Beep(784,200)
        self.__Beep(784,200)
        self.__Beep(740,200)
        self.__Beep(784,200)
        self.__Beep(880,200)
        self.__Beep(830,200)
        self.__Beep(880,200)
        self.__Beep(988,400)
        self.__Beep(880,200)
        self.__Beep(784,200)
        self.__Beep(699,200)
        self.__Beep(659,200)
        self.__Beep(699,200)
        self.__Beep(784,200)
        self.__Beep(880,400)
        self.__Beep(784,200)
        self.__Beep(699,200)
        self.__Beep(659,200)
        self.__Beep(587,200)
        self.__Beep(659,200)
        self.__Beep(699,200)
        self.__Beep(784,400)
        self.__Beep(699,200)
        self.__Beep(659,200)
        self.__Beep(587,200)
        self.__Beep(523,200)
        self.__Beep(587,200)
        self.__Beep(659,200)
        self.__Beep(699,400)
        self.__Beep(659,200)
        self.__Beep(587,200)
        self.__Beep(494,200)
        self.__Beep(523,200)
        time.sleep(400/1000)
        self.__Beep(349,400)
        self.__Beep(392,200)
        self.__Beep(330,200)
        self.__Beep(523,200)
        self.__Beep(494,200)
        self.__Beep(466,200)
        self.__Beep(440,200)
        self.__Beep(494,200)
        self.__Beep(523,200)
        self.__Beep(880,200)
        self.__Beep(494,200)
        self.__Beep(880,200)
        self.__Beep(1760,200)
        self.__Beep(440,200)
        self.__Beep(392,200)
        self.__Beep(440,200)
        self.__Beep(494,200)
        self.__Beep(784,200)
        self.__Beep(440, 200)
        self.__Beep(784,200)
        self.__Beep(1568,200)
        self.__Beep(392,200)
        self.__Beep(349,200)
        self.__Beep(440,200)
        self.__Beep(699,200)
        self.__Beep(415,200)
        self.__Beep(699,200)
        self.__Beep(1397,200)
        self.__Beep(349,200)
        self.__Beep(330,200)
        self.__Beep(311,200)
        self.__Beep(330,200)
        self.__Beep(659,200)
        self.__Beep(699,400)
        self.__Beep(784,400)
        self.__Beep(440,200)
        self.__Beep(494,200)
        self.__Beep(523,200)
        self.__Beep(880,200)
        self.__Beep(494,200)
        self.__Beep(880,200)
        self.__Beep(1760,200)
        self.__Beep(440,200)
        self.__Beep(392,200)
        self.__Beep(440,200)
        self.__Beep(494,200)
        self.__Beep(784,200)
        self.__Beep(440,200)
        self.__Beep(784,200)
        self.__Beep(1568,200)
        self.__Beep(392,200)
        self.__Beep(349,200)
        self.__Beep(392,200)
        self.__Beep(440,200)
        self.__Beep(699,200)
        self.__Beep(659,200)
        self.__Beep(699,200)
        self.__Beep(740,200)
        self.__Beep(784,200)
        self.__Beep(392,200)
        self.__Beep(392,200)
        self.__Beep(392,200)
        self.__Beep(392,200)
        self.__Beep(196,200)
        self.__Beep(196,200)
        self.__Beep(196,200)
        self.__Beep(185,200)
        self.__Beep(196,200)
        self.__Beep(185,200)
        self.__Beep(196,200)
        self.__Beep(208,200)
        self.__Beep(220,200)
        self.__Beep(233,200)
        self.__Beep(247,200)

          
    def __Beep(self, freq, duration):
        """
        play a 'beep' wiht the system
        """
        os.system('play -nq -t alsa synth {} sine {}'.format(duration/1000, freq))
            
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
                        modified_paramet_1 = paramet[1].replace("'", '"')
                        for att, value in json.loads(modified_paramet_1).items():
                            args = "{} {} {}".format(id, att, value)
                            formatCommande = self.__format_command(className, command, args)
                            eval(formatCommande)
                        return
                    else:
                        arguments = self.__clean_parameter(arguments)
                        if len(arguments) > 0:
                            arguments = "{} {}".format(className, arguments)
                        else:
                            arguments = "{}".format(className)
                        eval("self.do_{}('{}')".format(command, arguments))
                        return
                    
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
        
    def __format_command(self, className, comm, arg):
        return "self.do_{}(\"{} {}\")".format(comm, className, arg)
        
    def __Verif_json(self, paramet):
        paramet = paramet.replace("'", '"')
        try:
            json.loads(paramet)
        except ValueError as e:
            return False
        return True
        

    def __get_paramet(self, line):
        rgex = "^(\"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89aAbB][a-f0-9]{3}-[a-f0-9]{12}\")\, ?(.*)$"
        regex_prog = re.compile(rgex)
        res = regex_prog.findall(line)
        return res[0]
        
    
    def help_EOF(self):
        print(f"{Fore.BLUE}\n       EOF command to exit the program{Style.RESET_ALL}\n")

    def help_quit(self):
        print(
            f"{Fore.BLUE}\n       Quit command to exit the program{Style.RESET_ALL}\n")

    def help_create(self):
        print(
            f"{Fore.BLUE}\n                         Creates a new instance of BaseModel,")
        print(
            "         saves it (to the JSON file) and prints the id {Style.RESET_ALL}\n")

    def help_show(self):
        print(f"{Fore.BLUE}\n                Prints the string representation of an")
        print(
            "          instance based on the class name and id.{Style.RESET_ALL}\n")

    def help_all(self):
        print(
            f"{Fore.BLUE}\n         Prints all string representation of all instances")
        print("         based or not on the class name.{Style.RESET_ALL}\n")

    def help_destroy(self):
        print(f"{Fore.BLUE}\n           Deletes an instance based on the class name and id.{Style.RESET_ALL}\n")

    def help_update(self):
        print(
            f"{Fore.BLUE}\n                   Updates an instance based on the class name")
        print(
            "             and id by adding or updating attribute.{Style.RESET_ALL}\n")
    def help_count(self):
        print(
            f"{Fore.BLUE}\n           Retrieve the number of instances of a class.{Style.RESET_ALL}\n")
    
    def help_super(self):
        print(
            f"{Fore.RED}\n      install sox first with sudo apt install sox then run the comande :){Style.RESET_ALL}\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
