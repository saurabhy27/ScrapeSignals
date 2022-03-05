import string

from nltk.corpus import stopwords
from rake_nltk import Rake

word = stopwords.words("english")

r = Rake(stopwords=word, punctuations=string.punctuation)


def extaract_rake_keywords(data):
    r.extract_keywords_from_text(data)
    return r.get_ranked_phrases_with_scores()
