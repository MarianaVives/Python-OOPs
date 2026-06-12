import requests

params = {"amount":10,
         "type":"boolean"
          }
URL = "https://opentdb.com/api.php"

response = requests.get(url=URL, params=params)
response.raise_for_status()
body= response.json()
questions_and_ans = []

results = body["results"]
for r in results:
    q = r["question"]
    a = r["correct_answer"]
    questions_and_ans.append({"question":q,"answer":a})

