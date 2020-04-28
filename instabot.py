from instapy import InstaPy

session = InstaPy(username="kaleshcv", password="lasvegas007@")
session.login()
count=session.comment_replies.count()
print(count)
