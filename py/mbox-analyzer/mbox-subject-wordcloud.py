# -*- coding: utf-8 -*-

## References:
## [1] https://www.geeksforgeeks.org/generating-word-cloud-python/

import sys, re
import mailbox
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS 

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " file_name.mbox")
    sys.exit(1)

subjects = ""
stopwords = set(STOPWORDS)

mbox = mailbox.mbox(sys.argv[1])
for message in mbox:
    subject = message['Subject'] 
    subjects += "\n" + subject

subjects = re.sub('Re: ','',subjects)
subjects = re.sub('RE: ','',subjects)
subjects = re.sub('Fw: ','',subjects)
subjects = re.sub('FW: ','',subjects)

# print(subjects)

wordcloud = WordCloud(width = 1024, height = 768, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(subjects)

plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0)

plt.show()