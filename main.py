import string
from collections import Counter
from string import digits
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
import os


# =========================================== importing data ====================================================


# -----------------positif comment-----------------------
# save the folder Path where the data is
path = r"C:\Users\ACER\PycharmProjects\sentimentAnalysis\pos"

# Change the directory
os.chdir(path)

# create the variable text which will contain all our data
text = ""

# iterate through all file and put the text file on our variable 'text'
file_name = os.listdir()
for i in range(10):  # we choose to use 100 file
    if file_name[i].endswith(".txt"):
        file_path = f"{path}\{file_name[i]}"
        text = open(file_path, encoding="utf-8").read() + " " + text


# -----------------negatif comment-----------------------
# save the folder Path where the data is
path = r"C:\Users\ACER\PycharmProjects\sentimentAnalysis\neg"

# Change the directory
os.chdir(path)

# iterate through all file and put the text file on our variable 'text'
file_name = os.listdir()
for i in range(10):  # we choose to use 10 file
    if file_name[i].endswith(".txt"):
        file_path = f"{path}\{file_name[i]}"
        text = open(file_path, encoding="utf-8").read() + " " + text

#print(text)


# ========================================== preparing data ====================================================

# convert all uppercase letters to lowercase
lower_case = text.lower()

# Removing punctuations
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Removing numbers
cleaned_text = lower_case.translate(str.maketrans('', '', digits))

# splitting text into words using word_tokenize in NLTK library
tokenized_words = word_tokenize(cleaned_text, "english")

# Removing Stop Words using stopwords.words in NLTK library
word_stopwords = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        word_stopwords.append(word)
#print(word_stopwords)

#stemming every word
lancaster=LancasterStemmer()
stemming_words=[]
for word in word_stopwords:
    word = lancaster.stem(word)
    stemming_words.append(word)

# Lemmatization - From plural to single + Base form of a word (example better-> good)
final_words = []
for word in stemming_words:
    word = WordNetLemmatizer().lemmatize(word)
    final_words.append(word)

#print(final_words)
# ================================ Analyse sentiment on the data  ====================================================

# aplay the sentiment analysis on our data by using the SentimentIntensityAnalyzer() in NLTK
def sentiment_analyse(sentiment_text):
    print("the final sentiment is : ")
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    if score['neg'] > score['pos']:
        print("Negative Sentiment")
    elif score['neg'] < score['pos']:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")


sentiment_analyse(cleaned_text)


# extract all the sentiment in the text and count them
emotion_list = []
with open(r'C:\Users\ACER\PycharmProjects\sentimentAnalysis\emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

# print(emotion_list)
w = Counter(emotion_list)
print(w)


# Plotting the emotions on the graph
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
