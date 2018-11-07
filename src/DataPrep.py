import os
import nltk
#nltk.download()

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_DIR = os.path.split( PROJECT_DIR)[0]
DATA_DIR = os.path.join(PROJECT_DIR, "data")
TRAINING_FILE = os.path.join(DATA_DIR, "allocine_train.tsv")


# with open(TRAINING_FILE, "r") as file:
#     data = file.read()
#     # split into words
#
#     tokens = nltk.word_tokenize(data)
#     # stemming of words
#     from nltk.stem.porter import PorterStemmer
#
#     # convert to lower case
#     tokens = [w.lower() for w in tokens]
#     # remove punctuation from each word
#     import string
#
#     table = str.maketrans('', '', string.punctuation)
#     stripped = [w.translate(table) for w in tokens]
#     # remove remaining tokens that are not alphabetic
#     words = [word for word in stripped if word.isalpha()]
#     # filter out stop words
#     from nltk.corpus import stopwords
#
#     stop_words = set(stopwords.words('french'))
#     porter = PorterStemmer()
#     stemmed = [porter.stem(word) for word in tokens]
#     dictionnary = {}
#     count = 0
#     for word in stemmed :
#         if word not in dictionnary:
#             if word.isalpha():
#                 dictionnary[count] = word
#                 count +=1
#     print (dictionnary)


def padding_length(file):
    with open(file, "r") as file:
        max = 0
        for data in file.readlines():
            tokens = nltk.word_tokenize(data)
            length = len(tokens)
            if length > max :
                max = length
        return max


def list_doc(file):
    with open(file, "r") as file:
        comments = []
        positivity = []
        lines = file.readlines()
        for line in lines[1:]:
            split_line = line.split("\t")
            print(split_line)
            comments.append(split_line[3])
            positivity.append(split_line[2])
    return comments, positivity



print(list_doc(TRAINING_FILE))