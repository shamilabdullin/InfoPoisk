import re
import nltk
import zipfile
import pymorphy2
import math
from bs4 import BeautifulSoup

morph = pymorphy2.MorphAnalyzer()


def prepare():
    nltk.download('stopwords')


def is_word(word):
    word_is_valuable = word.lower() not in nltk.corpus.stopwords.words('russian')
    word_is_russian = re.compile(r"^[а-яА-Я]+$").match(word.lower())

    return word_is_valuable and word_is_russian


def lemmatize(word):
    return morph.parse(word.replace("\n", ""))[0].normal_form


def tokenize(html_text, lemmatized=False):
    parser = 'html.parser'
    content = BeautifulSoup(html_text, parser).get_text()
    tokens = filter(
        is_word,
        nltk.wordpunct_tokenize(content)
    )

    return list(map(lambda token: lemmatize(token) if lemmatized else token, tokens))


def read_index(index_path):
    index_dict = {}
    with open(index_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            items = line.split()
            index_dict[items[0]] = items[1:]

    return index_dict


def get_tf(word, tokens):

    # Расчет tf переданного термина word относительно массива tokens

    return tokens.count(word) / float(len(tokens))


def get_idf(word, index, docs_count=100):

    # Расчет idf переданного термина word с использованием индекса из задания №3

    return math.log(docs_count / float(len(index[word])))


def process(zip_file, lemmas_path, tokens_path):

    # Считывает общий индекс терминов и лемм и для каждого из файлов выкачки расчитывает idf и tf-idf

    lemmas_index = read_index(lemmas_path)
    tokens_index = read_index(tokens_path)
    for (index, file) in enumerate(zip_file.filelist):
        content = zip_file.open(file)
        tokens = tokenize(content, lemmatized=False)
        lemmas = list(map(lemmatize, tokens))

        result_tokens = []
        result_lemmas = []

        # TOKENS

        for token in set(tokens):
            tf = get_tf(token, tokens)
            idf = get_idf(token, tokens_index)
            result_tokens.append(f"{token} {idf} {tf * idf}")

        # LEMMAS

        for lemma in set(lemmas):
            tf = get_tf(lemma, lemmas)
            idf = get_idf(lemma, lemmas_index)
            result_lemmas.append(f"{lemma} {idf} {tf * idf}")

        with open(f"token_results/{index}.txt", "w") as token_f:
            token_f.write("\n".join(result_tokens))

        with open(f"lemma_results/{index}.txt", "w") as lemma_f:
            lemma_f.write("\n".join(result_lemmas))


if __name__ == '__main__':
    prepare()

    zip_file_path = "../task1/result.zip"
    lemmas_index_path = "../task3/index.txt"
    tokens_index_path = "../task3/index_tokens.txt"

    zip = zipfile.ZipFile(zip_file_path)

    process(zip, lemmas_index_path, tokens_index_path)