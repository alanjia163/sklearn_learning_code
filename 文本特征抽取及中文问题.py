#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import jieba

def countvec():
    '''
    英文
    将文本进行特征值化
    :return: None
    '''
    cv = CountVectorizer()
    text_data = ["life is like a box of chocolate.", "you never know what you're gonna get next."]
    # 文本特征值化
    data = cv.fit_transform(text_data)
    # 特征值名称,列名
    comls = cv.get_feature_names()
    print(comls)
    # 将数据的格式由sparce-->array
    data = data.toarray()
    print(data)


def countvec_chinese():
    '''
    中文
    将文本进行特征值化
    :return: None
    '''
    cv = CountVectorizer()
    c1,c2 = cut_words()
    data =cv.fit_transform([c1,c2])
    print(cv.get_feature_names())
    print(data.toarray())

    return None


def cut_words():
    text1 = jieba.cut("豫章故郡，洪都新府。星分翼轸，地接衡庐。")
    text2 = jieba.cut("襟三江而带五湖，控蛮荆而引瓯越。物华天宝，龙光射牛斗之墟")
    t1 = list(text1)
    t2 = list(text2)
    # 列表转换成字符串
    c1 = ' '.join(t1)
    c2 = ' '.join(t2)
    return c1, c2


if __name__ == '__main__':
    # countvec()
    countvec_chinese()