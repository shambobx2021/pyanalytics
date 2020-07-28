# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:48:01 2020

@author: Shambo
"""
#pip install wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = ("data data python chart plot show shambo shambo shambo")
wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
