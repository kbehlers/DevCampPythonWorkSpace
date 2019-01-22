import string
from collections import Counter
import timeit

def remove_punctuation(target_string, retain_hyphens=True):
    """Accepts a string, removes punctuation (keeps hyphens by default), returns cleansed string"""
    #Python string.punctuation constant and unicode lookups
    punctuation_to_remove_list = [
            string.punctuation,
            "\N{Left Double Quotation Mark}",
            "\N{Right Double Quotation Mark}",
            "\N{Left Single Quotation Mark}",
            "\N{Right Single Quotation Mark}",
        ]

    punctuation_to_remove = ''.join(punctuation_to_remove_list)
    if retain_hyphens:
        #Preserve the hyphen char by removing it from the punctuation_to_remove string
        punctuation_to_remove = punctuation_to_remove.replace("-", '')
    #maketrans below maps empty string to empty string as placeholder, and then maps third argument to None, removing all punctuation
    cleansed_string = target_string.translate(str.maketrans('','',punctuation_to_remove))
    return cleansed_string

def parse_file_to_word_counter(filename):
    """Given a filename, return a Counter object of lowercased words stripped of punctuation"""
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = filename + " not found."
        print(msg)
    else:
        contents = remove_punctuation(contents)
        words = contents.lower().split()
        word_counter = Counter(words)
        return word_counter

def most_common_words(filename, results_to_return=3):
    """Counts the number of words in the file, 
    return a list of the n most common elements and their counts from the most common to the least
    returns the top 3 results by default"""
    word_counts = parse_file_to_word_counter(filename)
    # #Uncomment to get output to terminal of what is being stored
    # for key, value in word_counts.items():
    #     print("Key: " + str(key), "Value: " + str(value))
    return word_counts.most_common(results_to_return)

def count_word(filename, word_to_count):
    """Counts occurrences of word_to_count in the file, and return count"""
    word_counts = parse_file_to_word_counter(filename)
    formatted_word = remove_punctuation(word_to_count.lower())
    return word_counts[formatted_word]

filename="C:/Users/Copy/Downloads/frankenstein.txt"
# print(most_common_words(filename))
# print(count_word(filename, "Frankenstein"))


SETUP_CODE = '''
import string
from collections import Counter
from __main__ import most_common_words, count_word, parse_file_to_word_counter, remove_punctuation
filename = "C:/Users/Copy/Downloads/frankenstein.txt"
'''

TEST_CODE = '''
most_common_words(filename)
'''

print(timeit.repeat(
    setup = SETUP_CODE,
    stmt = TEST_CODE,
    repeat=1,
    number = 1))
