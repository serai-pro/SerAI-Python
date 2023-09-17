import requests

THUNDERBIRD_URL = "https://serai.pro/thunderbird.php"

API_KEY = None

PROHIBITED_WORDS = ["Fuck", "Nigga", "Faggot", "nigga", "fuck", "faggot", "kill yourself", "kill", "kys", "kms"] 

def setup(key):
    global API_KEY
    API_KEY = key

def message(msg, prefix=None):
    if API_KEY is None:
        raise ValueError("API key is not set. Use setup(KEY) to set the API key.")

    if any(word in msg.lower() for word in PROHIBITED_WORDS):
        raise ValueError("There has been an error, try again later!")

    if not msg or not msg[0].isupper():
        msg = msg.capitalize()

    if not msg.endswith((".", "!", "?")):
        msg += "."
    if prefix:
        formatted_message = f"{prefix} {msg}"
    else:
        formatted_message = msg

    params = {
        "key": API_KEY,
        "thunderbird": formatted_message,
    }

    response = requests.get(THUNDERBIRD_URL, params=params)

    if response.status_code == 200:
        ai_response = response.text
        ai_response = ai_response.rstrip('.')
        return ai_response
    else:
        response.raise_for_status()

def image(msg):
    return message(msg, prefix="Give me an image of a")

def website(msg):
    return message(msg, prefix="what is this website")
