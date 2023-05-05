# Homework 14 Assignment
# Henry Penas
# 04-27-2023

import string
from html.parser import HTMLParser
from urllib.request import urlopen
import re

import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox


class MyHTMLParser(HTMLParser):
    def __init__(self):
        """
        Initializes MyHTMLParser
        """
        HTMLParser.__init__(self)
        self.text = ""
        self.emails = []

    def handle_data(self, data):
        """
        Adds cleaned up text data and collects emails.
        """
        clean_data = ''.join(c for c in data if c.isalnum() or c.isspace())
        if not any(c in string.punctuation for c in clean_data):
            self.text += clean_data.lower() + " "
        # use regex to find emails in data
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, data)
        for email in emails:
            self.emails.append(email)

    def collect_emails(self):
        """
        Returns a list of collected emails.
        """
        return self.emails


class MyGUI:
    """
    This creates a GUI for the MyHTMLParser class.
    """

    def __init__(self, master):
        self.master = master

        self.master.configure(background='#8a7b70')
        self.master.title("Email Searcher")
        self.master.geometry("600x400")

        self.url_label = tk.Label(self.master, background="#8a7b70", text="Please enter the URL:", font="Arial, 13",
                                  fg="white")
        self.url_label.pack(pady=10)

        self.url_entry = tk.Entry(self.master, width=75, background="#ebe9e7")
        self.url_entry.pack()

        self.collect_button = tk.Button(self.master, background="#c4bdb7", fg="black", text="Search Emails",
                                        relief="raised", command=self.collect_emails)
        self.collect_button.pack(pady=5)

        self.emails_label = tk.Label(self.master, background="#8a7b70", fg="white", font="Arial, 13",
                                     text="Collected Emails:")
        self.emails_label.pack(pady=5)

        self.emails_text = scrolledtext.ScrolledText(self.master, width=60, height=10, background="#ebe9e7")
        self.emails_text.pack()

    def collect_emails(self):
        """
        Collects emails from the entered URL and displays them in the GUI.
        """
        link = self.url_entry.get()
        response = urlopen(link)
        html_page = response.read().decode()

        parser = MyHTMLParser()
        parser.feed(html_page)

        emails = parser.collect_emails()

        if emails:
            for email in emails:
                self.emails_text.insert(tk.END, email + "\n")
        else:
            messagebox.showerror("Error: 101", "There are no emails found on this page.")


root = tk.Tk()
root.configure()
gui = MyGUI(root)
root.mainloop()
