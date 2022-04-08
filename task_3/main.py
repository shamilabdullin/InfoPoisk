import re
import nltk
import zipfile
import pymorphy2
from bs4 import BeautifulSoup

morph = pymorphy2.MorphAnalyzer()


def prepare():
    nltk.download('stopwords')


def lemmatize(word):
    return morph.parse(word.replace("\n", ""))[0].normal_form


def is_word(word):
    word_is_valuable = word.lower() not in nltk.corpus.stopwords.words('russian')
    word_is_russian = re.compile(r"^[а-яА-Я]+$").match(word.lower())

    return word_is_valuable and word_is_russian


def tokenize(html_text, lemmatized=False):

    # Токенизация и лемматизация

    parser = 'html.parser'
    content = BeautifulSoup(html_text, parser).get_text()
    tokens = filter(
        is_word,
        nltk.wordpunct_tokenize(content)
    )

    return set(map(lambda token: lemmatize(token) if lemmatized else token, tokens))


def build_index(zip_path, output_name, lemmatized):
    result_index = {}
    zip_file = zipfile.ZipFile(zip_path, "r")

    for index, file in enumerate(zip_file.filelist):
        content = zip_file.open(file)
        tokens = tokenize(content, lemmatized=lemmatized)

        for token in tokens:
            if token in result_index:
                result_index[token].add(index)
            else:
                result_index[token] = {index}

    with open(output_name, "w", encoding="utf8") as out:
        res_string = "\n".join(map(lambda key: f"{key} {' '.join(map(str, sorted(result_index[key])))}", result_index.keys()))
        out.write(res_string)


def read_index(index_path):
    index_dict = {}
    with open(index_path, "r", encoding="utf8") as file:
        lines = file.readlines()
        for line in lines:
            items = line.split()
            index_dict[items[0]] = items[1:]

    return index_dict


def search(query, index, mode):

    # Ищет страницы по словам в параметре query с сортировкой по максимальному совпадению (в случае mode="OR")

    items = query.split()
    search_results = {}

    if mode == "OR":
        for item in items:
            lemma = lemmatize(item)
            if lemma in index:
                results = index[lemma]
                for result in results:
                    if result in search_results:
                        search_results[result] += 1
                    else:
                        search_results[result] = 1

        return {k for k, v in sorted(search_results.items(), key=lambda item: item[1], reverse=True)}

    elif mode == "AND":
        for item in items:
            lemma = lemmatize(item)
            if lemma in index:
                results = index[lemma]
                if len(search_results) == 0:
                    search_results = set(results)
                else:
                    search_results = search_results.intersection(set(results))

        return search_results


if __name__ == '__main__':
    prepare()

    zip_file_path = "../task_1/выкачка.zip"
    index_file_path = "index.txt"
    index_tokens_file_path = "index_tokens.txt"

    build_index(zip_file_path, index_file_path, lemmatized=True)
    build_index(zip_file_path, index_tokens_file_path, lemmatized=False)

    search_res = search("красивая стена", read_index(index_file_path), mode="AND")
    print(search_res)

    search_res = search("красивая стена", read_index(index_file_path), mode="OR")
    print(search_res)