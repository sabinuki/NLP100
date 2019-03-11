# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」

# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

str1 = u"パトカー"
str2 = u"タクシー"
result = u""

for a, b in zip(str1, str2):
    result += a + b

print(result)
