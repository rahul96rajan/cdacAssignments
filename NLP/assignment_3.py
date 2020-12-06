"""
Requirements:
    - nltk (tested on v3.5)
"""

from nltk.corpus import reuters, webtext, brown, stopwords
from nltk import bigrams, trigrams
from collections import defaultdict
import string


def create_corpus():
    """Removing punctuations from the sentences of corpus."""
    # Here, I am taking a text from rueters, webtext and brown corpus here.
    rr_corpus = reuters.sents() + webtext.sents() + brown.sents()
    punctuations = [p for p in string.punctuation]
    cleaned_corpus = []

    for idx in range(len(rr_corpus)):
        cleaned_corpus.append([w for w in rr_corpus[idx] if w not in punctuations])
    
    return cleaned_corpus


def create_models(corpus):
    """
    Iterates over the sents of the corpus and form two sorted dicts:
        - bigram_model
        - trigram_model
    """
    # Initilizing defaultdicts for trigrams and bigrams
    trigram_model = defaultdict(lambda: defaultdict(lambda: 0))
    bigram_model = defaultdict(lambda: defaultdict(lambda: 0))

    for sentence in corpus:
        # creating bigram dict
        for w1, w2 in bigrams(sentence, pad_right=True, pad_left=True):
            bigram_model[w1][w2] += 1
        
        # creating trigram dict
        for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
            trigram_model[(w1, w2)][w3] += 1
        
        
    # Sorting the dicts: trigram_model, bigram_model based on the count of words
    for k1, v1 in bigram_model.items():
        sorted_dict = {k2: v2 for k2,v2 in sorted(v1.items(),
                                                  key=lambda item: item[1])}
        bigram_model[k1] = sorted_dict

    for k1, v1 in trigram_model.items():
        sorted_dict = {k2: v2 for k2,v2 in sorted(v1.items(),
                                                  key=lambda item: item[1])}
        trigram_model[k1] = sorted_dict
    
    return bigram_model, trigram_model


def predict_word(sentence, bi_model, tri_model):
    """Predict 3 possible words in the sentence sequence."""
    sentence = sentence.split()
    sent_len = len(sentence)
    
    posssible_words = []
    for i in [-1, -2, -3]:  #picks top 3 words; range(-1, -4, -1)
        if sent_len<2:
            word = list(bi_model[sentence[0]])[i]
            posssible_words.append(word)
        else:
            word = list(tri_model[sentence[-2:][0], sentence[-2:][1]])[i]
            posssible_words.append(word)
    return posssible_words


def print_sentence(pos_words, inp_sent):
    """Printing autocomplete suggetions"""
    print("Suggetions: ")
    for w in pos_words:
        print('\t' + inp_sent + ' ' + w)


def train_model():
    """Creates the training corpus and trains the bigram and trigram dict."""
    corpus = create_corpus()
    bimod, trimod = create_models(corpus)
    return bimod, trimod


def user_interactor():
    print("Welcome!")
    print("Trainig model..")
    bimod, trimod = train_model()
    print("Trainig Complete.")
    
    flag = True
    while(flag):
        sent = input("Please enter a sentence: ")
        pos_words = predict_word(sent, bimod, trimod)
        print_sentence(pos_words, sent)
        choice = input("\nWould you like to continue (Y/N): ").lower().strip()
        flag = False if choice =='n' else True


if __name__ == "__main__":
    user_interactor()
