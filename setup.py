import os
import nltk
#nltk.download()

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))

DATA_DIR = os.path.join(PROJECT_DIR, "data")
TRAINING_FILE = os.path.join(DATA_DIR, "allocine_train.tsv")

dictionnary = set


with open(TRAINING_FILE, "r") as file:
    for data in file.readlines():
        # split into words

        tokens = nltk.word_tokenize(data)
        # stemming of words
        from nltk.stem.porter import PorterStemmer

        # convert to lower case
        tokens = [w.lower() for w in tokens]
        # remove punctuation from each word
        import string

        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in tokens]
        # remove remaining tokens that are not alphabetic
        words = [word for word in stripped if word.isalpha()]
        # filter out stop words
        from nltk.corpus import stopwords

        stop_words = set(stopwords.words('french'))
        porter = PorterStemmer()
        stemmed = [porter.stem(word) for word in tokens]
        dictionnary = {}
        count = 0
        # for word in stemmed :
        #     if word not in dictionnary:
        #         if word.isalpha():
        #             dictionnary[count] = word
        #             count +=1
        print (words[:100])


