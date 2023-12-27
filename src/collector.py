"""This is the example module.

This module does stuff.
"""




import newspaper


class Collector:
    def __init__(self):
        self.article_urls = []
    
    def article_list(self, source_url):
        cnn_paper = newspaper.build(source_url)
        for article in cnn_paper.articles:
            self.article_urls.append(article.url)

    def full_list(self, source_urls):
        for source_url in source_urls:
            self.article_list(source_url)