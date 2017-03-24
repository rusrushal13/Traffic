import tweepy
import mysql.connector
consumer_key = '6Q8zYIUxsH7NuWXs505STGTiC'
consumer_secret = '5pjrMwpYXycABc1o6ZhjtiFfMis2sShwzrUBEmXHuMFh5Yci8e'
access_token = '373411090GsnxZEsKebLZIrI9CoosfldGH78z4Bkrz6pfwKRr'
access_token_secret = 'mbSVnlNIOiXIallA9NIws51l9mzpi6C2D49ihqktQhMRv'
try:
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
	print 'Error! Failed to get request token.' 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
cnx = mysql.connector.connect(user='root', database='traffic')
cursor = cnx.cursor()
query = ("SELECT * FROM temp")
cursor.execute(query)
for (a, b) in cursor:
	api.update_status('#'+a+b)
cursor.close()
cnx.close()
