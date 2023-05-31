# CIS-117 Final Project
# Description: GUI tool for searching and retrieving information from Project Gutenberg eBooks that allows
#              users to search the local database by book titles or by their URLS and displays frequencies.
# Author: Henry Penas
# Date: 05-16-2023


import tkinter as tk
import sqlite3
from urllib import request
import re

def create_table():
    """
    Creates the database table.
    """
    conn = sqlite3.connect('book_database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS books
                 (title TEXT, url TEXT, words TEXT)''')
    conn.commit()
    conn.close()


def search_local_database():
    """
    Searches the local database for books based on the entered title and displays the frequency information.
    """
    title = title_entry.get().lower()
    frequencies = frequencies_entry.get()
    if frequencies.isdigit():
        frequencies = int(frequencies)
    else:
        display_result("Invalid input for the number of frequencies.")
        return

    try:
        conn = sqlite3.connect('book_database.db')
        c = conn.cursor()
        c.execute("SELECT title, words FROM books WHERE LOWER(title) LIKE ?", ('%' + title + '%',))
        results = c.fetchall()
        conn.close()

        if results:
            display_result("Found books in the local database:")
            for result in results:
                book_title = result[0]
                frequencies_text = result[1]
                frequencies_lines = frequencies_text.split("\n")
                limited_frequencies = "\n".join(frequencies_lines[:frequencies])
                display_result(f"Book Title: {book_title}\nFrequencies:\n{limited_frequencies}\n")
        else:
            display_result("Book not found in the local database.")
    except sqlite3.Error as e:
        display_result("Error occurred while searching the local database.")


def search_book_url():
    """
    Searches for a book based on the entered URL and retrieves frequency information for the words
    in the book.
    """
    url = url_entry.get()
    try:
        response = request.urlopen(url)
        text = response.read().decode('utf-8')
        title = re.search(r'Title:\s*(.*)', text, re.IGNORECASE)
        if title:
            title = title.group(1)
            frequencies = frequencies_entry.get()
            if frequencies.isdigit():
                frequencies = int(frequencies)
                words = frequent_words(text, frequencies)
                conn = sqlite3.connect('book_database.db')
                c = conn.cursor()
                c.execute("INSERT INTO books (title, url, words) VALUES (?, ?, ?)", (title, url, words))
                conn.commit()
                conn.close()
                display_result(words)
            else:
                display_result("Please enter a valid number for Frequencies")
        else:
            display_result("Book title not found.")
    except request.HTTPError as e:
        display_result("HTTPError occurred while retrieving book information.")
    except request.URLError as e:
        display_result("URLError occurred while retrieving book information.")
    except sqlite3.Error as e:
        display_result("Error occurred while updating the local database.")


def frequent_words(text, num_frequencies):
    """
    Extracts the most frequent words and returns them along with their frequencies.
    """
    words = re.findall(r'\b\w+\b', text)

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    result = ""
    for i in range(min(num_frequencies, len(sorted_words))):
        word, count = sorted_words[i]
        result += f"{word}: {count}\n"

    return result


def display_result(words):
    """
    Displays the given text
    """
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, words)


create_table()
window = tk.Tk()
window.title("eBook Search Tool")

# Book Title and Input Form
title_label = tk.Label(window, text="Enter Book Title:")
title_label.grid(row=0, column=0, padx=10, pady=5)
title_entry = tk.Entry(window)
title_entry.grid(row=1, column=0, padx=10, pady=5)

# Search Local Database Button
search_local_button = tk.Button(window, text="Search Local Database", command=search_local_database,
                                bg="green", fg="white")
search_local_button.grid(row=2, column=0, padx=10, pady=5)

# URL and Input Form
url_label = tk.Label(window, text="Enter Book URL:")
url_label.grid(row=0, column=1, padx=10, pady=5)
url_entry = tk.Entry(window)
url_entry.grid(row=1, column=1, padx=10, pady=5)

# Frequencies and Input Form
frequencies_label = tk.Label(window, text="Enter Number of Frequencies:")
frequencies_label.grid(row=0, column=2, padx=10, pady=5)
frequencies_entry = tk.Entry(window)
frequencies_entry.grid(row=1, column=2, padx=10, pady=5)

# Search URL Button
search_project_button = tk.Button(window, text="  Search Provided URL  ", command=search_book_url,
                                  bg="orange", fg="white")
search_project_button.grid(row=2, column=1, columnspan=1, padx=10, pady=5)

# Results
result_text = tk.Text(window)
result_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
