#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import nltk
from nltk.draw.dispersion import dispersion_plot
import matplotlib

ww = open("Moana.txt","r")
raw = ww.read()

# process
pattern = r'''(?x)    # set flag to allow verbose regexps
    ([A-Z]\.)+        # abbreviations, e.g. U.S.A.
  | \w+(-\w+)*        # words with optional internal hyphens
  | \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
  | \.\.\.            # ellipsis
  | [][.,;"'?():-_`]  # these are separate tokens; includes ], [
  '''

tokens = nltk.regexp_tokenize(raw,pattern)

lctokens = [w.lower() for w in tokens]

# ordered by frequency
from collections import Counter
c = Counter(tokens)
c.most_common(100)

#plot
dispersion_plot(lctokens,['maui','hook','heart','te','fiti','ka','ocean','island',
  'reef','moana','boat','gramma','tattoo','cheeeehoooo','crab','shiny'])
