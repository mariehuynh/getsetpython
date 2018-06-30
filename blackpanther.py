import nltk
from nltk.draw.dispersion import dispersion_plot

#ww = open("Wonder.Woman.2017.txt","r")
ww = open("Black.Panther.dialogue.txt","r")
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
c = Counter(lctokens)
for (i,j) in c.most_common(300):
  if len(i) > 4:
    print (i,j)

dispersion_plot(lctokens,['wakanda','oakland','korea','t\'challa','black','panther','nakia', 'shuri', 'okoye', 'klaue', 
  'jabari','n\'jobu','killmonger','ancestors','lab','challenge','herb',
  'vibranium','weapons','freeze','beads','suit','heal','technology'])
