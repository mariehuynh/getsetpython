#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import nltk
from nltk.draw.dispersion import dispersion_plot
from nltk.tokenize import word_tokenize
import matplotlib

ww = open("eeaao.txt","r")
raw = ww.read()

tokens = word_tokenize(raw)
lctokens = [w.lower() for w in tokens]

# ordered by frequency
from collections import Counter
c = Counter(tokens)
c.most_common(100)

#plot
dispersion_plot(lctokens,['mandarin','cantonese','chinese','waymond','evelyn','joy','jobu','becky','gong','mom','dad','father','party','abandon','alpha','alphaverse','gay','pig','girlfriend','bagel','feel','eyes','kind','earpiece','hotdog','feet','love'])