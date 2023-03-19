from collections import defaultdict

class WordDictionary:

    def __init__(self):
        self.dict = defaultdict(set)


    def addWord(self, word: str) -> None:
        self.dict[len(word)].add(word)


    def search(self, word: str) -> bool:
        if '.' not in word:
            return word in self.dict[len(word)]

        for v in self.dict[len(word)]:
            for i, char in enumerate(word):
                if char != v[i] and char != '.':
                    break
            else:
                return True

        return False




obj = WordDictionary()
obj.addWord('a')
obj.addWord('ab')
print(obj.search('a'))
print(obj.search('a.'))
print(obj.search('ab'))
print(obj.search('.a'))
print(obj.search('.b'))
print(obj.search('ab.'))
print(obj.search('.'))
print(obj.search('..'))
