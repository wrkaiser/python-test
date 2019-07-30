import jieba
import jieba.posseg as pseg

jieba.load_userdict("userdict.txt")

test_sentence ="李小福是创新办主任，也是云计算方面的专家"
words = jieba.lcut(test_sentence, cut_all=False)  # 非精确切分
print(words)

words = jieba.lcut(test_sentence, cut_all=True)
print(words)

result = pseg.lcut(test_sentence)
print(result)

jieba.del_word("李小福")
words = jieba.lcut(test_sentence, cut_all=True)
print(words)
for word in words:
    print(str(word) + "----" + str(jieba.get_FREQ(word)))
jieba.add_word("李小福")

words = jieba.cut(test_sentence)
print("/".join(words))
jieba.suggest_freq(("云", "计算"), True)  # 调节词频，使之能单独开来
words = jieba.cut(test_sentence)
print("/".join(words))