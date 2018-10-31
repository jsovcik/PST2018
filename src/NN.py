import os.path
import keras.layers as kl
import keras.models as km

# from keras.layers import Convolution1D, Flatten, Dropout, Dense
# from keras.layers.embeddings import Embedding
# from keras.models import Sequential

WORKING_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_DIR = os.path.split(WORKING_DIR)[0]
DATA_DIR = os.path.join(PROJECT_DIR, "data")
print(DATA_DIR)

#la longueur maximum des texte
max_review_length = 1600

#le nombre de mots connus en francais
top_words = 10000

embedding_vecor_length = 300

model = km.Sequential()
model.add(kl.Embedding(top_words, embedding_vecor_length, input_length=max_review_length))
model.add(kl.Convolution1D(64, 3, padding='same'))
model.add(kl.Convolution1D(32, 3, padding='same'))
model.add(kl.Convolution1D(16, 3, padding='same'))
model.add(kl.Flatten())
model.add(kl.Dropout(0.2))
model.add(kl.Dense(180,activation='sigmoid'))
model.add(kl.Dropout(0.2))
model.add(kl.Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

