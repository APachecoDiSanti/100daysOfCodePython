from internet_speed_twitter_bot import *

bot = InternetSpeedTwitterBot()
down_speed, up_speed = bot.get_internet_speed()
if down_speed < bot.PROMISED_DOWN or up_speed < bot.PROMISED_UP:
    bot.login_twitter()
    bot.tweet_at_provider(down_speed, up_speed)
else:
    print("Internet speed is above promised values!")
