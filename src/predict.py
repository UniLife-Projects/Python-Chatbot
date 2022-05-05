from tensorflow.keras.models import load_model
import pickle
from theFlickrApi import *

import random
import numpy as np
from wikiAPI import *
import json

import nltk
nltk.download('punkt')
nltk.download('omw-1.4')
nltk.download('vader_lexicon')
nltk.download('wordnet')
from nltk.sentiment import SentimentIntensityAnalyzer as mood
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.JSON').read())
words = pickle.load(open('words.pk1', 'rb'))
classes = pickle.load(open('classes.pk1', 'rb'))
model = load_model('chatbot_model.h5')


responses_outside_topics = ["I will connect you with our customer support team for further details.", "Could you please repeat that?", "I did not get that.", "I am not sure we have what you are looking for.", "Our customer support team will get in touch with you soon."]

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):  # convert sentence into a bag of word
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)  # initial bag with just 0z
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_classes(sentence):
    bow = bag_of_words(sentence)  # create a bag of words
    # predicts classes based on the bag of words
    res = model.predict(np.array([bow]))[0]
    
    ERROR_THRESHOLD = 0.25  # certin threshold so not much uncertainty
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        # first one is the index next one is the result
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    
    return return_list  # return list full of intents and probabilities


def get_response(intents_list, intents_json,message=""):

    list_of_intents = intents_json['intents']

    mark = intents_list[0]['intent']

    result = random.choice(responses_outside_topics) ## default-output

    sign = str(intents_list)
    
    for i in list_of_intents:
        if i['topics'] == mark:

            print(mark)

            if mark=='shoes' or mark == 'shorts' or mark=='jeans':
                
                listed_Links=getFlickredAfterMath(mark)
                result=random.choice(listed_Links)
            elif mark=='clothes':
                
                listed_Links=getFlickredAfterMath('clothes')
                result=random.choice(listed_Links)
            elif mark=="who what" or mark=="when" or mark=="why" or mark=="how":
                
                res=getWikiConclusion(message)
                if len(res)>1:
                    result=res[0]
                
            else:
            # assigns output messages to be printed
                
                result = random.choice(i['outputs'])
            break
    
    return result


def get_mood(user_input):  # sentiment analysis to add empathy to responses
    empathizer = mood()
    return empathizer.polarity_scores(user_input)


print("Yeaaaaah! Let's go. The bot is running babyyyy!")