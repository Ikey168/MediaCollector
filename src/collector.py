"""This is the example module.

This module does stuff.
"""




import newspaper


class Collector:
    def __init__(self):
        self.article_urls = []
        self.article_titles = []
        self.article_texts = []
    
    def article_list(self, source_url):
        paper = newspaper.build(source_url)
        for article in paper.articles:
            self.article_urls.append(article.url)
            self.article_titles.append(article.title)
            self.article_texts.append(article.text)

    def full_list(self, source_urls):
        for source_url in source_urls:
            self.article_list(source_url)

