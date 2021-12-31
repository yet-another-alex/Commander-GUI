
class Commander:
    """Commander class.
    Works like a managing class for multiple single commands.
    Contains a dictionary 'commands' that contains all possible commands.

    """

    CMD_NOT_FOUND = "Command not found!"

    def __init__(self):
        """Initialization function.
        Initializes 'commands' as a dictionary.
        """
        self.commands = dict()

    def register_command(self, cmd):
        """Adds a command to the dictionary.

        Args:
            cmd (Command): Command to be added to the list.
        """
        self.commands[cmd.name] = cmd.function

    def is_command(self, name):
        """Helper function for convenience.
        CHecks if a command is available in the commands dictionary.

        Args:
            name (string): Command to search in the dictionary.

        Returns:
            bool: true if the command is vaild, false otherwise
        """
        return name in self.commands

    def unregister_command(self, name):
        """Helper function to delete a Command from the dictionary.

        Args:
            name (string): Name of the Command that should be deleted.
        """
        del self.commands[name]

    def run_command(self, name, *args):
        """Helper function to execute a Command with a supplied name.

        Args:
            name (string): Name of the Command that should be executed.

        Returns:
            string: Output from the Command.
        """
        if self.is_command(name):
            return self.commands[name](*args)
        else:
            return self.CMD_NOT_FOUND


class Command:
    """Command class.
    Contains a name and a function.
    """

    def __init__(self, name, function):
        """Initializer function for the Command class.

        Args:
            name (string): Name of the Command.
            function (func): Function that should be called.
        """
        self.name = name
        self.function = function