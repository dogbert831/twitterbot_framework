import newspaper

#to disable caching memoize_articles=False
nyt_paper = newspaper.build('http://nytimes.com', memoize_articles=False)
#for article in nyt_paper.articles:
#   print(article.url)
for article in nyt_paper.articles:
    print(article.url, file=open("nyt-results.txt", "a"))
