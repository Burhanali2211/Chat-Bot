import requests
import pyfiglet
import itertools
import threading
import time
import sys

# Gemini API URL
url = "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent"

# Your Gemini API Key
API_KEY = "YOUR_GEMINI_API_KEY"


def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r' + c)
        sys.stdout.flush()
        time.sleep(0.1)

    # Clear the console output
    sys.stdout.write('\r')
    sys.stdout.flush()


def ask(question):
    payload = {
        "contents": [{"parts": [{"text": question}]}]
    }
    response = requests.post(f"{url}?key={API_KEY}", json=payload)
    if response.status_code == 200:
        return response.json().get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No response received.")
    else:
        return "Error: Unable to get a response from Gemini API."


if __name__ == "__main__":
    print(pyfiglet.figlet_format("AI Chat BOT"))
    print("Enter the question to ask:")
    print()
    while True:
        question = str(input(">>  "))
        if question.lower() == 'q':
            print(">>  Bye! Thanks for Using...")
            break

        # Loading animation
        done = False
        t = threading.Thread(target=animate)
        t.start()

        answer = ask(question)
        time.sleep(2)
        done = True
        t.join()

        print(">> ", answer)
        print()
