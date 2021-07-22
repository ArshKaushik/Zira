import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
assistant_voice = engine.getProperty('voices')

engine.setProperty('voice', assistant_voice[1].id)

def speak(audio_argument): 
    engine.say(audio_argument)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")     

    speak("My name is Zira, creation of Mr. Kaushik. How may I help you?")

def takeCommand():
    recognition = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        recognition.pause_threshold = 1
        audio = recognition.listen(source)

    try:
        print("Recognizing...")    
        query = recognition.recognize_google(audio, language = "en-in")
        print(f"User Input: {query}\n")

    except Exception as e:
        speak("Sorry, I didn't get you. Could you please repeat it?")
        return "None"
    return query

def sendEmail(sendTo, content):
    GMAIL_ID = 'abc@gmail.com'
    GMAIL_PSWD = 'abcpass'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls() # starting the session
    server.login(GMAIL_ID, GMAIL_PSWD)
    server.sendmail(GMAIL_ID, sendTo, content)
    server.close()

if __name__ == "__main__":
    wishMe()    

    while True: 
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Let me search on Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("As I found on Wikipedia, ")
            speak(results)

        elif 'open youtube' in query:  
            speak("Opening YouTube")  
            webbrowser.open("youtube.com")
        elif 'open google' in query:  
            speak("Opening Google")  
            webbrowser.open("google.com")
        elif 'open linkedin' in query:  
            speak("Opening LinkedIn")  
            webbrowser.open("linkedin.com")
        elif 'open quora' in query:  
            speak("Opening Quora")  
            webbrowser.open("quora.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\kaush\\Music\\EDM'    
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'current time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")  
            speak(f"The current time is {str_time}")  
        
        elif 'open code' in query:
            codePath = "C:\\Users\\kaush\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open pycharm' in query:
            pyCharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.3\\bin\\pycharm64.exe"
            os.startfile(pyCharmPath)

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                sendTo = "receiver@gmail.com"
                sendEmail(sendTo, content)
                speak("Email has been sent!")
            except Exception as e:  
                speak("An error might have occured in sending the email!")

        elif 'goodbye' in query:
            speak("Goodbye Mr.Kaushik")
            exit()
            