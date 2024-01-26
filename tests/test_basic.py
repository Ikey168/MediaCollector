import os
import sys
import asyncio

sys.path.insert(1, "/home/claude/Desktop/career/Projects/MediaCollector/src")

import collector as co

col = co.Collector()

#asyncio.run(col.get_tweets("Elon Musk"))