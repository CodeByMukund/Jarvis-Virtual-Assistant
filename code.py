import random
import pyttsx3
import speech_recognition as sr
import webbrowser
from datetime import datetime
import requests

def speak(text):
    """Speak the given text"""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user input through the microphone"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text.lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            return ""
        

def wish_master():
    hour = datetime.now().hour
    if hour < 12:
        greeting = "Good morning!"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good evening!"
    speak(greeting + " How can I assist you today?")
    print(greeting + " How can I assist you today?")

def get_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"The current time is {current_time}."

def get_weather():
    city = "Mumbai"  # Replace with the city you want to fetch weather for
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=your_openweather_api_key&units=metric"  # Replace with your API key
    try:
        response = requests.get(url)
        weather_data = response.json()
        if weather_data["cod"] == 200:
            temp = weather_data["main"]["temp"]
            description = weather_data["weather"][0]["description"]
            return f"The current temperature in {city} is {temp}°C with {description}."
        else:
            return "I couldn't fetch the weather details right now."
    except Exception as e:
        return "There was an error fetching the weather details."

def symptoms_checker():
    symptoms = input("Enter your symptoms separated by commas: ").lower().split(',')
    print("Analyzing symptoms...")
    # Simplistic symptom checker
    if "fever" in symptoms and "cough" in symptoms:
        return "You might have a cold or flu. Please consult a doctor if it persists."
    elif "headache" in symptoms and "dizziness" in symptoms:
        return "It might be a migraine. Rest and stay hydrated."
    else:
        return "I'm not sure about the diagnosis. Consider consulting a healthcare professional."

def fitness_advice():
    advice = [
        "Drink at least 8 glasses of water daily.",
        "Incorporate strength training into your routine.",
        "Stretch before and after your workouts.",
        "Get at least 7-8 hours of sleep for recovery.",
        "Eat a balanced diet with plenty of protein and vegetables."
    ]
    return random.choice(advice)

def get_recipe():
    recipes = {
        "pasta": "Boil pasta, add sauce, and mix with vegetables or protein.",
        "omelette": "Whisk eggs, add veggies, and cook in a pan with some butter.",
        "smoothie": "Blend fruits, milk or yogurt, and some honey for sweetness."
    }
    print("Available recipes: pasta, omelette, smoothie")
    dish = input("Enter the dish you want the recipe for: ").lower()
    return recipes.get(dish, "Sorry, I don't have a recipe for that.")

def rizz_quotes():
    quotes = [
        "Are you a magician? Because every time I look at you, everyone else disappears.",
        "Is your name Google? Because you have everything I’ve been searching for.",
        "If beauty were time, you'd be eternity."
    ]
    return random.choice(quotes)

def shayari():
    shayaris = [
        "Zindagi se kyu shikwa karein, hum toh khud se naraz baithe hain.",
        "Dil se chahat ka izhar kabhi khatam nahi hota, ek pal ke liye dur chale jaayein toh kya? Yaadon ka silsila kabhi khatam nahi hota.",
        "Aankhon se aansu chupaye nahi jaate, dil ki baat zubaan tak laaye nahi jaate."
    ]
    return random.choice(shayaris)

def jokes():
    jokes_list = [
        "Why don’t skeletons fight each other? They don’t have the guts!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my wife she should embrace her mistakes. She gave me a hug!"
    ]
    return random.choice(jokes_list)

def funny_answer():
    funny_responses = [
        "I’m not arguing, I’m just explaining why I’m right.",
        "My boss told me to have a good day... so I went home!",
        "If I had a dollar for every smart thing you say, I’d be broke."
    ]
    return random.choice(funny_responses)

def tell_story():
    genres = {
        "horror": "It was a dark and stormy night. In the middle of the forest stood an abandoned house where lights flickered even though no one lived there...",
        "adventure": "Once upon a time, a young explorer ventured into the Amazon rainforest, discovering lost cities and hidden treasures guarded by ancient traps.",
        "romance": "In the bustling streets of Paris, two strangers met under the glow of the Eiffel Tower, and their lives were changed forever.",
        "comedy": "There once was a clumsy chef who accidentally added soap instead of salt to his soup. The customers had the bubbliest dinner of their lives!",
        "sci-fi": "In the year 3025, humanity colonized Mars, but little did they know, the planet was already inhabited by intelligent life forms..."
    }
    print("Available genres: horror, adventure, romance, comedy, sci-fi")
    genre = input("Which genre of story would you like to hear? ").lower()
    return genres.get(genre, "Sorry, I don't have a story for that genre.")

def open_application(command):
    if "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif "spotify" in command:
        speak("Opening Spotify")
        webbrowser.open("https://open.spotify.com")
    elif "reddit" in command:
        speak("Opening Reddit")
        webbrowser.open("https://www.reddit.com")
    elif "trs hindi" in command:
        speak("Opening TRS Hindi YouTube channel")
        webbrowser.open("https://www.youtube.com/c/TheRanveerShowHindi")
    elif "tarak mehta" in command:
        speak("Playing Taarak Mehta Ka Ooltah Chashmah on YouTube")
        webbrowser.open("https://www.youtube.com/results?search_query=taarak+mehta+ka+ooltah+chashmah")
    
    elif "open ufc" in command:
        speak("opening mma fight ")
        webbrowser.open("https://www.youtube.com/results?search_query=ufc")   
    else:
        speak("Application not recognized. Please try again.")

def main():
    wish_master()
    while True:
        print("Options: symptoms, fitness, recipe, rizz, shayari, joke, funny, story, time, weather, open app, exit")
        command = input("What do you want me to do? ").lower()

        if "symptoms" in command:
            result = symptoms_checker()
        elif "fitness" in command:
            result = fitness_advice()
        elif "recipe" in command:
            result = get_recipe()
        elif "rizz" in command:
            result = rizz_quotes()
        elif "shayari" in command:
            result = shayari()
        elif "joke" in command:
            result = jokes()
        elif "funny" in command:
            result = funny_answer()
        elif "story" in command:
            result = tell_story()
        elif "time" in command:
            result = get_time()
        elif "weather" in command:
            result = get_weather()
        elif "open" in command:
            open_application(command)
            result = ""
        elif "exit" in command:
            speak("Goodbye! Have a great day!")
            print("Goodbye! Have a great day!")
            break
        else:
            result = "I'm sorry, I didn't understand that."

        if result:
            print(result)
            speak(result)

if __name__ == "__main__":
    main()
