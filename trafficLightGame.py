"""Title: trafficLightGame
Description: Traffic light game which lets users guess a number or phrase of different lengths
"""

import tkinter as tk
from tkinter.ttk import *
from phrases import *


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
            "ATTEMPT_LABEL_FONT": ("Helvetica", 12),
            "PAD_X": 15,
            "PAD_Y": 20
        }

        # Configuring style using constants
        style = Style()
        style.configure('TLabel', font=self.style_consts["LABEL_FONT"])
        style.configure('header.TFrame', background=self.style_consts["BG_COL"])
        style.configure('header.TLabel', background=self.style_consts["BG_COL"], font=self.style_consts["HEADER_FONT"])
        style.configure('TButton', font=self.style_consts["BTN_FONT"])
        style.configure('error.TCombobox', foreground="red")
        style.configure('error.TSpinbox', foreground="red")
        style.configure('correct.TLabel', background="lightgreen")
        style.configure('valid.TLabel', background="orange")
        style.configure('incorrect.TLabel', background="dark salmon")
        style.configure('attempts.TLabel', font=self.style_consts["ATTEMPT_LABEL_FONT"])
        style.configure('errorAttempt.TLabel', font=self.style_consts["ATTEMPT_LABEL_FONT"], foreground="red")

        self.parent = parent
        self._phrase = ""
        self.game_modes = ["Number", "Word"]  # List of game modes

        self.game_mode = tk.StringVar()
        self.num_chars = tk.StringVar()
        self.num_attempts = tk.StringVar()
        self.submit_attempt_btn = Button()
        self.num_chars_range = (3, 7)
        self.num_attempts_range = (5, 10)
        self.default_num = "5"

        self.active_entry = None
        self.num_chars_entry = None
        self.num_attempts_entry = None
        self.game_mode_dropdown = None

        self.attempt_num = 0
        self.attempt_entries = None
        self.attempts = None
        self.attempt_label = None

        # Create selection frame for selecting game options
        self.selection_frame = Frame(parent)
        self.get_selection_frame()

        # Create selection frame for selecting game options
        self.playing_frame = Frame(parent)

    def get_selection_frame(self):
        self.selection_frame.pack(fill=tk.X)
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
        self.game_mode.set(self.game_modes[0])
        self.num_chars.set(self.default_num)
        self.num_attempts.set(self.default_num)

        # Create dropdown for selecting game mode
        self.game_mode_dropdown = Combobox(
            options_frame,
            width=30,
            textvariable=self.game_mode,
            values=self.game_modes
        )
        self.game_mode_dropdown.grid(row=1, column=1, sticky=tk.NW, padx=pad_x, pady=pad_y)

        # Create number picker for selecting number of characters
        self.num_chars_entry = Spinbox(
            options_frame,
            from_=self.num_chars_range[0],
            to=self.num_chars_range[1],
            width=31,
            textvariable=self.num_chars
        )
        self.num_chars_entry.grid(row=2, column=1, sticky=tk.NW, padx=pad_x, pady=pad_y)

        # Create number picker for selecting number of attempts
        self.num_attempts_entry = Spinbox(
            options_frame,
            from_=self.num_attempts_range[0],
            to=self.num_attempts_range[1],
            width=31,
            textvariable=self.num_attempts
        )
        self.num_attempts_entry.grid(row=3, column=1, sticky=tk.NW, padx=pad_x, pady=pad_y)

        # Create button for starting game
        start_game_btn = Button(
            self.selection_frame,
            text="Start game",
            command=self.check_options,
        )
        self.parent.bind("<Return>", self.check_options_event)
        start_game_btn.pack(pady=pad_y)

    def get_playing_frame(self):
        self.playing_frame.pack(fill=tk.X)
        pad_x = self.style_consts["PAD_X"]
        pad_y = self.style_consts["PAD_Y"]

        num_attempts = int(self.num_attempts.get())
        num_chars = int(self.num_chars.get())
        self.attempt_entries = [["" for _ in range(num_chars)] for _ in range(num_attempts)]
        self.attempts = ["" for _ in range(num_attempts)]

        # Create header for selection data frame
        header_frame = Frame(self.playing_frame, style='header.TFrame')
        header_frame.pack(fill=tk.X)
        header_label = Label(header_frame, text=f"Traffic Light {self.game_mode.get()} Game", style='header.TLabel')
        header_label.pack(pady=pad_y)

        # Set up character frame
        chars_frame = Frame(self.playing_frame)
        chars_frame.pack()

        game_mode = self.game_modes.index(self.game_mode.get())
        place_vals = ["M", "HTh", "TTh", "Th", "H", "T", "O"]
        start_row = 0
        end_row = num_attempts

        if game_mode == 0:
            self._phrase = get_random_number(num_chars)
            start_row += 1
            end_row += 1

            for n in range(num_chars):
                label_idx = (len(place_vals) - num_chars) + n
                label = Label(
                    chars_frame,
                    text=place_vals[label_idx],
                    font=self.style_consts["HEADER_FONT"],
                    justify='center'
                )
                label.grid(row=0, column=n, padx=pad_x, pady=(pad_y, 0))
        else:
            self._phrase = get_random_word(num_chars)
        print(self._phrase)

        row_num = 0
        for i in range(start_row, end_row):
            for j in range(num_chars):
                entry = Entry(
                    chars_frame,
                    width=10,
                    font=self.style_consts["HEADER_FONT"],
                    justify='center'
                )
                if row_num > 0:
                    entry.config(state='disabled')

                if game_mode == 0:
                    val_cmd = (chars_frame.register(self.validate_int_entry), '%P', '%d')
                else:
                    val_cmd = (chars_frame.register(self.validate_str_entry), '%P', '%d')
                    entry.bind('<KeyRelease>', self.to_uppercase)
                    entry.bind('<FocusOut>', self.to_uppercase)
                entry.configure(validate="key", validatecommand=val_cmd)
                entry.grid(row=i, column=j, padx=pad_x, pady=pad_y)
                entry.bind('<FocusIn>', self.set_active)
                entry.bind('<BackSpace>', self.clear_active)
                self.attempt_entries[row_num][j] = entry

            row_num += 1

        self.active_entry = self.attempt_entries[0][0]
        self.entry_next()

        # Set up submit frame
        submit_frame = Frame(self.playing_frame)
        submit_frame.pack()

        # Create button for changing mode
        change_mode_btn = Button(
            submit_frame,
            text="Change mode",
            command=self.new_selection_frame,
        )
        change_mode_btn.grid(row=0, column=0, pady=pad_y)

        # Create button for submitting attempt
        self.submit_attempt_btn = Button(
            submit_frame,
            text="Submit",
            command=self.check_attempt,
        )
        self.submit_attempt_btn.grid(row=0, column=1, padx=5*pad_x, pady=pad_y)

        self.parent.bind("<Return>", self.check_attempt_event)
        self.attempt_label = Label(submit_frame, text=f"{self.attempt_num} attempts", style="attempts.TLabel")
        self.attempt_label.grid(row=0, column=2, pady=pad_y)

    def check_options(self):
        """Test user inputs from dropdown and number pickers before starting game"""
        valid_game_mode = self.test_mode_input(self.game_mode_dropdown)
        valid_num_chars = self.test_int_input(self.num_chars_entry, self.num_chars_range)
        valid_num_attempts = self.test_int_input(self.num_attempts_entry, self.num_attempts_range)

        if all([valid_game_mode, valid_num_chars, valid_num_attempts]):
            self.selection_frame.pack_forget()
            self.new_playing_frame()

    def check_attempt(self):
        """Test user input in attempt entries"""
        num_attempts = int(self.num_attempts.get())
        num_chars = int(self.num_chars.get())
        game_mode = self.game_modes.index(self.game_mode.get())
        self.attempt_label.config(style="attempts.TLabel")

        if self.attempt_num >= num_attempts or self._phrase in self.attempts:
            self.new_playing_frame()
            return

        attempt_entry = self.attempt_entries[self.attempt_num]
        if any([len(entry.get()) == 0 for entry in attempt_entry]):
            self.attempt_label.config(text="Please fill in all characters", style="errorAttempt.TLabel")
            return

        attempt = "".join([entry.get() for entry in attempt_entry])
        self.attempts[self.attempt_num] = attempt

        for char in range(num_chars):
            if attempt_entry[char].get() == self._phrase[char]:
                attempt_entry[char].config(state='disabled', style="correct.TLabel")
            elif attempt_entry[char].get() in self._phrase:
                attempt_entry[char].config(state='disabled', style="valid.TLabel")
            else:
                attempt_entry[char].config(state='disabled', style="incorrect.TLabel")

        self.attempt_num += 1

        if attempt == self._phrase:
            self.attempt_label.config(text=f"Found in {self.attempt_num} attempts")
            self.submit_attempt_btn.config(text="Play again")
        elif self.attempt_num == num_attempts:
            if game_mode == 0:
                self.attempt_label.config(text=f"Number was {self._phrase}")
            else:
                self.attempt_label.config(text=f"Word was {self._phrase}")
            self.submit_attempt_btn.config(text="Play again")
        else:
            self.attempt_label.config(text=f"{self.attempt_num} attempts")
            attempt_entry = self.attempt_entries[self.attempt_num]
            for char in range(num_chars):
                attempt_entry[char].config(state='enabled')
        self.entry_next()

    def new_selection_frame(self):
        self.destroy_frames()
        self.selection_frame = Frame(self.parent)
        self.get_selection_frame()

    def new_playing_frame(self):
        self.destroy_frames()
        self.playing_frame = Frame(self.parent)
        self.get_playing_frame()

    def destroy_frames(self):
        self.selection_frame.destroy()
        self.playing_frame.destroy()
        self.attempt_num = 0

    def test_mode_input(self, input_field):
        """Tests if game mode is selected correctly by user"""

        value = input_field.get()  # gets value from entry
        error_text = "Please choose a game mode"

        try:
            change_frame = True

            if value not in self.game_modes:
                raise ValueError

        except ValueError:
            input_field.config(style='error.TCombobox')  # Changes entry colour to indicate error
            input_field.delete(0, tk.END)  # Clears entry
            input_field.insert(0, error_text)  # Inserts error message
            input_field.bind("<Button>", self.clear_dropdown)
            change_frame = False

        return change_frame

    def test_int_input(self, input_field, input_range):
        """Tests if integers are input correctly by user"""

        value = input_field.get()  # gets value from entry
        error_text = "Please choose a valid number"

        try:
            change_frame = True
            number = int(value)  # Returns true if number contains integers only

            if number < input_range[0] or number > input_range[1]:  # Returns false if number is negative (less than 0)
                raise ValueError

        except ValueError:
            input_field.config(style='error.TSpinbox')  # Changes entry colour to indicate error
            input_field.delete(0, tk.END)  # Clears entry
            input_field.insert(0, error_text)  # Inserts error message
            input_field.bind("<Button>", self.clear_entry)
            change_frame = False

        return change_frame

    def check_options_event(self, event):
        self.check_options()

    def check_attempt_event(self, event):
        self.check_attempt()

    def clear_dropdown(self, event):
        """Clears error message from dropdown when clicked"""
        event.widget.config(style='TCombobox')
        event.widget.delete(0, tk.END)
        event.widget.unbind("<Button>")

    def clear_entry(self, event):
        """Clears error message from entry when clicked"""
        event.widget.config(style='TSpinbox')
        event.widget.delete(0, tk.END)
        event.widget.unbind("<Button>")

    def validate_int_entry(self, char, action_type):
        if action_type == "0":
            return True

        if char.isdigit() and len(char) == 1:
            self.entry_next()
            return True
        return False

    def validate_str_entry(self, char, action_type):
        if action_type == "0":
            return True

        if char.isalpha() and len(char) == 1:
            if char.isupper():
                self.entry_next()
            return True
        return False

    def to_uppercase(self, event):
        if event.widget.get().islower():
            val = event.widget.get().upper()
            event.widget.delete(0, tk.END)
            event.widget.insert(0, val)

    def set_active(self, event):
        self.active_entry = event.widget

    def clear_active(self, event):
        self.active_entry = event.widget
        event.widget.delete(0, tk.END)
        self.entry_prev()

    def entry_next(self):
        if not isinstance(self.active_entry.tk_focusNext(), Button):
            self.active_entry = self.active_entry.tk_focusNext()
        self.active_entry.focus()

    def entry_prev(self):
        if not isinstance(self.active_entry.tk_focusPrev(), Button):
            self.active_entry = self.active_entry.tk_focusPrev()
        self.active_entry.focus()


def main():
    root = tk.Tk()
    root.title("Traffic Light Game")
    GameGUI(root)
    root.mainloop()


main()
