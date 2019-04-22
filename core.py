import re
import utils
import subprocess as sp

days_survived = 0
eat_in = 5
inventory = ['watch']


def start_game():
    while 1:
        AwakeningShell().make_instance()


def show_help():
    print('')
    print(utils.Colors.green + 'use' + utils.Colors.nc + ' <x> <y> - use <x> with <y>')
    print(utils.Colors.green + 'go' + utils.Colors.nc + ' north/east/west/south - travel in the specified direction')
    print(utils.Colors.green + 'examine' + utils.Colors.nc + ' <z> - examine object <z> in the current location')
    print(utils.Colors.green + 'choose' + utils.Colors.nc + ' <choice> - choose <choice>')
    print(utils.Colors.green + 'look' + utils.Colors.nc + ' - display items of interest in current location')
    print(utils.Colors.green + 'map' + utils.Colors.nc + ' - display a location map')
    print(utils.Colors.green + 'take' + utils.Colors.nc + ' <item> - add <item> to inventory')
    print(utils.Colors.green + 'inventory' + utils.Colors.nc + '- display inventory')


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
        split_comm = re.sub("[^\w]", " ", command).split()
        if len(split_comm):
            for command in self.allowed:
                if split_comm[0] == command.command:
                    if len(split_comm)-1 == command.args:
                        getattr(self, command.command)()
                        return
                    else:
                        print(utils.Colors.red + 'incorrect usage' + utils.Colors.nc)
                        return
            print(utils.Colors.red + 'unknown command' + utils.Colors.nc)

    def make_instance(self):
        self.parse_command(input("\n" + utils.Colors.blue + "awakening> " + utils.Colors.nc))

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
        print(utils.Colors.green, end='')
        for item in inventory:
            if inventory.index(item) != len(inventory)-1:
                print(item, end=', ')
            else:
                print(item)
        print(utils.Colors.nc, end='')
