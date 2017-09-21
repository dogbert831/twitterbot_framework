#http://newspaper.readthedocs.io/en/latest/index.html
import newspaper

#to disable caching memoize_articles=False
cnn_paper = newspaper.build('http://cnn.com', memoize_articles=True)
for article in cnn_paper.articles:
    print(article.url, file=open("results.txt", "a"))
