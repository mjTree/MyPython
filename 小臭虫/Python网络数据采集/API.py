from twitter import *

t=Twitter(auth=OAuth(<Access Token>,<Access Token Secret>,<Consumer Key>,<Consumer Secret>))
'''
pythonTweets=t.search.tweets(q = "#python")
print(pythonTweets)
'''
statusUpdate=t.statuses.update(status='213123')
print(statusUpdate)
