#!/usr/bin/python3
""" This module is for a console/ frontend of AirBnB project"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class that defines the command of console.py"""
    prompt = '(hbnb) '
    __classes = ["BaseModel"]

    def do_create(self, line):
        """Creates an instance
        """
        args = line.split(" ")
        if line == '' or line is None:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            created_class = eval(f"{args[0]}")()
            print(created_class.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        """
        args = line.split(" ")
        if line == '' or line is None:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_id = "{}.{}".format(args[0], args[1])
            if class_id not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[class_id])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        args = line.split(" ")
        if line == '' or line is None:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_id = "{}.{}".format(args[0], args[1])
            if class_id not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[class_id]

    def do_all(self, line):
        """Prints all string representation of all instances
           based on or not on the class name
        """
        args = line.split(" ")
        if line == "" or line is None:
            print([str(values) for values in storage.all().values()])
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            d = storage.all().items()
            only = [str(o) for k, o in d if k.startswith(args[0])]
            print(only)

    def do_update(self, line):
        """Updates an instance based on the class
        name and id by adding or updating attribute
        (save the change into the JSON file).
        """
        args = line.split(" ")
        if line == '' or line is None:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            if class_id not in storage.all():
                print("** no instance found **")

    def do_EOF(self, line):
        """Handles End Of File character
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exits the program
        """
        return True

    def emptyline(self):
        """Does nothing on Enter
        """
        return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
