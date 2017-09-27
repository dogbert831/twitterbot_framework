import pymysql
import bot

db = pymysql.connect(host = 'localhost',
					user = 'dba',
					password = 'admin!00',
					db = 'twitterbot')
cursor = db.cursor()

try:
	sql = "SELECT id, term FROM derog_term WHERE used = 0 LIMIT 1"
	cursor.execute(sql)
	results = cursor.fetchone()
	phrase = results[1]
	index = results[0]
	#print(results)
	#print(phrase)
	#print(index)
	sql = "UPDATE derog_term SET used = 1 where id = %s"
	#print(sql)
	cursor.execute(sql, (index))
	db.commit()
except:
    print("Error: unable to fetch data")
if phrase != "":
    tweet = "Daily description of Trump. " + "\"" + phrase + "\" " + "Can you make a sentence of this?"
    #print(tweet)
    #print(len(tweet))
    bot.tweet(tweet)
db.close()