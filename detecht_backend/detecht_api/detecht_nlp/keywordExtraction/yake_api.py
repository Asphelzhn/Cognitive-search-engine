# encoding: utf-8
'''
@author: Edward
@file: yake_api.py
@time: 2019/10/9 20:58
@desc:
reference for using YAKE:

In-depth journal paper at Information Sciences Journal

Campos, R., Mangaravite, V., Pasquali, A., Jatowt, A., Jorge, A., Nunes, C. and Jatowt, A. (2020). YAKE!
Keyword Extraction from Single Documents using Multiple Local Features. In Information Sciences Journal. Elsevier,
Vol 509, pp 257-289. pdf

ECIR'18 Best Short Paper

Campos R., Mangaravite V., Pasquali A., Jorge A.M., Nunes C., and Jatowt A. (2018). A Text Feature Based Automatic
Keyword Extraction Method for Single Documents. In: Pasi G., Piwowarski B., Azzopardi L., Hanbury A. (eds). Advances in
Information Retrieval. ECIR 2018 (Grenoble, France. March 26 – 29). Lecture Notes in Computer Science, vol 10772,
pp. 684 - 691. pdf

Campos R., Mangaravite V., Pasquali A., Jorge A.M., Nunes C., and Jatowt A. (2018). YAKE! Collection-independent
Automatic Keyword Extractor. In: Pasi G., Piwowarski B., Azzopardi L., Hanbury A. (eds). Advances in Information
Retrieval. ECIR 2018 (Grenoble, France. March 26 – 29). Lecture Notes in Computer Science, vol 10772, pp. 806 - 810. pdf
'''

import yake


class Yake4Keyword():
    def yake_api(text, filename):
        """API for YAKE algorithm

        :param text: plian text that need to extract keyword
        :param filename: the text's filename
        :return: (key word, weight) for most relevant keywords
        """
        language = "en"  # specifying parameters
        max_ngram_size = 3
        deduplication_thresold = 0.9
        deduplication_algo = 'seqm'
        windowSize = 1
        numOfKeywords = 20

        custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold,
                                                    dedupFunc=deduplication_algo, windowsSize=windowSize,
                                                    top=numOfKeywords, features=None)
        keywords = custom_kw_extractor.extract_keywords(text)

        return keywords


'''example using textRank to extract keyword
'''
if __name__ == '__main__':
    text = (
        "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and "
        "first released in 1991, Python's design philosophy emphasizes code readability with its notable use of "
        "significant whitespace. Its language constructs and object-oriented approach aim to help programmers write "
        "clear, logical code for small and large-scale projects.[28]\n "
        "\n"
        "Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including "
        "procedural, object-oriented, and functional programming. Python is often described as a \"batteries "
        "included\" language due to its comprehensive standard library.[29]\n "
        "\n"
        "Python was conceived in the late 1980s as a successor to the ABC language. Python 2.0, released 2000, "
        "introduced features like list comprehensions and a garbage collection system capable of collecting reference "
        "cycles. Python 3.0, released 2008, was a major revision of the language that is not completely "
        "backward-compatible, and much Python 2 code does not run unmodified on Python 3. Due to concern about the "
        "amount of code written for Python 2, support for Python 2.7 (the last release in the 2.x series) was "
        "extended to 2020. Language developer Guido van Rossum shouldered sole responsibility for the project until "
        "July 2018 but now shares his leadership as a member of a five-person steering council.[30][31][32]\n "
        "\n"
        "The Python 2 language, i.e. Python 2.7.x, is \"sunsetting\" on January 1, 2020, and the Python team of "
        "volunteers will not fix security issues, or improve it in other ways after that date.[33][34] With the "
        "end-of-life, only Python 3.6.x and later, e.g. Python 3.8 which should be released in October 2019 ("
        "currently in beta), will be supported.[35]\n "
        "\n"
        "Python interpreters are available for many operating systems. A global community of programmers develops and "
        "maintains CPython, an open source[36] reference implementation. A non-profit organization, the Python "
        "Software Foundation, manages and directs resources for Python and CPython development.")
    filename = 'hello.txt'
    keywords_list = Yake4Keyword.yake_api(text, filename)
    print(keywords_list)
