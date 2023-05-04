# Homework 14 Assignment
# Henry Penas
# 04-22-2023

import string
from html.parser import HTMLParser
from urllib.request import urlopen


class MyHTMLParser(HTMLParser):
    """
    This parser extends the built-in HTMLParser class and overrides its handle_data method to extract text data
    from HTML tags. It then removes all punctuation from the text and counts the frequency of each word.
    The frequency method returns a list of words that occur at least n times, and the dump_data method writes
    the cleaned text to a file.


    """
    def __init__(self):
        """
        Initializes MyHTMLParser
        """
        HTMLParser.__init__(self)
        self.text = ""

    def handle_data(self, data):
        """
        Adds cleaned up text data to the text variable
        :param data:
            Add data to the text variable with only clean data disregarding special characters
        :return:
            none
        """
        clean_data = ''.join(c for c in data if c.isalnum() or c.isspace())
        if not any(c in string.punctuation for c in clean_data):
            self.text += clean_data.lower() + " "

    def frequency(self, n):
        """
        Prints out words that occurred more than TWICE.
        :param n: int
            The minimum number of words that should occur to be printed
        :return:
            none
        """
        words = self.text.split()
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        print("Words that occur at least {} times:".format(n))
        for word, count in freq.items():
            if count >= n:
                print("{} : {}".format(word, count))

    def dump_data(self, filename):
        """
        Saves extracted text to a file.
        :param filename: str
            The name of the file where the extracted text will be saved
        :return:
            none
        """
        with open(filename, 'w') as file:
            file.write(self.text)


if __name__ == '__main__':
    """
    This retrieves data from the website listed below and parses the HTML content to extract
    clean text and finds the frequency of words that occurs more than twice.
    """
    link = 'https://collegeofsanmateo.edu/veterans/'
    response = urlopen(link)
    html_page = response.read().decode()

    parser = MyHTMLParser()
    parser.feed(html_page)

    parser.frequency(2)
    parser.dump_data('csmvet.txt')
