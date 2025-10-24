import heapq

class heapNode:
    def __init__(self, frq, sentence):
        self.frq = frq
        self.sentence = sentence

    def __lt__(self, other):
        if self.frq == other.frq:
            return self.sentence > other.sentence
        return self.frq < other.frq

class TrieNode:
    def __init__(self):
        self.children = [None] * 256
        self.startsWith = []

class AutocompleteSystem:

    def __init__(self, sentences, times):
        self.map = {}
        self.search = ""
        self.root = TrieNode()

        for i in range(len(sentences)):
            if sentences[i] not in self.map:
                self.insert(sentences[i])
            self.map[sentences[i]] = self.map.get(sentences[i], 0) + times[i]

    def insert(self, word):
        curr = self.root
        for c in word:
            idx = ord(c) - ord(' ')
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
            curr.startsWith.append(word)

    def searchPrefix(self, prefix):
        curr = self.root
        for c in prefix:
            idx = ord(c) - ord(' ')
            if curr.children[idx] is None:
                return []
            curr = curr.children[idx]
        return curr.startsWith

    def input(self, c):
        if c == '#':
            if self.search not in self.map:
                self.insert(self.search)
            self.map[self.search] = self.map.get(self.search, 0) + 1
            self.search = ""
            return []

        self.search += c
        pq = []

        for sentence in self.searchPrefix(self.search):
            heapq.heappush(pq, heapNode(self.map[sentence], sentence))
            if len(pq) > 3:
                heapq.heappop(pq)


        result = []
        while pq:
            result.append(heapq.heappop(pq).sentence)

        result.reverse()
        return result
