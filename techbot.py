# -*- coding: utf-8 -*-
"""TechBot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1v6gqQfg0SrgVEqpZ76ralJnmEMXXQ5HK
"""

from google.colab import drive
drive.mount('/content/drive')

"""# Importing Required Libaries:"""

import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
import random
import joblib

"""# Load Dataset:"""

with open('/content/drive/MyDrive/NLP/chatbots/chatbot.json','r') as file:
  data=json.load(file)

"""# Extract Patterns and Tags:"""

patterns=[]
tags=[]
responses={}

for intent in data['intents']:
  for pattern in intent['patterns']:
    patterns.append(pattern)
    tags.append(intent['tag'])
  responses[intent['tag']]=intent['responses']

"""# Convert Labels into numerical Values:"""

label_encoder=LabelEncoder()
encoded_tags=label_encoder.fit_transform(tags)
joblib.dump(label_encoder, "/content/drive/MyDrive/NLP/chatbots/label_encoder.joblib")

"""# Tokenize Text Data:"""

tokenizer=Tokenizer()
tokenizer.fit_on_texts(patterns)
joblib.dump(tokenizer, "/content/drive/MyDrive/NLP/chatbots/tokenizer.joblib")
sequences=tokenizer.texts_to_sequences(patterns)
max_length=max(len(seq) for seq in sequences)
padded_sequences=pad_sequences(sequences,maxlen=max_length,padding="post")

"""# Build LSTM Model:"""

model=tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(tokenizer.word_index)+1,output_dim=16,input_length=max_length),
    tf.keras.layers.LSTM(32),
    tf.keras.layers.Dense(16,activation="relu"),
    tf.keras.layers.Dense(len(set(tags)),activation="softmax")
])

model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])

model.fit(padded_sequences,np.array(encoded_tags),epochs=200,batch_size=8)

"""# Save the model in h5 file:"""

model.save('/content/drive/MyDrive/NLP/chatbots/chatbot.h5')

model=tf.keras.models.load_model('/content/drive/MyDrive/NLP/chatbots/chatbot.h5')

"""# Prediction:"""

def chatbot_conversation():
  print("TechBot: Hello How can I help you? (Type 'bye'to exit)" )

  while True:
    user_input=input("You:")

    if user_input.lower()=="bye":
      print("TechBot: Have Goodday Bye")
      break

    seq=tokenizer.texts_to_sequences([user_input])
    padded=pad_sequences(seq,maxlen=max_length,padding="post")
    prediction=model.predict(padded)

    tag=label_encoder.inverse_transform([np.argmax(prediction)])[0]
    response=random.choice(responses[tag])
    print("TechBot:",response)


#Start the conversation:
chatbot_conversation()

