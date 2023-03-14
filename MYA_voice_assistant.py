import wikipedia
import pyttsx3
import webbrowser
import speech_recognition as sr
import random
import datetime
from sys import exit

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak")
        r.pause_threshold = 1
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source, duration=5)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language="en-in")
            print("the command is ", Query)

        except Exception as i:
            print(i)
            print("I don't get what you mean. Can you repeat that?")
            return None

        return Query

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-25)
    engine.say(audio)
    engine.runAndWait()


def Hello():

    speak("hello I am MYA. How can I help you today?")
    speak("Are you a female or a male?")
    answers = command()
    answer = answers.lower()
    if "female" in answer:
        speak("what should I call you? ")
        names = command()
        name = names.lower()
        speak(f"Alright, {name}. Nice to meet you")
    elif "male" in answer:
        speak("what should I call you, sir?")
        names = command()
        name = names.lower()
        speak(f"Alright, {name}. Nice to meet you")

def take_command():
    # this will open the AI assistant
    Hello()

    while True:
        # this will take command
        answers = command()
        query = answers.lower()
        # this will open youtube
        if "youtube" in query:
            speak("opening youtube")
            webbrowser.open("www.youtube.com")
            continue
        # this will open spotify
        elif "spotify" in query:
            speak("opening spotify")
            webbrowser.open("www.spotify.com")
            continue
        # this will open google
        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue
        # this will tell the day
        elif (
            ("which day it is") in query
            or ("what day is it") in query
            or ("what is the date") in query
        ):
            date()
            continue
        # this will tell the time
        elif (
            ("tell me the time") in query 
            or ("what time is it") in query 
            or ("what's the time") in query):
            time()
            continue

        # this will exit the program
        elif "bye" in query:
            speak("Bye")
            exit()

        # search for information on wikipedia
        elif "from wikipedia" in query:
            speak("Checking from wikipedia ")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(command(), sentences=5)
            speak("According to wikipedia")
            speak(result)
            continue

        # asking AI about its name
        elif "tell me your name" in query or "what's your name" in query:
            speak("I am MYA your AI assistant.")
            continue

        # changing the name of the voice assistant
        elif "can i change your name" in query:
            speak("Yeah sure!")
            speak("what would you like to call me?")
            name = command()
            speak(f"Okay so my new name is {name}, that's a great name.")
            continue

        # opening a game
        elif ("open a game" in query):
            mylist = [game1(), game2()]
            speak("which game would you like to play? \n rock,paper,scissors \n or math problems?")
            game = command().lower()
            if "rock, paper, scissors" in game:
                speak("opening game 1")
                game1()
            elif "math problems" in game:
                speak("opening game 2")
                game2()
            continue

        # if command is unrecognized
        else:
            speak("Sorry I can't understand what you mean. Please say again")
            continue

def time():
    time = str(datetime.datetime.now())
    hour, minutes, seconds = time.split(":")
    speak("The time is " + hour + "Hours and " + minutes + " Minutes")
    print(f"{hour}:{minutes}")


def date():
    date = str(datetime.date.today())
    print(date)
    speak(date)

def game1():
    i = 0
    choice = ["rock", "paper", "scissors"]

    speak(f"choose from list {choice}")

    result = random.choice(choice)

    chooses = command()
    choose = chooses.lower()

    if (
        (choose == "rock" and result == "rock")
        or (choose == "paper" and result == "paper")
        or (choose == "scissors" and result == "scissors")
    ):
        speak("even")
        i += 1

    elif choose == "rock" and result == "scissors":
        speak("you win")
        exit()

    elif choose == "paper" and result == "rock":
        speak("you win")
        exit()

    elif choose == "scissors" and result == "paper":
        speak("you win")
        exit()

    elif choose == "rock" and result == "paper":
        speak("you lose")
        i += 1
    elif choose == "scissors" and result == "rock":
        speak("you lose")
        i += 1
    elif choose == "paper" and result == "scissors":
        speak("you lose")
        i += 1
    if i == 3:
        speak("Thank you for playing with me!")
        exit()

def game2():
    speak("choose a level: 1, 2, 3")
    strings = command()
    string = strings.lower()
    if string == 1:
        nums = range(1, 10)
        mylist = list(map(int, nums))
        n1 = int(random.choice(mylist))
        n2 = int(random.choice(mylist))
        speak(f"solve: {n1} x {n2}")
        result = n1 * n2
        answer = int(input("what's your answer? "))
        if answer == result:
            speak("Good job!")
        else:
            speak("Wrong answer")
            exit()
    elif string == 2:
        nums = range(10, 100)
        mylist = list(map(int, nums))
        n1 = int(random.choice(mylist))
        n2 = int(random.choice(mylist))
        speak(f"solve: {n1} x {n2}")
        result = n1 * n2
        answer = int(input("what's your answer? "))
        if answer == result:
            speak("Good job!")
        else:
            speak("Wrong answer")
            exit()
    elif string == 3:
        nums = range(100, 1000)
        mylist = list(map(int, nums))
        n1 = int(random.choice(mylist))
        n2 = int(random.choice(mylist))
        speak(f"solve: {n1} x {n2}")
        result = n1 * n2
        answer = int(input("what's your answer? "))
        if answer == result:
            speak("Good job!")
        else:
            speak("Wrong answer")
            exit()

if __name__ == "__main__":
    take_command()