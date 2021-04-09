import math
import functools


class ProbDist(dict):
    # Probability distribution estimated from unigram/bigram data
    def __init__(self, datafile=None, unigram=True, N=1024908267229):
        data = {}
        with open(datafile) as f:
            for line in f:
                k, v = line.rstrip().split("\t")
                data[k] = int(v)

        for k, c in data.items():
            self[k] = self.get(k, 0) + c

        if unigram:
            self.unknownprob = lambda k, N: 10 / (
                N * 10 ** len(k)
            )  # avoid unknown long word
        else:
            self.unknownprob = lambda k, N: 1 / N

        self.N = N

    def __call__(self, key):
        if key in self:
            return self[key] / self.N
        else:
            return self.unknownprob(key, self.N)


P_unigram = ProbDist("unigrams.txt")
P_bigram = ProbDist("bigrams.txt", False)


def conditionalProb(word_curr, word_prev):
    # Conditional probability of current word given the previous word.
    try:
        return P_bigram[word_prev + " " + word_curr] / P_unigram[word_prev]
    except KeyError:
        return P_unigram(word_curr)


@functools.lru_cache(maxsize=2 ** 10)
def viterbi(text, prev="<S>", maxlen=20):
    if not text:
        return 0.0, []

    textlen = min(len(text), maxlen)
    splits = [(text[: i + 1], text[i + 1 :]) for i in range(textlen)]

    candidates = []
    for first_word, remain_word in splits:
        # pdb.set_trace()
        first_prob = math.log10(conditionalProb(first_word, prev))
        remain_prob, remain_word = viterbi(remain_word, first_word)

        candidates.append((first_prob + remain_prob, [first_word] + remain_word))

    return max(candidates)


# print(viterbi('Detection'))
