import datetime
import jieba
import numpy as np


def test_time():
    now_time = datetime.datetime.now()  # UTC-0
    print(now_time)
    utc_time = datetime.datetime.utcnow()  # UTC-8
    print(utc_time)


def test_jieba():
    sss="东直门南大街"
    seg_list = jieba.lcut(sss, cut_all=False)
    print("/".join(seg_list))
    seg_list = jieba.cut_for_search(sss)
    print("/".join(seg_list))


if __name__ == '__main__':
    a = np.random.uniform(-0.1, 0.1, (10, 2))
    W = [[1,2,3],[1,2,3],[1,2,3]]
    input_array = [0.1,0.2,0.3]
    print(np.dot(W, input_array))
