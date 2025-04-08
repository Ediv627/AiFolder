import google.generativeai as genai
import pyttsx3 as p3
import speech_recognition as sr
import time

# Forbidden words list
forbidden_words = ['-', '+', '/', "*"]

# Function to filter forbidden words
def filter_forbidden_words(text):
    for word in forbidden_words:
        text = text.replace(word, '')
    return text

# Initialize speech engine and recognizer
engine = p3.init()
rec = sr.Recognizer()

# API key and configuration for Google Generative AI
API_KEY = 'Your_Api_Key'
genai.configure(api_key=API_KEY)

# Start chat model
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

# Execution time setup
execution_time = 35 * 60
stime = time.time()

while True:
    # Capture audio input using microphone
    with sr.Microphone() as src:
        print("Listening...")
        audio = rec.listen(src)
        text = rec.recognize_google(audio)

        # Exit condition
        if text.strip().lower() == "space":
            print("Exiting...")
            break

    # Send input to chat model and get response
    response = chat.send_message(text)
    print(f"You: {text}")
    
    # Get the bot's response
    bot_response = response.text
    print(f"Bot: {bot_response}")
    
    # Filter forbidden words in the bot's response
    filtered_response = filter_forbidden_words(bot_response)
    
    # Use text-to-speech to say the filtered response
    engine.say(filtered_response)
    engine.runAndWait()

    # Optional: Stop execution after certain time
    elapsed_time = time.time() - stime
    if elapsed_time >= execution_time:
        print("Execution time reached. Exiting...")
        break
