"""This is the example module.

This module does stuff.
"""




import newspaper


class Collector:
    def __init__(self):
        self.article_urls = []
    
    def article_list(self, news_website):
        cnn_paper = newspaper.build(news_website)
        for article in cnn_paper.articles:
            self.article_urls.append(article.url)
            print(article.url)