# 06. 集合

# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

def ngram(input, n):
    result = []

    for i in range(0, len(input) - n + 1):
        result.append(input[i:i+n])

    return result


str1 = "paraparaparadise"
str2 = "paragraph"

X = set(ngram(str1, 2))
Y = set(ngram(str2, 2))

print("X和集合: %s" % X)
print("Y和集合: %s" % Y)
print("XY和集合: %s" % X.union(Y))
print("XY積集合: %s" % X.intersection(Y))
print("XY差集合: %s" % X.difference(Y))
print("X_se:" + str("se" in X))
print("Y_se:" + str("se" in Y))
