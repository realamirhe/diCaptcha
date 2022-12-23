import random
import urllib2

from ai.model.pos_detector import pos_pipeline


def sort_tuple(tup):
    tup.sort(key=lambda x: x[1], reverse=True)
    return tup


def remove_duplicate_tuples(token_scores):
    return list(dict(reversed(token_scores)).items())


def nlp_tags(prompt):
    result = {'pos': [], 'neg': [], 'gold': []}
    positive_words = set()
    banned_words = ['hyper', 'super', 'style', 'dynamic', 'detailed', 'rendered', 'unreal', 'octane', 'ultra',
                    'high', 'contrast', 'ambient', 'trending', 'wide', 'pose', 'concept', 'unity']

    for o in pos_pipeline(prompt):
        if o['entity'] in ["NOUN", "VERB", "ADJ"]:
            word = prompt[o['start']:].split(' ')[0].lower()
            if (len(word) > 3) and (word[-2:] != 'ed') and (word not in banned_words):
                positive_words.add((word, str(o['score'])))

    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = urllib2.urlopen(word_site)
    txt = response.read()
    # TODO: read from spacy or nltk
    english_words = txt.splitlines()
    filtered_words = [word for word in english_words if 3 < len(word) < 9]
    negative_words = set(random.sample(filtered_words, 3))
    new_positive_words = []
    for gt_word in prompt.split(' '):
        for pos_word in positive_words:
            if gt_word == pos_word[0]:
                new_positive_words.append((pos_word[0], pos_word[1]))

    result['pos'] = random.sample(remove_duplicate_tuples(new_positive_words), 4)
    result['neg'] = list(negative_words)

    return result
