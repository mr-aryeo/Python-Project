import webbrowser
import speech_recognition as sr
import pyttsx3
import datetime
import subprocess
import openai
import random
import time
import pyautogui as pag
import pywhatkit
import screen_brightness_control as screen

apikey = "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"


def say(text):
    engine = pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) #female voice
    engine.say(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred"
        


def chat(query):
    openai.api_key = apikey
    prompt = query
    response = openai.ChatCompletion.create(
         model="gpt-3.5-turbo",
         messages=[

         {"role": "system", "content": "You are a helpful assistant"},
         {"role": "user", "content": prompt},
            ],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(f"AI: {response['choices'][0]['message']['content']}")
    if not "write".lower() in prompt.lower(): #koi bhi written essay ya mail bolega nhi
        say(response["choices"][0]["message"]["content"])
    return response["choices"][0]["message"]["content"]


if __name__ == '__main__':
    print("AI: How can i help you")
    say("How can i help you")

    while True:
        print("Listening....")
        query = takecommand()


        # To open any website
        if "open website".lower() in query.lower():
            leng=len(query)
            subquery=query[13:leng]
            subquery1=subquery.replace(" ", "") 
            print(f"A.I: Opening {subquery}")
            say(f"Opening{subquery}")
            webbrowser.open(f"https://{subquery1.lower()}.com")
                
        # My personal Data
        pi = [["my name","Your name is Aryan"],["my age","Your age is 19"],["my phone number","9918596971"],["me about myself","You are a B.C.A final year student who studies in ICFAI university in dehradun and loves to code"],["my birthday","9th of August"],["my girlfriend","I am sorry but nobody loves you"],["about yourself","I am an A.I assistant developed using python and created by Sir Aryan and trained on local data"],["your name","Sorry, as an A.I model I do not have any specific name"],["aur batao","hatt bhosdee k"]]
        for list in pi:
            if f"{list[0]}".lower() in query.lower():
                print(f"AI: {list[1]}")
                say({list[1]})

        # Chrome in Incognito Mode
        if "incognito".lower() in query.lower():
            say("Opeining Incognito Mode")
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito').                                                                                                                                                      open_new("https://xhamster20.desi/")

        # for current time
        elif "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"AI: The time is: {strfTime}")
            say(f"The time is: {strfTime}")

        # to exit A.I
        elif "exit" in query:
            print("AI: Exiting A.I")
            say("Exiting A.I")
            break

        # to play music 
        elif "play ".lower() in query.lower():
            say("Sure")
            leng=len(query)
            subquery= query[5:leng]
            webbrowser.open(f"https://www.youtube.com/results?search_query={subquery}")
            pywhatkit.playonyt(str(subquery)) #converting to string for faster loadup


        #to shutdown system,,, external .bat file used
        elif "shutdown" in query:
            say("Shutting down System")
            path = "C:/Users/shary/Downloads/shutdown.bat"
            subprocess.call([path])
            # subprocess.call(["taskkill","/F","/IM", "pycharm64.exe"])
            subprocess.call(["taskkill","/F","/IM", "cmd.exe"])

        # to keep the screen awake
        elif "screen" in query:
            while True:
                x=random.randint(600,700)
                y=random.randint(200, 600)
                pag.moveTo(x,y,0.7)
                time.sleep(0.1)
                print("Listening....")
                lq=takecommand()
                if "exit" in lq:
                    say("Function Disabled")
                    break
        

        # To control screen brightness
        elif "change brightness to".lower() in query.lower():
            leng=len(query)
            subquery= query[21:leng]
            # val=int(subquery)
            
            screen.set_brightness(int(subquery))

        


        #switching to writing mode        
        elif "switch" in query:
            while True:
                User = input("User: ")
                if(User=='exit'):
                    break
                else:
                    openai.api_key = apikey
                    prompt = User
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[

                        {"role": "system", "content": "You are a helpful assistant"},
                        {"role": "user", "content": prompt},
                            ],
                        temperature=0.7,
                        max_tokens=256,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
                    print(f"AI: {response['choices'][0]['message']['content']}")

        #closing chrome
        if "close chrome".lower() in query.lower():
            print("AI: Closing chrome")
            say("closing chrome")
            subprocess.call(["taskkill","/F","/IM", "chrome.exe"])
            


        # to use openai data 
        elif "samantha".lower() in query.lower():
            chat(query)