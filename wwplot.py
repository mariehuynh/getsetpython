import nltk
from nltk.draw.dispersion import dispersion_plot

ww = open("Wonder.Woman.2017.txt","r")
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

tokens = nltk.word_tokenize(raw)
lctokens = [w.lower() for w in tokens]

# ordered by frequency
from collections import Counter
c = Counter(text6)
c.most_common(50)

#plot
dispersion_plot(lctokens,['diana','wonder','woman','hippolyta','zeus','steve',
  'ares','war','men','evil','ludendorff','german','gas',
  'love','ice','cream','sleep','dance'])


# Who is WW really about?

dispersion_plot(lctokens,['diana','wonder','woman','hippolyta','zeus','steve',
  'ares','ludendorff','german','germans', 'doctor', 'poison', 'secretary',])