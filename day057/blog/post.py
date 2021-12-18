import requests
class Post:
    def  __init__(self,id,title,subtitle,body):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.body = body
        

all_posts = {}

for post in requests.get("https://api.npoint.io/c790b4d5cab58020d391").json():
    print(post)
    all_posts[post["id"]] = Post(post["id"],post["title"],post["subtitle"],post["body"])
