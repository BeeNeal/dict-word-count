# Further Study
import re


def read_file(filename):
    """opens text file and returns a formatted list of words"""
    words = re.findall(r'\w+', open(filename).read().lower())
    #filename.close()  # is this needed?
    return words


def get_count_of_words(word_list):
    """Given a word list, returns a dictionary of the counts of each word."""
    count_of_words = {}
    for word in word_list:
        count_of_words[word] = count_of_words.get(word, 0) + 1
    return count_of_words


def print_key_value_pairs(dictionary):
    """given a dictionary prints all key value pairs """
    for word, count in dictionary.iteritems():
        print word, count
    # for word in dictionary:
        # print word, dictionary[word]

word_list = read_file("twain.txt")
#print word_list

count = get_count_of_words(word_list)
print_key_value_pairs(count)



# Assignment
# # put your code here.
# def read_file(filename):
#     """opens text file and returns a formatted list of words"""
#     words = []
#     with open(filename) as text_file:
#         for line in text_file:
#             line_words = line.rstrip().split()
#             words.extend(line_words)
#     return words


# def get_count_of_words(word_list):
#     """Given a word list, returns a dictionary of the counts of each word."""
#     count_of_words = {}
#     for word in word_list:
#         count_of_words[word] = count_of_words.get(word, 0) + 1
#     return count_of_words


# def print_key_value_pairs(dictionary):
#     """given a dictionary prints all key value pairs """
#     for word, count in dictionary.iteritems():
#         print word, count
#     # for word in dictionary:
#         # print word, dictionary[word]

# word_list = read_file("twain.txt")
# #print word_list

# count = get_count_of_words(word_list)
# print_key_value_pairs(count)
