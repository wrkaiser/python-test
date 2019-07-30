# coding:utf-8

import sys
import gensim
import sklearn
import numpy as np

from gensim.models.doc2vec import Doc2Vec, LabeledSentence

TaggededDocument = gensim.models.doc2vec.TaggedDocument
import jieba

f1 = open(r"E:\data\sentence_similarty\dataset\doc2vec_demo\train.txt", "r", encoding='utf-8', errors='ignore')
f2 = open(r"E:\data\sentence_similarty\dataset\doc2vec_demo\fenci.txt", 'w', encoding='utf-8', errors='ignore')

lines = f1.readlines()  # 读取全部内容
w = ''
# 对句子分词且将分词后的文本存入txt
for line in lines:
    line.replace('\t', '').replace('\n', '').replace(' ', '')
    seg_list = jieba.cut(line, cut_all=False)
    f2.write(" ".join(seg_list))
f1.close()
f2.close()


def get_datasest():
    with open(r"E:\data\sentence_similarty\dataset\doc2vec_demo\fenci.txt", 'r', encoding='utf-8', errors='ignore') as cf:
        docs = cf.readlines()
        print(len(docs))

    x_train = []

    # 将分词后的文本给予索引
    for i, text in enumerate(docs):
        word_list = text.split(' ')
        l = len(word_list)
        word_list[l - 1] = word_list[l - 1].strip()
        document = TaggededDocument(word_list, tags=[i])
        x_train.append(document)
    # print(x_train)
    return x_train


# 获取语料库中的向量
def getVecs(model, corpus, size):
    vecs = [np.array(model.docvecs[z.tags[0]].reshape(1, size)) for z in corpus]
    return np.concatenate(vecs)


# 训练模型
def train(x_train, size=200, epoch_num=1):
    model_dm = Doc2Vec(x_train, min_count=1, window=3, size=size, sample=1e-3, negative=5, workers=4)
    model_dm.train(x_train, total_examples=model_dm.corpus_count, epochs=70)
    model_dm.save('model_dm')
    print(model_dm)
    return model_dm


# 测试模型
def test():
    model_dm = Doc2Vec.load("model_dm")
    test_text = ["语料", "信息量"]
    inferred_vector_dm = model_dm.infer_vector(test_text)
    print(inferred_vector_dm)
    sims = model_dm.docvecs.most_similar([inferred_vector_dm], topn=10)

    return sims


# 主函数应用
if __name__ == '__main__':
    x_train = get_datasest()
    model_dm = train(x_train)
    sims = test()
    for count, sim in sims:
        sentence = x_train[count]
        words = ''
        for word in sentence[0]:
            words = words + word + ' '
        print(words, sim, len(sentence[0]))