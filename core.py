import re
import models
import subprocess as sp

inventory = ['watch']


def start_game():
    while 1:
        try:
            AwakeningShell().make_instance()
        except:
            print("\nExiting...")
            break


def show_help():
    print(models.Colors.green + 'use' + models.Colors.nc + ' <x> <y> - use <x> with <y>')
    print(models.Colors.green + 'go' + models.Colors.nc + ' north/east/west/south - travel in the specified direction')
    print(models.Colors.green + 'examine' + models.Colors.nc + ' <z> - examine object <z> in the current location')
    print(models.Colors.green + 'choose' + models.Colors.nc + ' <choice> - choose <choice>')
    print(models.Colors.green + 'look' + models.Colors.nc + ' - display items of interest in current location')
    print(models.Colors.green + 'map' + models.Colors.nc + ' - display a location map')
    print(models.Colors.green + 'take' + models.Colors.nc + ' <item> - add <item> to inventory')
    print(models.Colors.green + 'inventory' + models.Colors.nc + '- display inventory')


class Command:
    def __init__(self, command, args):
        self.command = command
        self.args = args


class AwakeningShell:
    allowed = [Command('use', 2), Command('go', 1),
               Command('examine', 1), Command('choose', 1),
               Command('clear', 0), Command('stats', 0),
               Command('quit', 0), Command('help', 0),
               Command('inventory', 0), Command('take', 1)]

    def parse_command(self, command):
        split_comm = re.sub("[^\\w]", " ", command).split()
        if len(split_comm):
            for command in self.allowed:
                if split_comm[0] == command.command:
                    if len(split_comm) - 1 == command.args:
                        try:
                            getattr(self, command.command)()
                        except AttributeError:
                            print(models.Colors.red + 'command failed to run' + models.Colors.nc)
                        return
                    else:
                        print(models.Colors.red + 'incorrect usage' + models.Colors.nc)
                        return
            print(models.Colors.red + 'unknown command' + models.Colors.nc)

    def make_instance(self):
        self.parse_command(input(models.Colors.blue + "awakening> " + models.Colors.nc))

    @staticmethod
    def help():
        show_help()

    @staticmethod
    def quit():
        quit(0)

    @staticmethod
    def clear():
        sp.call('clear', shell=True)

    @staticmethod
    def stats():
        print('Days survived: ' + str(days_survived))
        print('Need to eat in: ' + str(eat_in))

    @staticmethod
    def inventory():
        print(models.Colors.green, end='')
        for item in inventory:
            if inventory.index(item) != len(inventory) - 1:
                print(item, end=', ')
            else:
                print(item)
        print(models.Colors.nc, end='')
