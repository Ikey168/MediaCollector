import os
import sys

sys.path.insert(1, "/home/claude/Desktop/career/Projects/MediaCollector/src")

import collector as co

col = co.Collector()
col.article_list('https://www.foxnews.com/')

#ner = co.NER()
#entities = ner.extract_entitities(text)