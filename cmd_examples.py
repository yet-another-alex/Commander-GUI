from commander import Command
from datetime import date

fake_inventory = ['sword', 'a stack of dirt', 'a three headed monkey', 'a banana', '6000 gold coins', 'a red hering']

def hello_world(*args):
    return 'Hello World!'

def name_is(*args):
    if len(args) > 0:
        name = ' '.join(args)
        return f"Hello {name}, I am {name[::-1]}!"
    else:
        return 'Your name?'

def quit(*args):
    return 'Oh, no thank you, Dave ...'

def time(*args):
    return date.today()

def reverse(*args):
    if args is not None:
        if len(args) > 0:
            return ' '.join(args)[::-1]

def go(*args):
    if args is not None:
        if len(args) > 0:
            dir = args[0].lower()
            
            if dir == 'left':
                return 'Such a nice direction. You were eaten by a bear.'
            elif dir == 'right':
                return 'What a great choice! You got lost in the woods and froze to death.'
            else:
                return 'Instructions unclear, you starved to death.'

        else:
            return 'Going without moving is pretty much standing ..'

def inventory(*args):
    inv_str = '~~~~~~~~~~ Inventory:'
    for item in fake_inventory:
        inv_str += f"\n{item}"
    return inv_str

def help(*args):
    output = '~~~~~~~~~ Available commands:'
    output += '\nCommand\t\tFunction Name'
    for cmd in cmdlist:
        output += f"\n{cmd.name}:\t\t{cmd.function.__name__}"
    return output



### Create a list of commands and add individual commands ###

cmdlist = list()

cmd_name = Command('name', name_is)
cmdlist.append(cmd_name)

cmd_hw = Command('hello', hello_world)
cmdlist.append(cmd_hw)

cmd_quit = Command('quit', quit)
cmdlist.append(cmd_quit)

cmd_today = Command('today', time)
cmdlist.append(cmd_today)

cmd_rev = Command('reverse', reverse)
cmdlist.append(cmd_rev)

cmd_go = Command('go', go)
cmdlist.append(cmd_go)

# example for multiple input commands for the same function:
cmd_inv = Command('inv', inventory)
cmdlist.append(cmd_inv)

cmd_inv = Command('inventory', inventory)
cmdlist.append(cmd_inv)

cmd_inv = Command('i', inventory)
cmdlist.append(cmd_inv)

cmd_help = Command('help', help)
cmdlist.append(cmd_help)