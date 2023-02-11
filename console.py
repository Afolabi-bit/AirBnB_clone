#!/usr/bin/python3
""" This module is for a console/ frontend of AirBnB project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class that defines the command of console.py"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        return True
    def do_quit(self, line):
        return True





if __name__ == "__main__":
    HBNBCommand().cmdloop()
