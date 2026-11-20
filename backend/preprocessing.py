def remove_html(tags):
    import re
    clean = re.compile('<.*?.')
    return re.sub(clean, '', tags)

#2. Convert everything to lower
def lower_case(text):
    return text.lower()

#Removing special char
def remove_special(text):
    if not isinstance(text, str):
        return ""

    x = ""
    for i in text:
        if i.isalnum():
            x += i
        else:
            x += " "

    return x

from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def remove_stopwords(text):
    x = []

    for i in text.split():
        if i not in stop_words:
            x.append(i)

    return " ".join(x)


#Perform stemming
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def stem_words(text):
    y = []

    for i in text.split():
        y.append(ps.stem(i))

    return " ".join(y)

def join_back(text):
    return "".join(text)


def clean_text(text):
    text = remove_html(text)
    text = lower_case(text)
    text = remove_special(text)
    text = remove_stopwords(text)
    text = stem_words(text)
    text = join_back(text)

    return text

def preprocess_text(x):
    return [clean_text(text) for text in x]