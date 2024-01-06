import os
import sys

sys.path.insert(1, "/home/claude/Desktop/career/Projects/MediaCollector/src")

import collector as co

col = co.Collector()
col.article_list('https://edition.cnn.com/')
text = col.article_texts[-1]

ner = co.NER()
entities = ner.extract_entitities(text)