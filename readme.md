# Commander GUI

*Commander GUI* is a *Terminal* or *Console* style application written in **Python** and **Tkinter**.
Lots of projects require some form of termina/console GUI, so I decided to create a reusable copy-paste-done-type of solution.
See *usage in your own project* below to get started. It's MIT License, so do whatever with it - but if it's a cool thing, please let me know.

## Running the examples

Clone the repo or download the files and simply run *main.py*.
The window will open and the focus is set to the text entry widget automatically. You can start typing immediately and see what happens.
When pressing *Enter/Return*, the command is processed.
Type **help** to see all available commands in the examples.
When pressing *Escape*, the application will prompt for confirmation and quit afterwards.

Some commands accept arguments that will be processed as well, e.g. try typing *name*, *name John* and *name John Doe* to see how arguments are working.

## Building a project around it

You're absolutely free to build a project around it - here's how:
1. Copy/Download/Clone *main.py*, *main_window.py*, *commander.py* and put in a folder
2. Create a *cmd_yourcoolprojectname.py* file and start creating commands (check *building commands* below)
3. Modify *main.py* and remove the cmd_examples import and instead import cmd_yourcoolprojectname
4. run *main.py* and check to see if your commands work

## Usage in your own project

All you really need is *main_window.py* and *commander.py*.
Copy them from this repo (or just download the files, copy/paste, rewrite by memory) and put them wherever it fits your project.
In your *main.py* import the MainWindow class:

    from main_window import MainWindow

You can initialize the window as follows (other parameters include background and foreground color):

    main_window = MainWindow(resize=True, title='Your very nice project', cmdlist=cmdlist)

The important part in the code above is the parameter **cmdlist** which should be a list of objects of the Command-class.

After that, you can run the application with:

    main_window.run()

If you want to modify the application in a way different from what it currently does, you'll have to check **main_window.py** for the Tkinter configuration.

### Building commands

To build your own commands, check *cmd_examples.py* for some easy to copy and modify examples.
Basically, you need to define 2 things:

1. a name that doubles as a command
2. a function that will be called

For example:

    def hello_world(*args):
        return 'Hello World!'

The above function is our function that should be called when someone types "hello". To make it into an command, we do the following:

    cmd_helloworld = Command('hello', hello_world)

Then it can be added to a list and passed to the MainWindow of the application.
*note:* a command name can currently only consist of one word - so 'hello' will work but 'hello world' will call 'hello' and pass 'world as arguments.

### The command functions

The functions currently need to conform to two rules:

1. a function needs to accept arguments as a parameter
2. a function needs to return a string

The *first* rule is to ensure that the application won't crash, even if arguments are not accepted by the command but the user provided some.
The *second* rule is to make sure that there's something to display to the user in the GUI.

Technically, those are not rules. You must not conform. It might crash or behave unexpectedly though.