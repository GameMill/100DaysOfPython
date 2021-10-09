import requests

AMOUNT = 10
TYPE = "boolean"

def get_questions():
    parameters = {
        "amount": AMOUNT,
        "type":TYPE
    }
    responses = requests.get(f"https://opentdb.com/api.php",params=parameters)
    responses.raise_for_status()
    data = responses.json()
    if(data["response_code"] == 0):
        return data["results"]
    else:
        return []



question_data = get_questions()