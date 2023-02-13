#!/usr/bin/python3
""" This module is for a console/ frontend of AirBnB project"""
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class that defines the command of console.py"""
    prompt = '(hbnb) '

    def do_create(self, line):
        """Creates an instance
        """
        if line == '' or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            print('exists')

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
        pass




if __name__ == "__main__":
    HBNBCommand().cmdloop()
