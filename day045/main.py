# import os
# from bs4 import BeautifulSoup

# ROOT = os.path.dirname(os.path.abspath(__file__))+"/"
# with open(f"{ROOT}website.html", encoding="utf-8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# #print(soup.prettify())
# #print(soup.title.string)

# # all_a_tags = soup.find_all("a")

# # #print(all_a_tags)
# # for tag in all_a_tags:
# #     print(tag.string)
# #     print(tag.get("href"))


# # heading = soup.find(name="h1",id="name")
# # print(heading)

# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading)
# # print(section_heading.string)

# company_url = soup.select_one(selector="p a").get("href")
# print(company_url)



import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
storys_rows = soup.select_one(".itemlist").find_all("tr")

data = []
for story_index in range(0,len(storys_rows),3):
    row_header = storys_rows[story_index]
    row_data = storys_rows[story_index+1]

    try:
        text = row_header.select_one(".storylink").string
    except:
        continue # Not Valid row
    
    link = row_header.select_one(".storylink").get("href")
    try:
        upvote = row_data.select_one(".score").string
    except:
        upvote = "0 points"
    
    data.append({
        "text":text,
        "link":link,
        "upvote":upvote,
        "upvote_points":int(upvote.split(" ")[0])
    })

highest = data[0]
    
for item in data:
    if highest["upvote_points"] < item["upvote_points"]:
        highest = item
    
    
print(highest["text"])
print(highest["link"])
print(highest["upvote"])