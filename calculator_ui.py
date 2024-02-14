import tkinter as tk
import random
from math import *
from tkinter import ttk
from keypad import Keypad
from pygame import mixer

class CalculatorUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.history_value = ""
        self.variable =""
        self.variable1 = 0
        self.function = tk.StringVar()
        self.history_list = []      
        self.title("Calculator")
        self.init_components()
        mixer.init()
    def play_sound_error(self):
        # Load the sound file
        mixer.music.load("Error.mp3")
        # Play the sound
        mixer.music.play()
    def play_sound_normal(self):
        # Load the sound file
        soundlist = ["sound1.mp3","sound2.mp3","sound3.mp3"]
        selected = random.choice(soundlist)
        mixer.music.load(selected)
        # Play the sound
        mixer.music.play()
    def play_sound_work(self):
        # Load the sound file
        mixer.music.load("Quickly.mp3")
        # Play the sound
        mixer.music.play()
    def init_components(self):
        """Create components and layout the UI."""
        optiondisplay = {"padx":3,"pady":3,"font":("Arial", 30),"background": "black", "foreground": "yellow"}
        optionhistory = {"padx":3,"pady":3,"font":("Arial", 10),"background": "black", "foreground": "yellow"}
        self.display = tk.Label(text = self.variable, **optiondisplay, justify = "right",anchor = "e")
        self.history = tk.Label(text = self.history_value, **optionhistory, justify = "right",anchor = "e")
        self.history.pack(side = tk.TOP, expand = True, fill = tk.BOTH)
        self.display.pack(side = tk.TOP, expand = True, fill = tk.BOTH)
        clrbar = self.create_button_bar()
        clrbar.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
        framekey = self.create_keypad()
        framekey.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
        framesigns = self.create_sign_pad()
        framesigns.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
        dcm_bar = self.decimal_place_bar()
        dcm_bar.pack(side = tk.RIGHT, expand = True, fill = tk.BOTH)
    
    def create_keypad(self):
        """Create numeric key frame for keypad"""
        option = {"padx":5,"pady":5,"font":("Quicksand", 12),"background": "yellow", "foreground": "blue"}
        numeric = ["7","8","9","4","5","6","1","2","3","π","0","."]
        keypad = Keypad(parent = self,keynames = numeric, columns = 3)
        keypad.pack(expand=True, fill=tk.BOTH)
        keypad.configure(**option)
        keypad.bind(seq = "<Button>", handler = self.key_pressed, add = "+")
        return keypad
    
    def create_sign_pad(self):
        """Create sign button frame"""
        signs = ["*","/","+","-","(",")","^","mod","e","="]
        option = {"padx":5,"pady":5,"font":("Quicksand", 12),"background": "orange", "foreground": "blue"}
        keypad = Keypad(parent = self,keynames = signs, columns = 1)
        keypad.pack(expand=True, fill=tk.BOTH)
        keypad.configure(**option)
        keypad.bind(seq = "<Button>", handler = self.key_pressed, add = "+")
        return keypad

    def create_button_bar(self):
        """Create clear button and del button and combobox for functions"""      
        option = {"padx":5,"pady":5,"font":("Quicksand", 12),"background": "green", "foreground": "blue"}
        function_list = ["","Exponential","Square root","Log base 2","Log base 10","Natural log","Sine function","Cosine function","Tangent function","Arcsine","Arccosine","Arctangent"]
        frame = tk.Frame()
        clr  = tk.Button(frame, text = "CLR", **option)
        delete = tk.Button(frame, text = "DEL", **option)
        select = tk.Button(frame, text = "Select Function", **option)
        func_menu = ttk.Combobox(values = function_list, font=("Arial", 12), foreground = "blue", textvariable = self.function)
        func_menu.current(newindex = 0)
        # func_menu.bind("<<ComboboxSelected>>", self.combo_handler)        
        func_menu.pack(side = tk.TOP, expand = True, fill = tk.BOTH)
        select.pack(side = tk.TOP, expand = True, fill = tk.BOTH)
        clr.pack(side = tk.TOP, expand = True, fill = tk.BOTH)
        delete.pack(side = tk.TOP, expand = True, fill = tk.BOTH)
        select.bind("<Button>", self.combo_handler)  
        clr.bind("<Button>", self.clear_pressed)  
        delete.bind("<Button>", self.del_pressed)  
        return frame
    
    def decimal_place_bar(self):
        option = {"padx":5,"pady":5,"font":("Quicksand", 12),"background": "pink", "foreground": "blue"}
        decimal = ["2 Decimal", "Normal","Science"]
        keypad = Keypad(parent = self,keynames = decimal, columns = 1)
        keypad.pack(expand=True, fill=tk.BOTH)
        keypad.configure(**option)
        keypad.bind(seq = "<Button>", handler = self.decimal_pressed, add = "+")
        return keypad
    
    def combo_handler(self, event = None):
        selected_function = self.function.get()
        signs = ["+","-","*","/","%"]
        self.varlist = list(self.variable)
        last_index = len(self.varlist)-1
        try:
            if selected_function == "Square root":
                if self.varlist[last_index] in signs:
                    self.varlist.append("sqrt(")
                else:
                    self.varlist.insert(0,"sqrt(")
                    self.varlist.append(")")
            elif selected_function == "Log base 10":
                if self.varlist[last_index] in signs:
                    self.varlist.append("log10(")
                else:
                    self.varlist.insert(0,"log10(")
                    self.varlist.append(")")
            elif selected_function == "Log base 2":
                if self.varlist[last_index] in signs:
                    self.varlist.append("log2(")
                else:
                    self.varlist.insert(0,"log2(")
                    self.varlist.append(")")
            elif selected_function == "Exponential":
                if self.varlist[last_index] in signs:
                    self.varlist.append("exp(")
                else:
                    self.varlist.insert(0,"exp(")
                    self.varlist.append(")")
            elif selected_function == "Natural log":
                if self.varlist[last_index] in signs:
                    self.varlist.append("log(")
                else:
                    self.varlist.insert(0,"log(")
                    self.varlist.append(")")
            elif selected_function == "Sine function":
                if self.varlist[last_index] in signs:
                    self.varlist.append("sin(")
                else:
                    self.varlist.insert(0,"sin(")
                    self.varlist.append(")")
            elif selected_function == "Cosine function":
                if self.varlist[last_index] in signs:
                    self.varlist.append("cos(")
                else:
                    self.varlist.insert(0,"cos(")
                    self.varlist.append(")")
            elif selected_function == "Tangent function":
                if self.varlist[last_index] in signs:
                    self.varlist.append("tan(")
                else:
                    self.varlist.insert(0,"tan(")
                    self.varlist.append(")")
            elif selected_function == "Arcsine":
                if self.varlist[last_index] in signs:
                    self.varlist.append("asin(")
                else:
                    self.varlist.insert(0,"asin(")
                    self.varlist.append(")")
            elif selected_function == "Arccosine":
                if self.varlist[last_index] in signs:
                    self.varlist.append("acos(")
                else:
                    self.varlist.insert(0,"acos(")
                    self.varlist.append(")")
            elif selected_function == "Arctangent":
                if self.varlist[last_index] in signs:
                    self.varlist.append("atan(")
                else:
                    self.varlist.insert(0,"atan(")
                    self.varlist.append(")")
            self.play_sound_work()
        except IndexError:
            self.play_sound_error()
        self.variable = ""
        for i in range(len(self.varlist)):
            self.variable = self.variable + self.varlist[i]
        self.display.config(text = self.variable)

    def key_pressed(self, event = tk.Event):
        EQUAL = "="
        widget = event.widget    
        ERRORCOLOR = "red"
        NORMALCOLOR = "yellow"
        if "." in self.variable and widget["text"] == ".":
            self.play_sound_normal()
        elif widget["text"] == "mod":
            self.variable = self.variable + "%"
            self.play_sound_normal()
        elif widget["text"] == "π":
            self.variable = self.variable + "pi"
            self.play_sound_normal()
        elif widget["text"] == "^":
            self.variable = self.variable + "**"
            self.play_sound_normal()
        elif widget["text"] == EQUAL:
            try:
                self.variable1 = eval(self.variable)
                self.history_list.append([self.variable, self.variable1])
                self.history_value = self.history_value + f"{self.variable:<50} {EQUAL:^1} {self.variable1:>50}\n"                
                self.variable = str(self.variable1)
                self.display.config(fg = NORMALCOLOR, text = self.variable)
                self.history.config(fg = NORMALCOLOR, text = self.history_value)
                self.play_sound_work()
            except SyntaxError:
                self.display.config(fg = ERRORCOLOR)
                self.play_sound_error()
            except ValueError:
                self.display.config(fg = ERRORCOLOR)
                self.play_sound_error()
            except ZeroDivisionError:
                self.display.config(fg = ERRORCOLOR)
                self.play_sound_error()
        else:
            self.variable = self.variable + widget["text"]
            self.play_sound_normal()
        self.display.config(text = self.variable)

    def decimal_pressed(self, event = None):
        widget = event.widget
        ERRORCOLOR = "red"
        NORMALCOLOR = "yellow"
        try:
            self.variable1 = float(self.variable)
            if widget["text"] == "2 Decimal":
                self.variable = f"{self.variable1:.2f}"
            elif widget["text"] == "Normal":
                self.variable = f"{self.variable1:.8f}"
            elif widget["text"] == "Science":
                self.variable = f"{self.variable1:.2e}"
            self.display.config(text = self.variable, fg = NORMALCOLOR)
            self.play_sound_work()
        except ValueError:
            self.display.config(fg = ERRORCOLOR)
            self.play_sound_error()
        except ZeroDivisionError:
            self.display.config(fg = ERRORCOLOR)
            self.play_sound_error()

    def clear_pressed(self, event = None):
        self.variable = ""
        self.variable1 = 0
        self.history_list.clear()
        self.history_value = ""
        self.display.config(text = self.variable)
        self.history.config(text = self.variable)

    def del_pressed(self, event = None):
        numeric = ["(",")","*","%","+","-","1","2","3","4","5","6","7","8","9","0","."]
        self.varlist = list(self.variable)
        try:
            c = self.varlist.pop(len(self.varlist)-1)
            if c not in numeric:
                while c not in numeric:
                    c = self.varlist.pop(len(self.varlist)-1)
                self.varlist.append(c)
            self.variable = ""
        except IndexError:
            self.varlist = []
            self.variable = ""
        for i in range(len(self.varlist)):
            self.variable = self.variable + self.varlist[i]
        self.display.config(text = self.variable)

    def run(self):
        self.mainloop()

