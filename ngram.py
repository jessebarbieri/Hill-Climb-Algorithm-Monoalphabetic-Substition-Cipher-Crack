from math import log10


class ngram(object):
    def __init__(self):
        self.ngram = {}
        for line in open('english_bigrams.txt'):
            key, count = line.split()
            self.ngram[key] = int(count)
        self.L = len(key)
        self.N = sum(self.ngram.values())

        for key in self.ngram.keys():
            self.ngram[key] = log10(float(self.ngram[key]) / self.N)

        self.floor = log10(0.01 / self.N)

    def score(self, text):
        score = 0
        ngram = self.ngram.__getitem__
        for i in range(len(text) - self.L + 1):
            if text[i:i + self.L] in self.ngram:
                score += ngram(text[i:i + self.L])
            else:
                score += self.floor
        return score
