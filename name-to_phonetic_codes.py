# Import Packages
import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Read Data containing NATO phonetic codes
data = pd.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary
phonetic_dict = {
    row.letter: row.code for (index, row) in data.iterrows()
}


def name_to_code():
    """Convert words to NATO alphabet codes, no args"""

    delete_codes()  # Clear current result

    name = name_input.get()

    if len(name) == 0:
        messagebox.showinfo(title="Oops!", message="Please make an entry")
    else:

        word = name.upper()
        spaced_words = word.split()

        number_of_words = len(spaced_words)

        list_of_result = []
        title_list = []
        result_list = []

        for n in range(0, number_of_words):
            if number_of_words > 1:
                result_title = f"Word {n + 1}: {(spaced_words[n]).title()}"
            else:
                result_title = f'Word: {word.title()}'

            try:
                output_list = [phonetic_dict[letter] for letter in spaced_words[n]]
            except KeyError as error_prompt:
                messagebox.showinfo(title="Oops!", message=f"Please remove {error_prompt}")
            else:
                result = {result_title: output_list}
                list_of_result.append(result)
                title_list.append(result_title)
                result_list.append(output_list)

        # Write Result to window
        try:
            codes_result_label1.config(text=f"\n{title_list[0]}:\n{result_list[0]}")
            if number_of_words > 1:
                codes_result_label2.config(text=f"{title_list[1]}:\n{result_list[1]}")
                if number_of_words > 2:
                    codes_result_label3.config(text=f"{title_list[2]}:\n{result_list[2]}")
                    if number_of_words > 3:
                        codes_result_label4.config(text=f"{title_list[3]}:\n{result_list[3]}")
                        if number_of_words > 4:  # more than 4 words or index error found
                            messagebox.showinfo(title="Oops!", message=f"Maximum number of entries exceeded, "
                                                                       f"remove {number_of_words - 4} word(s)")
        except IndexError:
            delete_codes()  # Clear result display


def delete_codes():
    """Clear Result Display"""
    if codes_result_label1['text'] != "":
        codes_result_label1['text'] = ""
        if codes_result_label2['text'] != "":
            codes_result_label2['text'] = ""
            if codes_result_label3['text'] != "":
                codes_result_label3['text'] = ""
                if codes_result_label4['text'] != "":
                    codes_result_label4['text'] = ""


window = tk.Tk()
window.title("Name to Phonetic Code Converter")
window.config(padx=20, pady=20)
window.minsize(width=300, height=300)

# Input
name_input = tk.Entry(width=30)
name_input.grid(row=0, column=1)
name_input.insert(0, "four words maximum entry")
name_input.focus()

# Button
display_button = tk.Button(text="Display NATO Codes", command=name_to_code)
display_button.grid(row=1, column=1, columnspan=2)

clear_button = tk.Button(text="Clear", command=delete_codes)
clear_button.grid(row=2, column=1, columnspan=2)

# Labels
names_label = tk.Label(text="Name(s)")
names_label.grid(row=0, column=0)

phonetic_label = tk.Label(text="NATO phonetic codes: ")
phonetic_label.grid(column=0, row=1)

codes_result_label1 = tk.Label(text="No Entry")
codes_result_label1.grid(row=3, column=1)

codes_result_label2 = tk.Label()
codes_result_label2.grid(row=4, column=1)

codes_result_label3 = tk.Label()
codes_result_label3.grid(row=5, column=1, columnspan=2)

codes_result_label4 = tk.Label()
codes_result_label4.grid(row=6, column=1, columnspan=2)

window.mainloop()
