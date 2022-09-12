import re
import string


def GetTextFromFile(book_fn):
    with open(book_fn, "r", encoding='utf-8') as f:
        text = f.read()
    text = remove_newlines(text)
    text = remove_extra_spaces(text)
    return text


def GetStopWords(stopwords_fn):
    with open(stopwords_fn, "r") as f:
        stopwords = f.readlines()
    return stopwords


def GetCleanText(text, stopwords):
    text_clean = remove_punctuation(text)
    text_clean = remove_numbers(text_clean)
    text_clean = remove_stopwords(text_clean, stopwords)
    text_clean = remove_extra_spaces(text_clean)
    text_clean = text_clean.lower()
    return text_clean


def GetUniqueWordList(text_clean):
    text_words = tokenize_words(text_clean)
    text_words = list(get_all_words(text_words))
    return text_words


def GetChapterTextList(text, stopwords):
    chapters = split_chapters(text)
    chapters = [GetCleanText(c, stopwords) for c in chapters]
    return chapters


def GetChapterWordList(chapters):
    return [GetUniqueWordList(c) for c in chapters]

##################################################################################


def remove_newlines(text):
    return re.sub(r'\n', '', text)


def remove_extra_spaces(text):
    return re.sub(r'\s+', ' ', text)


def remove_punctuation(text, omit=[]):
    punc = string.punctuation
    for o in omit:
        punc = punc.replace(o, '')
    return re.sub(r'[' + punc + ']', '', text)


def remove_stopwords(text, stopwords):
    return re.sub(r'\b(' + '|'.join(stopwords) + r')\b', '', text)


def remove_numbers(text):
    return re.sub(r'\d+', '', text)


def tokenize_words(text):
    return text.split()


def get_all_words(words):
    return set(w.lower() for w in words)


def split_chapters(text, roman_numeral=True):
    if roman_numeral:
        return re.split(r'CHAPTER [IVXLCDM]+', text, flags=re.IGNORECASE)
    else:
        return re.split(r'CHAPTER \d+', text, flags=re.IGNORECASE)