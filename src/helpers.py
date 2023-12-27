"""This is the example module.

This module does stuff.
"""


__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Ilja Krasnjanski'

import newspaper
cnn_paper = newspaper.build('http://cnn.com')
print(cnn_paper)


