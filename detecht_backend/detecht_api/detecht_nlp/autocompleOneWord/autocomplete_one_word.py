class TrieNode:
    def __init__(self):
        # Initialising one node for trie
        self.children = {}
        self.word_list = []
        self.last = False


class Trie:
    def __init__(self):
        # Initialising one node for trie
        self.root = TrieNode()

    def form_trie(self, wordWeight):

        for item in wordWeight:
            self.insert(item)  # inserting one key to the trie.

    def insert(self, wordWeight):

        node = self.root

        for a in list(key):
            if not node.children.get(a):
                node.children[a] = TrieNode()

            node = node.children[a]

        node.last = True

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

    def print_auto_suggestions(self, key):

        # Returns all the words in the trie whose common
        # prefix is the given key thus listing out all
        # the suggestions for autocomplete.
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

        return node.word_list

