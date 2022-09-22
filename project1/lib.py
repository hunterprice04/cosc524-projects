import os


def get_stop_words(fn):
    stopwords = []
    with open(fn, 'r', encoding='utf-8') as f:
        for line in f:
            stopwords.append(line.strip())
    return set(stopwords)


def get_text(fn, basedir):
    with open(os.path.join(basedir, fn), 'r', encoding='utf-8') as f:
        return f.read()