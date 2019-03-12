# 05. n-gram

# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．


def ngram(input, n):
    result = []

    for i in range(0, len(input) - n + 1):
        result.append(input[i:i+n])

    return result


str = "I am an NLPer"

words = str.split()

word = ngram(words, 2)
chars = ngram(str, 2)

print("word: %s" % word)
print("char: %s" % chars)
