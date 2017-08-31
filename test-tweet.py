import guardian_content

ttweet = guardian_content.scrape_guardian()
tweet = ttweet[0]
url = ttweet[1]
text = tweet + " " + url
print(text)
