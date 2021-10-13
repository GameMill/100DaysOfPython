import requests
import os
from datetime import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))+"/";
with open(f"{ROOT}pixe.la.key") as pixe_key_file:
    PIXE_API_KEY = pixe_key_file.read()
USERNAME = "chrisboardman"

# user_params ={
#     "token": PIXE_API_KEY,
#     "username":USERNAME,
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes"
# }
#
# response = requests.post(url="https://pixe.la/v1/users",json=user_params)
# print(response.text)


graph_config ={
    "id": "test1",
    "name":"A Test Graph",
    "unit":"Km",
    "type":"float",
    "color":"momiji"
}

# headers = {
#     "X-USER-TOKEN":PIXE_API_KEY
# }

# response = requests.post(url=f"https://pixe.la/v1/users/{USERNAME}/graphs",json=graph_config,headers=headers)
# print(response.text)


#Challange Post to Grapt

def safe_float_input(text):
    """turn the user input into an float. Prevents invalid input"""
    try:
        data =  float(input(text).strip())
        return data
    except:
        return safe_float_input(text)


def today():
    return datetime.today().strftime('%Y%m%d')

headers = {
    "X-USER-TOKEN":PIXE_API_KEY
}

# new_data = {
#     "date":today(),
#     "quantity":str(safe_float_input("Please enter a quatity for today: "))
# }

# response = requests.post(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_config['id']}",json=new_data,headers=headers)
# print(response.text)

update_data = {
    "quantity":str(safe_float_input("Please enter a quatity for today: "))
}

response = requests.put(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_config['id']}/{today()}",json=update_data,headers=headers)
print(response.text)


