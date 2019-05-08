
import nltk
#nltk.download('punkt')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#nltk.download('wordnet')
#nltk.download('stopwords')
#nltk.download('brown')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import ne_chunk, pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
#from nltk.stem import PorterStemmer

#stemmer = PorterStemmer()

lemmatizer = WordNetLemmatizer()

text = "Hello this is a simple test. This is success"

#Tokenize to sentence
#sents = sent_tokenize(text)

#Tokenize to words
#words = word_tokenize(text)

#print(nltk.wordpunct_tokenize(sample_sentence))
#Print parts of speech of the tokenized words
'''print(nltk.pos_tag(words))'''

#Tokenizing and Printining Parts of Speech for a real life example
'''
def entities(text):
    return(ne_chunk(
        pos_tag(
            word_tokenize(text))
    ))
tree = entities("“You talk about business, this is the group. And we’re so honoured to have you. And we’re gonna be discussing later on some of the ideas you may have to, as the expression goes, make America great again.”")
tree.pprint()'''

#Lemmatize testing with a sample word

#lemma_test_text = "ran"
#print(lemmatizer.lemmatize(lemma_test_text, pos="v"))

#removing stopwords
sample_sentence = "The terrorists tried to blow up the railroad station."
'''sample_sentence = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
print(sample_sentence.similar('woman'))'''

#conversion to lower case for effective filtering
sample_sentence = sample_sentence.lower()

#using regular expression to filter out punctuation and token the sentence
tokenizer = RegexpTokenizer(r'\w+')
words = tokenizer.tokenize(sample_sentence)

#setting stopwords
stop_words = set(stopwords.words("english"))

#words = stemmer.stem(words)

#lemmatizing and then removing the stopwords
words = [lemmatizer.lemmatize(w) for w in words]
filtered_sample = [w for w in words if not w in stop_words]
lst = []
lstn = []
lstv = []
lsta = []
lsts = []
lstr = []
print(lst)
print(type(lst))
for i in range (0, len(filtered_sample)):
   
    lstv.append(lemmatizer.lemmatize(filtered_sample[i], pos="v"))
    lstn.append(lemmatizer.lemmatize(filtered_sample[i], pos="n"))
    lsta.append(lemmatizer.lemmatize(filtered_sample[i], pos="a"))
    lsts.append(lemmatizer.lemmatize(filtered_sample[i], pos="s"))
    lstr.append(lemmatizer.lemmatize(filtered_sample[i], pos="r"))

#print(lst)
print("BREAK")
print(filtered_sample)
lst1 = []
print("break")
print(lstn)
print("break")
print(lstv)
print("break")
print(lsta)
print("break")
print(lstr)
print("break")
print(lsts)
for j in range(0, len(lstr)):
    lst.append(lstr[j])
'''for i in range (0, len(lst)):
    for j in range(0, len(lstv))::
        if(lst[i]==lstv[j]):
            continue
        else:
            lst.append(lstv[j])'''
lst2 = [1, 2, 3, 4]
lst3 = [1, 2, 5, 6]
for i in range(0, len(lst2)):
    for j in range(0, len(lst3)):
        print(lst2[i])
        print(lst3[j])
        if lst2[i]!=lst3[j]:
            lst2.append(lst3[j])
            print(lst2)
        
#lst.append(lstv)
#lst.append(lstr)
#print(lst)