import requests

THUNDERBIRD_URL = "https://serai.pro/thunderbird" #modified 18.09.2023 reason: removed ".php"

API_KEY = None

#THIS IS USED ONLY IF THERE'S ANY ERROR WITH THE CODE HIMSELF (CAN BE REMOVED)
NOT_ALLOWED = ["Fuck", "Nigga", "Faggot", "nigga", "fuck", "faggot", "kill yourself", "kill", "kys", "kms"] #modified 18.09.2023 reason: a simpler word

def setup(key):
    global API_KEY
    API_KEY = key

def message(msg, prefix=None):
    if API_KEY is None:
        raise ValueError("API key is not set. Use setup(KEY) to set the API key.")

    if any(word in msg.lower() for word in NOT_ALLOWED):
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
