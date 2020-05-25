import pyttsx3
import subprocess      #system command
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser           #control web browser
import random
import wolframalpha
import ctypes       
import winshell           
import os
import cv2  #openCV moduals
import time 
import pyjokes   #joke system
import smtplib
import sys
import requests
from twilio.rest import Client
from PIL import ImageGrab
from bs4 import BeautifulSoup  #corona virus update
from selenium import webdriver
# from VideoCapture import Device  #take photo



engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('Your_API _Id')
voices  = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    print('Jarvis: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 17:
        speak("Good Afternoon!")

    if hour >= 17 and hour !=0:
        speak('Good Evening!')


print("----Welcome to Our Project Personal voice Assistant - Jarvis----")
wishMe()
speak('Hello Sir, I am your Personal assistant Jarvis!')
speak('How may I help you?')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user: {query}\n")

    except Exception as e:
        #print(e)
        speak('Sorry sir! I didn\'t get that! again please...')
        speak("Please Enter Your command")
        query = input()

    return query

def open_application(query):
    if "chrome" in query:
        speak("Google Chrome")
        codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(codePath)
        return

    elif "firefox" in query or "mozilla" in query:
        speak("Opening Mozilla Firefox")
        codePath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        os.startfile(codePath)
        return

    elif "word" in query:
        speak("Opening Microsoft Word")
        codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
        os.startfile(codePath)
        return

    elif "excel" in query:
        speak("Opening Microsoft Excel")
        codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
        os.startfile(codePath)
        return

    elif 'vs code' in query or 'code' in query:
        speak("Opening Visual Studio Code")
        codePath = "c:\\Users\\kanar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
        return

    elif 'PyCharm' in query or 'pycharm' in query:
        speak("Opening JetBrain Pycharm")
        codePath = "C:\\Program Files\\JetBrains\\PyCharm 2020.1\\bin\\pycharm64.exe"
        os.startfile(codePath)
        return

    elif "TeamViewer" in query or "teamviewer" in query:
        speak("Opening TeamViewer")
        codePath = "C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe"
        os.startfile(codePath)
        return

    elif "Notepad" in query or "notepad" in query:
        speak("Opening Notepad++")
        codePath = "C:\\Program Files\\Notepad++\\notepad++.exe"
        os.startfile(codePath)
        return


# Social media and Website
    elif 'instagram' in query:
        speak('okay')
        webbrowser.open('www.instagram.com')
        return

    elif 'facebook' in query:
        speak('okay')
        webbrowser.open('www.facebook.com')
        return

    elif 'erp' in query or 'ERP' in query:
        speak('okay')
        webbrowser.open('http://jecrc.academiaerp.com/academia_jecrc/index.jsp')
        return

    elif 'twitter' in query:
        speak('okay')
        webbrowser.open('www.twitter.com')
        return

    elif 'reddit' in query:
        speak('okay')
        webbrowser.open('www.reddit.com')
        return

    elif 'fb' in query:
        speak('okay')
        webbrowser.open('www.fb.com')
        return

    elif 'youtube' in query:
        webbrowser.open('www.youtube.com')
        return

    elif 'gmail' in query:
        speak('okay')
        webbrowser.open('www.gmail.com')
        return

    elif 'google' in query:
        webbrowser.open('www.google.com')
        return

    elif 'github' in query:
        webbrowser.open('www.github.com')
        return
    
    elif 'stackoverflow' in query:
        webbrowser.open('www.stackoverflow.com')
        return
    else:
        speak(query + "not available")
        return

# searching system all engines
#
# def search_web(query):
#
#     driver = webdriver.Firefox()
#     driver.implicitly_wait(1)
#     driver.maximize_window()
#
#     if 'youtube' in query.lower():
#
#         speak("Opening in youtube")
#         indx = query.lower().split().index('youtube')
#         query = query.split()[indx + 1:]
#         driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
#         return
#
#     # elif 'wikipedia' in query.lower():
#
#     #     speak("Opening Wikipedia")
#     #     indx = query.lower().split().index('wikipedia')
#     #     query = query.split()[indx + 1:]
#     #     driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
#     #     return
#
#     else:
#
#         if 'google' in query:
#
#             indx = query.lower().split().index('google')
#             query = query.split()[indx + 1:]
#             driver.get("https://www.google.com/search?q =" + '+'.join(query))
#
#         elif 'search' in query:
#
#             indx = query.lower().split().index('google')
#             query = query.split()[indx + 1:]
#             driver.get("https://www.google.com/search?q =" + '+'.join(query))
#
#         else:
#
#             driver.get("https://www.google.com/search?q =" + '+'.join(query.split()))
#
#         return
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        #logic for executing tasks based on query
        if 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy', "I'm fine, glad you me that"]
            speak(random.choice(stMsgs))

        elif 'hello' in query or 'hello Jarvis' in query or 'Hi Jarvis' in query or 'jarvis' in query or 'hey jarvis' in query:
            wishMe()
            speak('Hello Sir! How can I help you?')

        elif 'who are you' in query or 'define yourself' in query:
            speak('Hello Sir, I am Jarvis. Your personal Assistant created by kanaram yadav". I am here to make your life easier.')

        elif 'who is your developer' in query or 'who is your designer' in query:
            speak('Mr. kanaram yadav is developed me.')

        elif "will you be my gf" in query or "will you be my bf" in query:    
            speak("I'm not sure about, may be you should give me some time")  
  
        elif "i love you" in query: 
            speak("It's hard to understand")

        elif "why you came to world" in query: 
            speak("Thanks to kanaram. further It's a secret") 
  
        elif 'is love' in query: 
            speak("It is 7th sense that destroy all other senses")  
  
        elif 'reason for you' in query: 
            speak("I was created as a Minor project by Mister kanaram ") 

        elif 'change background' in query: 
            ctypes.windll.user32.SystemParametersInfoW(20,  
                                                       0,  
                                                       "G:\\Photos\\wallpaper", 
                                                       0) 
            speak("Background changed succesfully")

        elif 'joke' in query: 
            speak(pyjokes.get_joke())
        
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'play music' in query or 'start music' in query :
            music_folder = 'G:\\ram\\'
            music = ['Dil_Darbadar', 'dil-hi-toh-hai','Mareez-E-Ishq','Sanam_Re',
                    'Teri_Khair_Mangdi','Teri_Yaad','Tu_Hai_Ki_Nahi','tum-hi-aana']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
                  
            speak('Okay, here is your music! Enjoy sir!')

        elif 'the time' in query or 'what is time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'sir, the time is {strTime}')

        elif 'email' in query or 'send email' in query or 'send mail' in query:
            speak('Who is the recipient? ')
            recipient = takeCommand()

            if 'self' in recipient:
                try:
                    speak('What should I say? ')
                    content = takeCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("To Email is", 'Your_password')
                    server.sendmail('To Email ID', "From Email Id", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')

        # elif 'send message' in query or 'Send SMS' in query:
        #     speak('who is the recipient?')
        #     inputres = takeCommand()
        #     inputlist = {'', ''}
        #     for inputres in inputlist:
        #         if 'inputres' == query or inputres == query or inputres in query or 'inputres' in query:
        #             client = Client("Your_API _Id", "Your_API _key")
        #             client.messages.create(to=inputlist[inputres], 
#                                 from_="+12073832920",
#                                 body="This msg from jarvis")
        #             speak('Message sent Successfully')
        #         else:
        #             speak('Sorry Sir! I am unable to send your message at this moment!')
        #     else:
        #         speak("Recipient Not Avaliable!")
        elif "send message" in query or 'message to self' in query: 
                # You need to create an account on Twilio to use this service 
                account_sid = 'Your_API _Id'
                auth_token = 'Your_API _Key'
                client = Client(account_sid, auth_token) 
                speak('What should I say? '),
                message = client.messages.create(                   
                                    body = takeCommand(), 
                                    from_="Number", 
                                    to ='Nymber',
                                ) 
                print(message.sid) 

        elif 'take photo' in query or 'open camera and click' in query:
            videoCaptureObject = cv2.VideoCapture(0)
            result = True
            while (result):
                ret, frame = videoCaptureObject.read()
                cv2.imwrite("NewPicture.jpg", frame)
                result = False
            videoCaptureObject.release()
            cv2.destroyAllWindows()
            speak("photo capture successfull")

        elif 'corona virus status' in query or 'coronavirus update' in query or 'coronavirus status' in query:
            speak('which update show - worldwide ya India')
            ans = takeCommand()
            if 'india' == ans or 'India' == ans:
                url = "https://www.worldometers.info/coronavirus/country/india/"
                req = requests.get(url)
                bsObj = BeautifulSoup(req.text, "html.parser")
                data = bsObj.find_all("div",class_ = "maincounter-number")

                speak("Total Cases: ")
                speak(data[0].text.strip())
                speak("Total Deaths: ")
                speak(data[1].text.strip())
                speak("Total Recovered: ")
                speak(data[2].text.strip())
            else:
                url = "https://www.worldometers.info/coronavirus/"
                req = requests.get(url)
                bsObj = BeautifulSoup(req.text, "html.parser")
                data = bsObj.find_all("div",class_ = "maincounter-number")

                speak("Total Cases: ")
                speak(data[0].text.strip())
                speak("Total Deaths: ")
                speak(data[1].text.strip())
                speak("Total Recovered: ")
                speak(data[2].text.strip())


        elif 'lock window' in query: 
                speak("locking the device") 
                ctypes.windll.user32.LockWorkStation() 
  
        elif 'shutdown system' in query: 
                speak("Do you wish to shutdown your computer ? (yes / no): ") 
                shutdown = takeCommand()
                if shutdown == 'no': 
                    exit() 
                else: 
                    os.system("shutdown /s /t 1") 
                # subprocess.call('shutdown / p /f') 
                  
        elif 'empty recycle bin' in query: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
            speak("Recycle Bin Recycled") 
  
        elif "don't listen" in query or "stop listening" in query: 
            speak("for how much time you want to stop jarvis from listening commands") 
            a = int(takeCommand()) 
            time.sleep(a) 
            print(a) 
  
        elif "where is" in query: 
            query = query.replace("where is", "") 
            location = query 
            speak("User asked to Locate") 
            speak(location) 
            webbrowser.open("https://www.google.com/maps/place/" + location + "") 
  
        elif "restart" in query: 
            subprocess.call(["shutdown", "/r"]) 
              
        elif "hibernate" in query or "sleep" in query: 
            speak("Hibernating") 
            os.system("shutdown.exe /h") 
  
        elif "log off" in query or "sign out" in query: 
            speak("Make sure all the application are closed before sign-out") 
            time.sleep(5) 
            subprocess.call(["shutdown", "/l"]) 

        elif 'screenshot' in query or 'take ScreenShot' in query:
            snapshot = ImageGrab.grab()
            save_path = "C:\\Users\\kanar\\Pictures\\Screenshots\\MySnapshot.jpg"
            snapshot.save(save_path)
  
        elif "write a note" in query: 
            speak("What should i write, sir") 
            note = takeCommand() 
            file = open('jarvis.txt', 'w') 
            speak("Sir, Should i include date and time") 
            snfm = takeCommand() 
            if 'yes' in snfm or 'sure' in snfm: 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime) 
                file.write(" :- ") 
                file.write(note) 
            else: 
                file.write(note) 
          
        elif "show note" in query: 
            speak("Showing Notes") 
            file = open("jarvis.txt", "r")  
            print(file.read()) 
            speak(file.read(6)) 

        elif 'open' in query:
            open_application(query.lower())

        # if 'search' in query or 'play' in query:
        #     search_web(query)

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'nothing' in query or 'abort' in query or 'stop' in query or 'exit' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Result finded.')
                    speak('WOLFRAM-ALPHA says - ')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Result finded.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                ans = query
                webbrowser.open("https://www.google.com/search?q="+ ans +"") 

        speak('Next Command! Sir!')




        

