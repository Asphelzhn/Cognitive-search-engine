import operator

class TrieNode:
    def __init__(self):
        # Initialising one node for trie
        self.children = {}
        self.last = False
        self.word_list = []


class Trie:
    def __init__(self):
        # Initialising one node for trie
        self.root = TrieNode()
        self.sizeOfSuggestions = 0

    def form_trie(self, key, sizeOfSuggestion):
        self.sizeOfSuggestions = sizeOfSuggestion
        for item in key.items():
            self.insert(item)  # inserting one key to the trie.

    def insert(self, word_tuple):

        node = self.root
        for a in list(word_tuple[0]):
            if not node.children.get(a):
                node.children[a] = TrieNode()
            node = node.children[a]
            self.insert_word_node(node, word_tuple)
        node.last = True

    def insert_word_node(self, node, value_pair):
        temp_word_list = [i[0] for i in node.word_list]
        if len(node.word_list) < self.sizeOfSuggestions and value_pair[0] not in temp_word_list:
            node.word_list.append(value_pair)
        elif value_pair[0] in temp_word_list:
            i = node.word_list.index(value_pair[0])
            del node.word_list[i]
            node.word_list.append(value_pair)
        elif value_pair[1] > node.word_list[self.sizeOfSuggestions-1][1]:
            del node.word_list[self.sizeOfSuggestions-1]
            node.word_list.append(value_pair)

        # Sorts all word tuples with largest first
        node.word_list.sort(key=operator.itemgetter(1), reverse=True)

    def search(self, key):

        # Searches the given key in trie for a full match
        # and returns True on success else returns False.
        node = self.root
        found = True
        for a in list(key):
            if not node.children.get(a):
                found = False
                break
            node = node.children[a]

        return node and node.last and found

    def suggestions(self, node, word):
        temp = []
        if node.last:
            temp.append(word)

        for a, n in node.children.items():
            t = self.suggestions(n, word + a)
            temp = temp+t

        return temp

    def find_all_suggestions(self, key):

        node = self.root
        not_found = False
        temp_word = ''

        for a in list(key):
            if not node.children.get(a):
                not_found = True
                break

            temp_word += a
            node = node.children[a]

        if not_found:
            return 0
        elif node.last and not node.children:
            return -1

        #suggest = self.suggestions(node, temp_word)
        suggest = node.word_list
        return suggest

    def find_word_suggestions(self, key):
        tuples = self.find_all_suggestions(key)
        if tuples == 0:
            return 0
        elif tuples == -1:
            return -1
        else:
            return [i[0] for i in tuples]
