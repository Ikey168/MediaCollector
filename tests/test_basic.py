import os
import sys

sys.path.insert(1, "/home/claude/Desktop/career/Projects/MediaCollector/src")

import collector as co

col = co.Collector()

col.get_pdf_list("https://arxiv.org/list/cs.AI/recent", "https://arxiv.org", '/pdf')
