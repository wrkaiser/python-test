import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim import corpora, similarities

texts = [['human', 'interface', 'computer', 'computer'],
['survey', 'user', 'computer', 'system', 'response', 'time'],
['eps', 'user', 'interface', 'system'],
['system', 'human', 'system', 'eps'],
['user', 'response', 'time'],
['trees'],
['graph', 'trees'],
['graph', 'minors', 'trees'],
['graph', 'minors', 'survey']]

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
print(corpus)  # [(0, 1), (1, 1), (2, 1)]

from gensim import models
tf_idf = models.TfidfModel(corpus)
doc_bow = [(0, 1), (1, 1)]
# print(tf_idf[doc_bow]) # [(0, 0.70710678), (1, 0.70710678)]

tf_idf.save("./model.tfidf")
tf_idf = models.TfidfModel.load("./model.tfidf")

corpus_tfidf = tf_idf[corpus]

# 构造LSI模型并将待检索的query和文本转化为LSI主题向量
# 转换之前的corpus和query均是BOW向量
lsi_model = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=2)
documents = lsi_model[corpus]
print(documents)
query_vec = lsi_model[doc_bow]

index = similarities.MatrixSimilarity(documents)
sims = index[query_vec]