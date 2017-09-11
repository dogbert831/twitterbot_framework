import pymysql
import bot

db = pymysql.connect(host = 'localhost',
					user = 'dba',
					password = 'admin!00',
					db = 'twitterbot')
cursor = db.cursor()

try:
	sql = "SELECT id, quote FROM quotes WHERE used = 0 LIMIT 1"
	cursor.execute(sql)
	results = cursor.fetchone()
	phrase = results[1]
	index = results[0]
	#print(results)
	#print(phrase)
	#print(index)
	sql = "UPDATE quotes SET used = 1 where id = %s"
	#print(sql)
	cursor.execute(sql, (index))
	db.commit()
except:
    print("Error: unable to fetch data")
if phrase != "":
    tweet = "Trump quote of the day. " + "\"" + phrase + "\""
    #print(tweet)
    bot.tweet(tweet)
db.close()

