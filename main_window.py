from tkinter import *
from tkinter import messagebox
from commander import Commander

class MainWindow:
    """MainWindow class. Sets up the terminal-style Tkinter interface and handles input and output.
    """

    def __init__(self, resize, title, cmdlist, bgcolor = 'black', fgcolor = 'white'):
        """Initialize function for the MainWindow class.

        Args:
            resize (bool): wether or not the window can be resized
            title (string): title of the window
            cmdlist [(Command)]: Commandlist to be loaded.
            bgcolor (str, optional): Background color, can be hex value with #. Defaults to 'black'.
            fgcolor (str, optional): Foreground color, can be hex value with #. Defaults to 'white'.
        """
        self.root = Tk()
        self.title = title
        self.resize = resize
        self.bgcolor = bgcolor
        self.fgcolor = fgcolor
        self.cmdr = Commander()
        for cmd in cmdlist:
            self.cmdr.register_command(cmd)

    def setup(self):
        """Setup function that defines and configures the GUI.
        Main components are:
            input_entry         The main input element at the bottom of the window.
            output_text         The text widget that takes up most of the screen and displays
                                input and output.
        The following events are bound:
            <Return>            Starts processing input.
            <Escape>            Shows a messagebox and after confirmation quits the application.
        """
        self.root.configure(background=self.bgcolor)

        self.scrollbar_text = Scrollbar(self.root)
        self.scrollbar_text.pack(side=RIGHT, fill=Y)
        self.output_text = Text(self.root, fg=self.fgcolor, bg=self.bgcolor, state='disabled', yscrollcommand=self.scrollbar_text.set)
        self.output_text.pack(expand=1, fill=BOTH)
        self.scrollbar_text.configure(command=self.output_text.yview)

        self.input_entry = Entry(self.root, fg=self.fgcolor, bg=self.bgcolor)
        self.input_entry.pack(expand=0, fill=X, side=BOTTOM)
        self.input_entry.focus()

        self.root.bind('<Return>', self.process_input)
        self.root.bind('<Escape>', self.quit)

    def run(self):
        """run function to start the application.
        Calls the setup-function and starts the main loop.
        """
        # app settings
        self.root.title(self.title)
        # prevent resizing
        self.root.resizable(self.resize, self.resize)

        # setup gui
        self.setup()

        self.root.mainloop()

    def quit(self, event):
        """Quit function. Will show a Tkinter messagebox for confirmation.
        If confirmed, it will quit the application.

        Args:
            event (obj): event
        """
        result = messagebox.askokcancel('Quitting ..', 'Do you really want to quit?')

        if result:
            self.root.quit()

    def process_input(self, event):
        """Starts processing input.
        If any input was given, it will be split into a command (first word) and 
        everything else (*args) - see cmd_examples.py on what to do with that.
        Command will be run afterwards and the output added to the Text widget.

        Args:
            event (obj): event
        """
        input = self.input_entry.get()

        if len(input) < 1:
            return

        self.text_to_screen(input)
        inputlist = input.split()
        input = inputlist[0]
        inputlist.remove(input)

        if len(inputlist) > 0:
            output = self.cmdr.run_command(input, *inputlist)
        else:
            output = self.cmdr.run_command(input)

        if output is not None:
            self.text_to_screen(output)

        self.input_entry.delete(0, END)

    def text_to_screen(self, text):
        """Helper function to display text in a 'readonly'-way.
        The Text-widget is disabled by default. It requires to be enabled for text to be added.
        Also adds a newline and scrolls, if required.
        Afterwards, the widget will be disabled again.

        Args:
            text (string): Text to add to the text widget.
        """
        self.output_text.configure(state='normal')
        self.output_text.insert(END, text)
        self.output_text.insert(END, '\n')
        self.output_text.see(END)
        self.output_text.configure(state='disabled')