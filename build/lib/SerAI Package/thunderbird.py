
import requests

THUNDERBIRD_URL = "https://serai.pro/thunderbird.php"

# Store the API key globally
API_KEY = None

def setup(key):
    global API_KEY
    API_KEY = key

def message(message):
    if API_KEY is None:
        raise ValueError("API key is not set. Use setup(KEY) to set the API key.")

    params = {
        "key": API_KEY,
        "thunderbird": message,
    }

    response = requests.get(THUNDERBIRD_URL, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
