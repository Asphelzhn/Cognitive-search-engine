from detecht_api.detecht_nlp.autocompleOneWord import autocomplete_one_word

if __name__ == '__main__':
    texts = ["hej", "hur", "var"]
    theTrie = autocomplete_one_word.Trie()
    theTrie.form_trie(texts)
    bool1 = theTrie.search("hej")
    bool2 = theTrie.search("hejsvanepo")
    print(bool1)
    print(bool2)

    print(theTrie.root.children.items())

    print(theTrie.printAutoSuggestions('h'))