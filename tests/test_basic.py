import os
import sys

sys.path.insert(1, "/home/claude/Desktop/career/Projects/MediaCollector/src")

import collector as co

col = co.Collector()

col.get_reddit_posts("MachineLearning", 5)