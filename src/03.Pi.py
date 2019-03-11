# 03. 円周率

# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = str.split(" ")

count_list = []

for word in words:
    word = word.rstrip(",.")
    count_list.append(len(word))
    print(word)

print(count_list)
