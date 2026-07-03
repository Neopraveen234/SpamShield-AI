import re 
import string

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words=set(stopwords.words("english"))
lemmatizer=WordNetLemmatizer()

def clean_text(text):

    if not isinstance(text,str):
        return ""
    
    #Lower case
    text=text.lower()

    #Remove URLs
    text=re.sub(r"http\S+|www\S+","",text)

    #Remove email address
    text=re.sub(r"\S+@\S+","",text)

    #Remove numbers
    text=re.sub(r"\d+","",text)

    #Remove punctuation
    text=text.translate(
        str.maketrans("","",string.punctuation)
    )

    #Tokenize
    words=text.split()

    #Remove stopwords
    words=[
        word
        for word in words
        if word not in stop_words
    ]

    #Lemmatization
    words=[
        lemmatizer.lemmatize(word)
        for word in words
    ]

    #Join
    return " ".join(words)