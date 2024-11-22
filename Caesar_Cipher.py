#This App created by Diyar Penjweny from Kurdistan
#
# What is Caesar Cipher :
#
#The Caesar Cipher, used by Julius Caesar around 58 BC,
# is a substitution cipher that shifts letters in a message to make it unreadable if intercepted.
# To decrypt, the receiver reverses the shift.
#
#
# 21/11/2024
from time import *


print ("""
 +-+-+-+-+-+ +-+-+-+-+-+-+-+-+
 |D|i|y|a|r| |P|e|n|j|w|e|n|y|
 +-+-+-+-+-+ +-+-+-+-+-+-+-+-+
 """)

sleep(1)


import tkinter as tk        #for GUI in python
from tkinter import ttk     #subclass of tkinter
from tkinter import messagebox    #subclass of tkinter


# Function to encrypt text using Caesar Cipher بۆ ئینکریپتکردنی نوسینەکە
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - start + (shift if mode == 'Encrypt' else -shift)) % 26
            result += chr(start + shifted)
        else:
            result += char
    return result;

# Function to handle the encryption/decryption button click  کاتێ کە کلیک لە پرۆسێس ئەکەیت هەڵئەستێ بە تێست کردنی بۆشاییەکان تاوەکو بە بەتاڵی یان بە داتاتایپی هەڵە پرت نەکردبێتەوە
def process_text():
    text = text_entry.get("1.0", "end-1c").strip()  # Get text from multi-line input and remove leading/trailing whitespace
    if not text:  #if empty show error ئەگەر بەتاڵبوو ئیرۆری پشان بە
        messagebox.showerror("Input Error", "Please enter some text.")
        return


    try:
        shift = int(shift_entry.get())
    except ValueError:#if not use int show error ئەگەر ئینتیجەری بەکارنەهێنا ئەوا ئیرۆری بۆ بگەڕێنەوە
        messagebox.showerror("Input Error", "Please enter a valid integer for shift value.")
        return

    mode = operation_var.get()

    if mode == "Select Operation": #if user do not choose Encrypte/Decrypt show error message ئەگەر بەکارهێنەر یەکێک لەئینکریپت یان دیکریپت هەڵنەبژارد ئەوا ئیرۆری پشان بە
        messagebox.showerror("Input Error", "Please select an operation (Encrypt/Decrypt).")
        return

    result_text = caesar_cipher(text, shift, mode)
    result_area.delete("1.0", "end")  # Clear previous result ئەنجامی پێشووت ئەسڕێتەوە
    result_area.insert(tk.END, result_text)  # Insert new result ئەنجامە تازەکە پیشان ئەیاتەوە


# this function to clear the input and result ئەم فەکشنە بەکاریەت بۆ سڕینەوەی ئەنجام و ئینپوت
def clear_fields():
    text_entry.delete("1.0", "end")
    shift_entry.delete(0, "end")
    operation_var.set("Select Operation")
    result_area.delete("1.0", "end")


# Create the main window  GUI دروستکردنی پەڕەیەک بۆ 
root = tk.Tk()
root.title("Caesar Cipher Tool")

root.geometry("1000x1000")
root.config(bg="#2C3E50")

# Title label نوسینی ناوی بەرنامەکە لەناو لەیبڵێک
title_label = tk.Label(root, text="Caesar Cipher Tool", font=("Segoe UI", 22, "bold"), bg="#2980B9", fg="white", anchor="center")
title_label.pack(fill="x", pady=20)

# create text input area دروستکردنی خانەی نوسین
text_label = tk.Label(root, text="Enter text to Encrypt/Decrypt:", font=("Segoe UI", 12), bg="#2C3E50", fg="white")
text_label.pack(pady=5)
text_entry = tk.Text(root, height=5, width=50, font=("Segoe UI", 12), wrap=tk.WORD, bg="#34495E", fg="#ECF0F1", bd=2, relief="solid", highlightthickness=0)
text_entry.pack(pady=10)

# create shift input field درووستکردنی خانەی شیفت
shift_label = tk.Label(root, text="Enter Shift Value:", font=("Segoe UI", 12), bg="#2C3E50", fg="white")
shift_label.pack(pady=5)
shift_entry = tk.Entry(root, width=10, font=("Segoe UI", 12), bg="#34495E", fg="#ECF0F1", bd=2, relief="solid")
shift_entry.pack(pady=5)

# Operation selection (Encrypt/Decrypt) using a ComboBox هەڵبژاردنی ئینکریپت و دیکریپت لەڕێی کۆمبۆ بۆکس
operation_var = tk.StringVar(value="Select Operation")
operation_label = tk.Label(root, text="Select Operation:", font=("Segoe UI", 12), bg="#2C3E50", fg="white")
operation_label.pack(pady=5)
operation_menu = ttk.Combobox(root, textvariable=operation_var, values=["Encrypt", "Decrypt"], width=20, state="readonly", font=("Segoe UI", 12), background="#34495E", foreground="#ECF0F1")
operation_menu.pack(pady=10)

# Process button دوگمەی پرۆسێسکردن
process_button = tk.Button(root, text="Process", font=("Segoe UI", 14, "bold"), bg="#16A085", fg="white", relief="flat", command=process_text)
process_button.pack(pady=15, fill="x")

# Clear button دوگمەی سڕینەوە
clear_button = tk.Button(root, text="Clear", font=("Segoe UI", 14, "bold"), bg="#E74C3C", fg="white", relief="flat", command=clear_fields)
clear_button.pack(pady=10, fill="x")

# Result area - scrollable text widget
result_label = tk.Label(root, text="Result:", font=("Segoe UI", 14, "bold"), bg="#2C3E50", fg="white")
result_label.pack(pady=10)
result_area = tk.Text(root, height=8, width=50, font=("Segoe UI", 12), wrap=tk.WORD, bg="#34495E", fg="#ECF0F1", bd=2, relief="solid", highlightthickness=0)
result_area.pack(pady=10)

# footer
creator_label = tk.Label(root, text="Created by Diyar", font=("Segoe UI", 10), bg="#2C3E50", fg="white", anchor="center")
creator_label.pack(side="bottom", pady=10)


root.mainloop()
