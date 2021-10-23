from internet_speed_twitter_bot import InternetSpeedTwitterBot



speedtest = InternetSpeedTwitterBot()

speedtest.get_internet_speed()

print(speedtest.ref)
print(speedtest.ping)
print(speedtest.down)
print(speedtest.up)

speedtest.tweet_at_provider()
