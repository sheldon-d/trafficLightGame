"""Title: trafficLightGame
Description: Traffic light game which lets users guess a number or phrase of different lengths
"""

import tkinter as tk
from tkinter.ttk import *


class GameGUI:
    def __init__(self, parent):
        """set up a GUI that consists of two frames that are toggled between each other
        depending upon what mode the program is in - Selecting Mode or Playing Game"""

        # Dictionary of constants for formatting and styling
        self.style_consts = {
            "BG_COL": "lightgrey",
            "HEADER_FONT": ("Helvetica", 16, "bold"),
            "LABEL_FONT": ("Calibri", 12),
            "BTN_FONT": ("Helvetica", 12),
            "PAD_X": 15,
            "PAD_Y": 15
        }

        # Configuring style using constants
        style = Style(parent)
        style.configure('TLabel', font=self.style_consts["LABEL_FONT"])
        style.configure('header.TFrame', background=self.style_consts["BG_COL"])
        style.configure('header.TLabel', background=self.style_consts["BG_COL"], font=self.style_consts["HEADER_FONT"])
        style.configure('TButton', font=self.style_consts["BTN_FONT"])

        self.phrases = []  # List for phrases to be appended to
        self.game_modes = ["Number", "Word"]  # List of game modes
        self.game_mode = tk.StringVar()
        self.num_chars = tk.StringVar()
        self.num_attempts = tk.StringVar()

        # Create selection frame for selecting game options
        self.selection_frame = Frame(parent)
        self.selection_frame.pack(fill=tk.X)
        self.get_selection_frame()

    def get_selection_frame(self):
        pad_x = self.style_consts["PAD_X"]
        pad_y = self.style_consts["PAD_Y"]

        # Create header for selection data frame
        header_frame = Frame(self.selection_frame, style='header.TFrame')
        header_frame.pack(fill=tk.X)
        header_label = Label(header_frame, text="Selecting game mode", style='header.TLabel')
        header_label.pack(pady=pad_y)

        # Set up options frame
        options_frame = Frame(self.selection_frame)
        options_frame.pack()

        # Labels for options
        game_mode = Label(options_frame, text="Game mode:")
        game_mode.grid(row=1, column=0, sticky=tk.NW, padx=pad_x, pady=pad_y)
        num_chars_label = Label(options_frame, text="Number of characters:")
        num_chars_label.grid(row=2, column=0, sticky=tk.NW, padx=pad_x, pady=pad_y)
        num_attempts_label = Label(options_frame, text="Number of attempts:")
        num_attempts_label.grid(row=3, column=0, sticky=tk.NW, padx=pad_x, pady=pad_y)

        # Set the initial selection for options
        self.game_mode.set("Select game mode")
        self.num_chars.set("Select character count")
        self.num_attempts.set("Select attempt count")

        # Create dropdown for selecting game mode
        game_mode_dropdown = Combobox(
            options_frame,
            width=20,
            textvariable=self.game_mode,
            values=self.game_modes
        )
        game_mode_dropdown.grid(row=1, column=1, sticky=tk.NW, padx=pad_x, pady=pad_y)

        # Create number picker for selecting number of characters
        num_chars_entry = Spinbox(
            options_frame,
            from_=5,
            to=10,
            width=21,
            textvariable=self.num_chars
        )
        num_chars_entry.grid(row=2, column=1, sticky=tk.NW, padx=pad_x, pady=pad_y)

        # Create number picker for selecting number of attempts
        num_attempts_entry = Spinbox(
            options_frame,
            from_=5,
            to=10,
            width=21,
            textvariable=self.num_attempts
        )
        num_attempts_entry.grid(row=3, column=1, sticky=tk.NW, padx=pad_x, pady=pad_y)

        # Create button for starting game
        start_game_btn = Button(
            self.selection_frame,
            text="Start game",
            command=self.check_options,
        )
        start_game_btn.pack(pady=pad_y)

    def check_options(self):
        """Test user inputs from dropdown and number pickers before starting game"""
        pass


def main():
    root = tk.Tk()
    root.title("Traffic Light Game")
    phrases = GameGUI(root)
    root.mainloop()


main()
