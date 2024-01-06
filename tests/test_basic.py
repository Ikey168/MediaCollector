import os
import sys

sys.path.insert(1, "/home/claude/Desktop/career/Projects/MediaCollector/src")

import collector as co

col = co.Collector()
col.article_list('https://apnews.com/')
print(col.article_dics)
text = col.article_dics[-1]['text']

ner = co.NER()
entities = ner.extract_entitities(text)

db = co.MediaDB()
