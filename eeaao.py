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
print(c.most_common(100))

#plot
dispersion_plot(lctokens,['mandarin','cantonese','chinese','waymond','alphawaymond','evelyn',
  'joy','jobu','becky','gonggong','alphagonggong','deirdre','hotdog','party','alpha',
  'alphaverse','gay','pig','bagel','feel','eyes','kind','earpiece','feet','love','raccoon'])
