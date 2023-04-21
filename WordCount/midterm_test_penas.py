# Midterm Programming Assignment
# Henry Penas
# 03/24/2023

def word_count(text):
    """
    Receives a text as a parameter and returns the number of words in the text
    Parameters: Input text
    Returns: The number of words in the text
    """
    words = text.lower().split()
    words = [word.strip(".,!?\"'-") for word in words]
    return len(words)


def unique_word_count(text):
    """
    Receives a text as a parameter and returns the number of unique words (without repetitions & punctuations)
    Parameters: The input text
    Returns: The number of unique words in the text.
    """
    words = text.lower().split()
    words = [word.strip(".,!?\"'-") for word in words]
    unique_words = set(words)
    return len(unique_words)


def sentence_count(text):
    """
    Receives a text and returns the number of sentences
    Parameters: The input text
    Returns: The number of sentences in the text
    """
    sentences = text.split('.')
    return len(sentences)


def frequencies(text, min_frequency):
    """
    Prints a list of words with its corresponding frequency in the text
    Parameters: The input text + The minimum frequency that a word must have to be printed.
    """
    words = text.lower().split()
    words = [word.strip(".,!?\"'-") for word in words]
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    for word, count in word_counts.items():
        if count >= min_frequency:
            print(f"{word}: {count}")


if __name__ == "__main__":
    """
    Initialized text with the following below
    Prints all functions
    """
    text = "The governing wisdom about writing sentences says not to repeat. Repetition is bad. Repetition is sloppy. Writers are encouraged to consult a thesaurus and change up that pesky offending word. But is this really true? Literature is full of repetition. Literary writers constantly use the literary device of repeated words. I think the only type of repetition which is bad is sloppy repetition. Repetition which is unintentional, which sounds awkward. If you repeat on purpose, repetition is gorgeous. I mean, think about music. Music is all about repetition and patterns. If you didn’t have repetition in music, it would all just be noise."

    print(word_count(text))
    print(unique_word_count(text))
    print(sentence_count(text))
    """
    Frequency Test: Only prints words that occur at least 3 times
    """
    frequencies(text, 3)

