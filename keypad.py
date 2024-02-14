import tkinter as tk
from tkinter import ttk

class Keypad(tk.Frame):

    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        super().__init__(parent, **kwargs)
        self.keynames = keynames
        self.init_components(columns)

    def init_components(self, columns):
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        for i, key in enumerate(self.keynames):
            row, col = divmod(i, columns)
            button = tk.Button(self, text=key)
            button.grid(row=row, column=col, sticky="nsew")
            self.rowconfigure(row, weight = 1)
            self.columnconfigure(col, weight = 1)

    def bind(self, seq = None, handler = None, add = ""):
        """Bind an event handler to an event sequence."""
        for button in self.winfo_children():
            button.bind(seq, handler, add)
    

    def __setitem__(self, key, value):
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        for button in self.winfo_children():
            button[key] = value

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        return self.winfo_children()[0][key]

    def configure(self, config=None, **kwargs):
        """Apply configuration settings to all buttons."""
        for button in self.winfo_children():
            button.configure(config, **kwargs)

    @property
    def frame(self):
        """Returns a reference to the the superclass object for this keypad."""
        return self

if __name__ == '__main__':
    keys = list('789456123 0.')
    root = tk.Tk()
    root.title("Keypad Demo")
    keypad = Keypad(root, keynames=keys, columns=3)
    keypad.pack(expand=True, fill=tk.BOTH)
    root.mainloop()
