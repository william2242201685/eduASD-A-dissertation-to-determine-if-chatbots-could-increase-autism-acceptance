#FreeBirdsCrew (2020) CHATBOTS - Using Natural Language Processing and Tensorflow. Available At: https://github.com/FreeBirdsCrew/AI_ChatBot_Python/blob/master/Contextual%20Chatbot%20-%20NLP%20and%20Tensorflow.ipynb [Accessed: 15/04/2023]
#AI Studio (2021) Web Scrapping Chatbot with Python. Available At: https://www.youtube.com/watch?v=Je7M_K3IANI [Accessed: 25/03/2023]


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=Warning)


# In[2]:


from flask import Flask, render_template, request


# In[3]:


import json
import math
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import pickle
import random
import re
import requests
import shutil
import string
import sys
import tensorflow as tf
import tflearn
import webbrowser


# In[4]:


print(tf.version.VERSION)


# In[5]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[6]:


from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


# In[7]:


from flask import Flask, render_template, request


# In[8]:


stdout = sys.stdout
sys.stdout = None
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
sys.stdout = stdout


# In[9]:


ERROR_THRESHOLD = 0.50


# In[10]:


def get_alt_intents():
    try:
        altintents = open("./resources/scraped_intents/intents.txt", "r")
    except:
        print("Error reading intents file")
        sys.exit('Closing Program')
    try:
        altResponse = open("./resources/scraped_intents/response.txt", "r")
    except:
        print("Error reading intents file")
        sys.exit('Closing Program')
        
    return str(altintents.readline()), str(altResponse.readline())


# In[11]:


def generate_alt_response(human, alt_res):
    bot_response = ""
    alt_sen.append(human)
    
    stopwords = nltk.corpus.stopwords.words('english')
    
    word_vectorizer = TfidfVectorizer(tokenizer = get_processed_text, stop_words = stopwords)
    word_vectors = word_vectorizer.fit_transform(alt_sen)
    similar_vector_values = cosine_similarity(word_vectors[-1], word_vectors)
    similar_sentence_number = similar_vector_values.argsort()[0][-2]
    
    matched_vector = similar_vector_values.flatten()
    matched_vector.sort()
    vector_matched = matched_vector[-2]
    
    if vector_matched == 0:
        bot_response = bot_response + "I am sorry, I don't understand"
        return bot_response
    else:
        bot_response = bot_response + alt_res[similar_sentence_number]
        print(alt_sen[similar_sentence_number])
        return bot_response


# In[12]:


def gen_alt_greet_res(greeting):
    for token in greeting.split():
        if token.lower() in greeting_inputs:
            return random.choice(alt_greeting_responses)


# In[13]:


def get_processed_text(document):
    return perform_lemm(nltk.word_tokenize(document.lower().translate(pr)))


# In[14]:


def perform_lemm(tokens):
    return[wnlem.lemmatize(token)  for token in tokens]


# In[15]:


def create_directory():
  dir = ["./tflearn_logs", "./cbmodel"]
  try:
    for i in dir:
      if os.path.exists(i):
        shutil.rmtree(i)
      else:
        print(i, " already deleted")
  except:
    print("Cannot Delete Directories")

  try:
    os.mkdir("./cbmodel")
  except:
    print("Cannot Add ./cbmodel Directory")


# In[16]:


def read_intent():
  try:
    with open("./resources/scraped_intents/intents.json") as chatbot_library:
      intents = json.load(chatbot_library)
    wrd, lbl, patn = get_word(intents)

    return wrd, lbl, patn, intents

  except:
    print("Intents file not found! Please Make Sure You Have Included The Folders resources/scraped_intents and Place The Provided intents.json Inside The Scraped_Intents Folder! \n\nAlternatively, open the resources folder and run the scrape.ipynb file to scrape the intents")


# In[17]:


def get_word(intents):
  wrd = []
  #classes
  lbl = []
  #doc
  patn = []

  for token in intents["intents"]:
    for i in token["patterns"]:
      txt = nltk.word_tokenize(i)
      wrd.extend(txt)
      patn.append((txt, token['tag']))
      if token['tag'] not in lbl:
        lbl.append(token['tag'])

  wrd = [lemmatizer.lemmatize(w.lower()) for w in wrd if w not in "?"]
  wrd = sorted(list(set(wrd)))
  lbl = sorted(list(set(lbl)))

  return wrd, lbl, patn


# In[18]:


def train_assain(patn, wrd, lbl):
  tr = []
  for pat in patn:
    op = []
    op_emp = [0] * len(lbl)
    bg = []
    pw = pat[0]
    pw = [lemmatizer.lemmatize(i.lower()) for i in pw]

    for j in wrd:
      if j in pw:
        bg.append(1)
      else:
        bg.append(0)
    row = list(op_emp)
    row[lbl.index(pat[1])] = 1

    tr.append([bg, row])

  return tr


# In[19]:


def assigning_x_y(train):
  random.shuffle(train)
  train = np.array(train)
  x = list(train[:, 0])
  y = list(train[:, 1])

  return x, y


# In[20]:


def classify(human):
  results = model.predict([bow(human, wrd)])[0]
  results = [[i, r] for i, r in enumerate(results) if r > ERROR_THRESHOLD]
  results.sort(key=lambda x: x[1], reverse=True)
  return_list = []
  for r in results:
    return_list.append((lbl[r[0]], r[1]))

  print(return_list)

  return return_list


# In[21]:


def bow(userin, wrd):
    ui = clean_input(userin)
    bg = [0] * len(wrd)
    for s in ui:
      for i, w in enumerate(wrd):
        if w == s:
          bg[i] = 1
 
    return np.array(bg)


# In[22]:


def clean_input(userin):
  ui = nltk.word_tokenize(userin)
  ui = [lemmatizer.lemmatize(word.lower()) for word in ui]
  return ui


# In[23]:


def responder(result):
  if result:
    for i in intents['intents']:
      if i['tag'] == result[0][0]:
        return random.choice(i['responses'])
    result.pop(0)
  else:
    return "I'm sorry? Can you repeat that?"


# In[24]:


def word_change(human):
    inp = ""
    
    for i in human.split():
        if i == "symptoms" or i == "symptom":
            i = "signs"
        elif i == "vaccination" or i == "vaccinations":
            i = "vaccine"
        elif i == "identified":
            i = "diagnosed"
        elif i == "employment" or i == "employed":
            i = "job"
        elif i == "medication" or i == "medicine":
            i = "treatment"
        elif i == "medication" or i == "medicine":
            i = "treatment"
                
        inp = inp + i + " "

    if inp != "":
        human = inp
    
    human = re.sub(r'\s+', ' ',re.sub(r'\[[0-9]*\]', ' ', human))
    human = human.replace("-", " ")
    human = human.replace("adi r", "adir")
    
            
    return human.rstrip()


# In[25]:


create_directory()


# In[26]:


wrd, lbl, patn, intents = read_intent()


# In[27]:


train = train_assain(patn, wrd, lbl)


# In[28]:


x, y = assigning_x_y(train)


# In[29]:


hiddenLayerNode = math.ceil(((len(x[0]) + len(y[0])) / 2))
net = tflearn.input_data(shape=[None, len(x[0])])
net = tflearn.fully_connected(net, hiddenLayerNode)
net = tflearn.fully_connected(net, math.ceil((hiddenLayerNode / 2)))
net = tflearn.fully_connected(net, len(y[0]), activation='softmax')
net = tflearn.regression(net)


# In[30]:


model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')


# In[31]:


model.fit(x, y, n_epoch=200, batch_size=16, show_metric=True)


# In[32]:


alt_scraped_data, alt_scraped_res = get_alt_intents()


# In[33]:


alt_hard_sen = alt_sen = nltk.sent_tokenize(alt_scraped_data)
alt_res = nltk.sent_tokenize(alt_scraped_res)
alt_words = nltk.word_tokenize(alt_scraped_data)
wnlem = nltk.stem.WordNetLemmatizer()


# In[34]:


pr = dict((ord(punctuation), None) for punctuation in string.punctuation)


# In[35]:


greeting_inputs = ("hey", "hello", "hi")
alt_greeting_responses = ["hello there", "testy hello 1", "testy hello 2"]


# In[36]:


app = Flask(__name__)


# In[37]:


@app.route('/get')
def userChat():
    myinp = human = request.args.get('msg')
    human = str(human.lower())
    human = word_change(human)
    result = classify(human)
    response = responder(result)
    response = str(response)
    
    if response == "I'm sorry? Can you repeat that?":
        syno = ""
        res = ""

        if myinp == "what is autism":
            res = str(alt_hard_sen[5])
            return res
        else:
            if gen_alt_greet_res(human) != None:
                res = str(gen_alt_greet_res(human))
                return res
            else:
                for i in human.split():
                    for syn in wordnet.synsets(i):
                        syno += syn.name() + " "
                    syno = i + " " + syno + " "
                human = syno
                response = str(generate_alt_response(human, alt_res))
                alt_sen.remove(human)
        

    return response


# In[38]:


@app.route('/')
def index():
    return render_template('index.html')


# In[ ]:


if __name__ == "__main__":
    url = "http://127.0.0.1:5000/"
    webbrowser.open(url, new=0, autoraise=True)
    app.run()


# In[ ]:




